from fastapi import FastAPI

app = FastAPI(title="Stock Chatbot API")

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "ok"}

# Placeholder stock price endpoint
@app.get("/stocks/price/{symbol}")
def get_stock_price(symbol: str):
    return {"symbol": symbol, "price": "placeholder"}
