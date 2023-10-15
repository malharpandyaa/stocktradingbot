import requests import time
# Define your API key and account ID api_key = 'YOUR_TD_API_KEY' account_id = 'YOUR_ACCOUNT_ID'
# Thinkorswim strategy ID strategy_id = 'YOUR_STRATEGY_ID'
# Thinkorswim API URL
api_url = 'https://api.tdameritrade.com/v1/accounts/{}/strategies/{}/ orders'.format(account_id, strategy_id)
# Define your trading parameters
order_qty = 100 # Number of shares to buy/sell symbol = 'AAPL' # Stock symbol to trade
side = 'BUY' # 'BUY' or 'SELL'
# ThinkScript strategy condition
condition = 'bullish' # Replace with your specific condition
while True:
# Check your ThinkScript condition here
# You may need to parse Thinkorswim data or use a custom data source
if condition:
# Place an order order_payload = {
"orderType": "LIMIT",
"session": "NORMAL",
"duration": "DAY",
"orderStrategyType": "SINGLE",
"orderLegCollection": [{"instruction": side, "quantity": order_qty,
"instrument": {"symbol": symbol}}],
"orderPricing": {"type": "LIMIT", "limit": 150.0}
}
headers = {
"Authorization": "Bearer {}".format(api_key)
}
response = requests.post(api_url, json=order_payload, headers=headers)
if response.status_code == 201:
print(f"Order placed: {side} {order_qty} {symbol}")
else:
print(f"Order failed with status code: {response.status_code}")
time.sleep(60) # Check every minute (adjust as needed)