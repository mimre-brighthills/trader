# Stock Trader Application

A modern, responsive stock trading application built with FastAPI that displays interactive candlestick charts with real-time stock data.

## Features

- 📈 **Interactive Candlestick Charts**: Beautiful, interactive charts powered by Plotly.js
- 💹 **Real-time Stock Data**: Live stock data from Yahoo Finance
- 📊 **Volume Analysis**: Volume bars overlaid on price charts
- 🎯 **Multiple Time Periods**: Support for various time ranges (1 day to 10 years)
- 🚀 **Popular Stocks**: Quick access to major stocks (AAPL, GOOGL, TSLA, etc.)
- 📱 **Responsive Design**: Modern, mobile-friendly interface
- 🎨 **Beautiful UI**: Clean, professional design with smooth animations
- ⚡ **Fast Performance**: Optimized for quick data loading and chart rendering

## Technology Stack

- **Backend**: FastAPI (Python)
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Charts**: Plotly.js
- **Data Source**: Yahoo Finance (via yfinance)
- **Styling**: Custom CSS with gradients and animations

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd stock-trader-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python main.py
   ```
   
   Or using uvicorn directly:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

4. **Access the application**:
   Open your browser and navigate to `http://localhost:8000`

## Usage

### Home Page
- Enter a stock symbol (e.g., AAPL, GOOGL, TSLA) in the search box
- Select your desired time period
- Click "Analyze" to view the candlestick chart
- Use the popular stocks buttons for quick access to major stocks

### Chart Page
- View interactive candlestick charts with OHLC (Open, High, Low, Close) data
- Analyze volume data in the overlaid bar chart
- Change time periods using the dropdown menu
- Navigate between different stocks using quick action buttons
- Use Plotly's built-in tools for zooming, panning, and hover information

## API Endpoints

### Web Routes
- `GET /` - Home page with stock symbol input
- `POST /chart` - Generate and display candlestick chart

### API Routes
- `GET /api/stock/{symbol}?period={period}` - Get stock data in JSON format
- `GET /api/search/{query}` - Search for stock symbols

## Features in Detail

### Candlestick Charts
- **OHLC Data**: Open, High, Low, Close prices for each time period
- **Volume Overlay**: Trading volume displayed as bars
- **Interactive Controls**: Zoom, pan, hover for detailed information
- **Professional Styling**: Dark theme optimized for financial data

### Time Periods Supported
- 1 Day (`1d`)
- 5 Days (`5d`)
- 1 Month (`1mo`)
- 3 Months (`3mo`)
- 6 Months (`6mo`)
- 1 Year (`1y`)
- 2 Years (`2y`)
- 5 Years (`5y`)
- 10 Years (`10y`)
- Year to Date (`ytd`)
- Maximum available (`max`)

### Stock Information Display
- Current stock price
- Daily change (absolute and percentage)
- Company name and stock symbol
- Real-time price updates

## Dependencies

- `fastapi==0.104.1` - Modern web framework for building APIs
- `uvicorn[standard]==0.24.0` - ASGI server for FastAPI
- `yfinance==0.2.24` - Yahoo Finance data fetching
- `plotly==5.17.0` - Interactive charting library
- `pandas==2.1.4` - Data manipulation and analysis
- `jinja2==3.1.2` - Template engine for HTML rendering
- `python-multipart==0.0.6` - Form data handling

## File Structure

```
stock-trader-app/
├── main.py                 # FastAPI application
├── requirements.txt        # Python dependencies
├── README.md              # Documentation
├── templates/             # Jinja2 templates
│   ├── base.html         # Base template with common styling
│   ├── index.html        # Home page template
│   └── chart.html        # Chart display template
└── static/               # Static files directory
    ├── css/              # Custom CSS files
    └── js/               # Custom JavaScript files
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For support, please open an issue in the GitHub repository or contact the development team.

## Future Enhancements

- [ ] User authentication and portfolios
- [ ] Real-time price alerts
- [ ] Technical indicators (RSI, MACD, etc.)
- [ ] Comparison charts for multiple stocks
- [ ] Historical news integration
- [ ] Export chart functionality
- [ ] Mobile app version