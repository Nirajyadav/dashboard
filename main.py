import streamlit as st
import yfinance as yf
from PIL import Image
from urllib.request import urlopen

# Title and subtitle

st.title("Cryptocurrency Daily Prices")
st.header("Main Dashboard")

# Define ticker variables
Bitcoin = "BTH-USD"
Ethereum = 'ETH-USD'
Ripple = "XRP-USD"
BitcoinCash = "BCH-USD"

#Acces the data from Yahoo finance

BTC_Data = yf.Ticker(Bitcoin)
ETH_Data = yf.Ticker(Ethereum)
XRP_Data = yf.Ticker(Ripple)
BCH_Data = yf.Ticker(BitcoinCash)

# Fetch history data from Yahoo finance
BTCHis = BTC_Data.history(period="max")
ETHHis = ETH_Data.history(period="max")
XRPHis = XRP_Data.history(period="max")
BCHHis = BCH_Data.history(period="max")

# Fetch crypto data for the dataframe
BTC = yf.download(Bitcoin,start="2022-10-01",
end="2022-10-07")
ETH = yf.download(Ethereum,start="2022-10-01",
end="2022-10-07")
XRP = yf.download(Ripple,start="2022-10-01",
end="2022-10-07")
BCH = yf.download(BitcoinCash,start="2022-10-01",
end="2022-10-07")
#Bitcoin
st.write("BITCOIN ($)")
imageBTC = Image.open(urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/1.png"))
st.image(imageBTC)
# Dispaly table
st.table(BTC)
# Display a char
st.bar_chart(BTCHis.Volume)

#Ethereum
st.write("Ethereum ($)")
imageETH = Image.open(urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png"))
st.image(imageETH)
# Dispaly table
st.table(ETH)
# Display a char
st.bar_chart(ETHHis.Volume)

#Ripple
st.write("Ripple ($)")
imageXRP = Image.open(urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/52.png"))
st.image(imageXRP)
# Dispaly table
st.table(XRP)
# Display a char
st.bar_chart(XRPHis.Volume)

#Bitcoin Cash
st.write("BITCOIN CASH ($)")
imageBCH = Image.open(urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/1831.png"))
st.image(imageBCH)
# Dispaly table
st.table(BCH)
# Display a char
st.bar_chart(BCHHis.Volume)





