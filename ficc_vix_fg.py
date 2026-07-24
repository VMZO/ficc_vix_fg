import streamlit as st
import yfinance as yf
import pandas as pd
import fear_greed as fg
from datetime import date
today = date.today()

# 관련 데이터 받기
tickers = ['USDKRW=X', 'USDJPY=X', 'DX-Y.NYB', '^TNX', '^FVX', 'GC=F', 'CL=F', '^VIX']
period = '6mo'
df = yf.download(tickers, period=period, auto_adjust=True, progress=False).Close

# Fear & Greed 데이터 받기
hist = fg.get_history(last='6m')
fg_df = pd.DataFrame(hist).sort_values("date").set_index("date")

# USD/KRW
usdkrw_data = df['USDKRW=X'].dropna()
usdkrw_cur = round(usdkrw_data.iloc[-1], 2)
usdkrw_delta = usdkrw_data.pct_change(fill_method=None).iloc[-1]
usdkrw_delta_str = str(round(usdkrw_delta * 100, 2)) + '%'

# USD/JPY
usdjpy_data = df['USDJPY=X'].dropna()
usdjpy_cur = round(usdjpy_data.iloc[-1], 2)
usdjpy_delta = usdjpy_data.pct_change(fill_method=None).iloc[-1]
usdjpy_delta_str = str(round(usdjpy_delta * 100, 2)) + '%'

# DXY
dxy_data = df['DX-Y.NYB'].dropna()
dxy_cur = round(dxy_data.iloc[-1], 2)
dxy_delta = dxy_data.pct_change(fill_method=None).iloc[-1]
dxy_delta_str = str(round(dxy_delta * 100, 2)) + '%'

# US10Y
us10y_data = df['^TNX'].dropna()
us10y_cur = round(us10y_data.iloc[-1], 4)
us10y_delta = us10y_data.pct_change(fill_method=None).iloc[-1]
us10y_delta_str = str(round(us10y_delta * 100, 2)) + '%'

# US5Y
us5y_data = df['^FVX'].dropna()
us5y_cur = round(us5y_data.iloc[-1], 4)
us5y_delta = us5y_data.pct_change(fill_method=None).iloc[-1]
us5y_delta_str = str(round(us5y_delta * 100, 2)) + '%'

# GC 금선물
gc_data = df['GC=F'].dropna() 
gc_cur = round(gc_data.iloc[-1], 2)
gc_delta = gc_data.pct_change(fill_method=None).iloc[-1]
gc_delta_str = str(round(gc_delta * 100, 2)) + '%'

# WTI
wti_data = df['CL=F'].dropna() 
wti_cur = round(wti_data.iloc[-1], 2)
wti_delta = wti_data.pct_change(fill_method=None).iloc[-1]
wti_delta_str = str(round(wti_delta * 100, 2)) + '%'

# VIX
vix_data = df['^VIX'].dropna() 
vix_cur = round(vix_data.iloc[-1], 2)
vix_delta = vix_data.pct_change(fill_method=None).iloc[-1]
vix_delta_str = str(round(vix_delta * 100, 2)) + '%'

# Fear & Greed
fg_data = fg_df['score'].dropna() 
fg_cur = round(fg_data.iloc[-1], 2)
fg_delta = fg_data.pct_change(fill_method=None).iloc[-1]
fg_delta_str = str(round(fg_delta * 100, 2)) + '%'
fg_rating = fg_df['rating'].dropna().iloc[-1]


# Streamlit
st.set_page_config(
    page_title="FICC / VIX / Fear & Greed",                 # 브라우저 탭에 보일 글자
    page_icon="/home/cosmos/streamlit_app/favicon.ico",     # 파비콘 (이모지, 이미지 파일 등)
    # layout="wide",                                        # 선택 사항
)

st.title('VMZO Investment')
st.subheader('📈 FICC / VIX / Fear & Greed')
st.write(today)

a, b, c = st.columns(3)
d, e, f = st.columns(3)
g, h, i = st.columns(3)

a.metric("USD/KRW", usdkrw_cur, usdkrw_delta_str, chart_data=usdkrw_data, chart_type="line", border=True)
b.metric("USD/JPY", usdjpy_cur, usdjpy_delta_str, chart_data=usdjpy_data, chart_type="line", border=True)
c.metric("DXY", dxy_cur, dxy_delta_str, chart_data=dxy_data, chart_type="line", border=True)
d.metric("US10Y", us10y_cur, us10y_delta_str, chart_data=us10y_data, chart_type="line", border=True)
e.metric("US5Y", us5y_cur, us5y_delta_str, chart_data=us5y_data, chart_type="line", border=True)
f.metric("GC 금선물", gc_cur, gc_delta_str, chart_data=gc_data, chart_type="line", border=True)
g.metric("WTI", wti_cur, wti_delta_str, chart_data=wti_data, chart_type="line", border=True)
h.metric("VIX", vix_cur, vix_delta_str, chart_data=vix_data, chart_type="line", border=True)
i.metric(f"Fear & Greed  \n({fg_rating})", fg_cur, fg_delta_str, chart_data=fg_data, chart_type="line", border=True)


