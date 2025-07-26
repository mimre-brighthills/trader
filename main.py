from fastapi import FastAPI, Request, HTTPException, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import yfinance as yf
import plotly.graph_objects as go
import plotly.utils
import pandas as pd
from datetime import datetime, timedelta
import json
from typing import Optional

app = FastAPI(title="Stock Trader Application", description="A trading application with candlestick charts")

# Setup templates
templates = Jinja2Templates(directory="templates")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Home page with stock symbol input"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chart", response_class=HTMLResponse)
async def get_chart(request: Request, symbol: str = Form(...), period: str = Form("1mo")):
    """Generate candlestick chart for the given stock symbol"""
    try:
        # Fetch stock data
        stock = yf.Ticker(symbol.upper())
        hist = stock.history(period=period)
        
        if hist.empty:
            raise HTTPException(status_code=404, detail="Stock symbol not found or no data available")
        
        # Get stock info
        info = stock.info
        company_name = info.get('longName', symbol.upper())
        current_price = info.get('currentPrice', hist['Close'].iloc[-1])
        
        # Create candlestick chart
        fig = go.Figure(data=go.Candlestick(
            x=hist.index,
            open=hist['Open'],
            high=hist['High'],
            low=hist['Low'],
            close=hist['Close'],
            name=symbol.upper()
        ))
        
        # Add volume subplot
        fig.add_trace(go.Bar(
            x=hist.index,
            y=hist['Volume'],
            name='Volume',
            yaxis='y2',
            marker_color='rgba(158,202,225,0.5)'
        ))
        
        # Update layout
        fig.update_layout(
            title=f'{company_name} ({symbol.upper()}) - Current Price: ${current_price:.2f}',
            yaxis_title='Stock Price (USD)',
            yaxis2=dict(
                title='Volume',
                overlaying='y',
                side='right',
                showgrid=False
            ),
            xaxis_title='Date',
            template='plotly_dark',
            height=600,
            showlegend=True,
            xaxis_rangeslider_visible=False
        )
        
        # Convert to JSON for embedding in HTML
        chart_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        
        # Calculate daily change
        prev_close = hist['Close'].iloc[-2] if len(hist) > 1 else hist['Close'].iloc[-1]
        daily_change = current_price - prev_close
        daily_change_pct = (daily_change / prev_close) * 100
        
        return templates.TemplateResponse("chart.html", {
            "request": request,
            "chart_json": chart_json,
            "symbol": symbol.upper(),
            "company_name": company_name,
            "current_price": current_price,
            "daily_change": daily_change,
            "daily_change_pct": daily_change_pct,
            "period": period
        })
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching data: {str(e)}")

@app.get("/api/stock/{symbol}")
async def get_stock_data(symbol: str, period: str = "1mo"):
    """API endpoint to get stock data in JSON format"""
    try:
        stock = yf.Ticker(symbol.upper())
        hist = stock.history(period=period)
        
        if hist.empty:
            raise HTTPException(status_code=404, detail="Stock symbol not found")
        
        # Convert to JSON-serializable format
        data = {
            "symbol": symbol.upper(),
            "data": []
        }
        
        for index, row in hist.iterrows():
            data["data"].append({
                "date": index.strftime("%Y-%m-%d"),
                "open": float(row['Open']),
                "high": float(row['High']),
                "low": float(row['Low']),
                "close": float(row['Close']),
                "volume": int(row['Volume'])
            })
        
        return data
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching data: {str(e)}")

@app.get("/api/search/{query}")
async def search_stocks(query: str):
    """Search for stock symbols"""
    try:
        # This is a simple implementation - in production, you'd use a proper stock search API
        ticker = yf.Ticker(query.upper())
        info = ticker.info
        
        if 'symbol' in info:
            return {
                "results": [{
                    "symbol": info.get('symbol', query.upper()),
                    "name": info.get('longName', 'Unknown'),
                    "exchange": info.get('exchange', 'Unknown')
                }]
            }
        else:
            return {"results": []}
            
    except Exception as e:
        return {"results": []}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)