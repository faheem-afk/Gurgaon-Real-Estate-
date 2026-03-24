import streamlit as st
import pandas as pd
import numpy as np
import joblib


st.set_page_config(page_title='Price Predictor · Gurgaon', layout="wide", initial_sidebar_state="collapsed")

if 'results' not in st.session_state:
    st.session_state['results'] = None
if 'pred_data' not in st.session_state:
    st.session_state['pred_data'] = None

df = pd.read_csv('df.csv')
pipeline = joblib.load('model.joblib')
# Block 1 — fonts and base
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
<style>
[data-testid="stHeader"] { display: none !important; }
[data-testid="stSidebar"] { display: none !important; }
[data-testid="collapsedControl"] { display: none !important; }
[data-testid="stSidebarNav"] { display: none !important; }
.block-container { padding: 2.5rem 3rem 3rem !important; max-width: 860px !important; }
section[data-testid="stMain"] { background: #FAFAF8; }
h1,h2,h3 { font-family:'DM Serif Display',serif !important; font-weight:400 !important; color:#1A1A1A !important; }
p,li,div,label,span { font-family:'DM Sans',sans-serif !important; }
</style>
""", unsafe_allow_html=True)

# Block 2 — component styles
st.markdown("""
<style>
.back-link { display:inline-flex; align-items:center; gap:6px; font-size:12px; font-weight:500; color:#888; text-decoration:none; margin-bottom:32px; font-family:'DM Sans',sans-serif; }
.back-link:hover { color:#1A1A1A; }
.page-eyebrow { font-size:11px; font-weight:500; letter-spacing:1.4px; text-transform:uppercase; color:#1D9E75; margin-bottom:10px; font-family:'DM Sans',sans-serif; }
.page-title { font-family:'DM Serif Display',serif !important; font-size:42px !important; font-weight:400 !important; color:#1A1A1A !important; line-height:1.15 !important; margin-bottom:10px !important; }
.page-sub { font-size:15px; font-weight:300; color:#777; line-height:1.7; margin-bottom:36px; font-family:'DM Sans',sans-serif; }
div[data-testid="stSelectbox"] label, div[data-testid="stNumberInput"] label { font-size:12px !important; font-weight:500 !important; color:#555 !important; text-transform:uppercase !important; font-family:'DM Sans',sans-serif !important; }
div[data-testid="stButton"] > button { background:#1A1A1A !important; color:#fff !important; border:none !important; border-radius:8px !important; padding:12px 32px !important; font-size:14px !important; font-weight:500 !important; width:100% !important; }
div[data-testid="stButton"] > button:hover { background:#333 !important; }
</style>
""", unsafe_allow_html=True)

# Block 3 — result card styles
st.markdown("""
<style>
.result-card { background:#FFFFFF; border:1px solid #EBEBEB; border-radius:12px; padding:32px; margin-top:24px; border-top:3px solid #1D9E75; }
.result-eyebrow { font-size:11px; font-weight:500; letter-spacing:1.2px; text-transform:uppercase; color:#1D9E75; margin-bottom:8px; font-family:'DM Sans',sans-serif; }
.result-range { font-family:'DM Serif Display',serif; font-size:48px; color:#1A1A1A; line-height:1; margin-bottom:6px; }
.result-sub { font-size:13px; color:#999; font-weight:300; font-family:'DM Sans',sans-serif; margin-bottom:24px; }
.result-meta-row { display:flex; gap:12px; flex-wrap:wrap; margin-top:20px; }
.result-meta { flex:1; min-width:140px; background:#FAFAF8; border:1px solid #EBEBEB; border-radius:8px; padding:14px 16px; }
.result-meta-label { font-size:10px; font-weight:500; letter-spacing:.8px; text-transform:uppercase; color:#BBB; margin-bottom:4px; font-family:'DM Sans',sans-serif; }
.result-meta-val { font-size:14px; font-weight:500; color:#1A1A1A; font-family:'DM Sans',sans-serif; }
.confidence-bar-wrap { margin-top:20px; padding-top:20px; border-top:1px solid #F0F0F0; }
.confidence-label { display:flex; justify-content:space-between; font-size:12px; color:#999; font-family:'DM Sans',sans-serif; margin-bottom:6px; }
.confidence-track { width:100%; height:6px; background:#EBEBEB; border-radius:3px; overflow:hidden; }
.confidence-fill { height:100%; background:#1D9E75; border-radius:3px; width:90%; }
.disclaimer { font-size:11px; color:#BBB; margin-top:12px; font-family:'DM Sans',sans-serif; font-weight:300; font-style:italic; }
.model-strip { display:flex; gap:8px; flex-wrap:wrap; margin-top:28px; padding-top:20px; border-top:1px solid #EBEBEB; }
.model-pill { font-size:11px; background:#FAFAF8; border:1px solid #E8E8E8; color:#888; padding:4px 12px; border-radius:20px; font-family:'DM Sans',sans-serif; }
.model-pill.accent { background:#E8F5EF; border-color:#B8DFD0; color:#1D6B4E; font-weight:500; }
</style>
""", unsafe_allow_html=True)


# ── back nav ──
st.markdown('<a class="back-link" href="/" target="_self">← Back to overview</a>', unsafe_allow_html=True)

# ── page header ──
st.markdown('<div class="page-eyebrow">Gurgaon · Price Intelligence</div>', unsafe_allow_html=True)
st.markdown('<h1 class="page-title">Get an instant price estimate</h1>', unsafe_allow_html=True)
st.markdown('<p class="page-sub">Fill in the property details below. The model will return a fair-value price range based on real market data — not listing prices.</p>', unsafe_allow_html=True)

# ── form ──
st.markdown('<div class="form-card">', unsafe_allow_html=True)
st.markdown('<div class="form-section-label">Property details</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    property_type = st.selectbox('Property type', ['flat', 'house'])
    bedroom = float(st.selectbox('Bedrooms', sorted(df['bedRoom'].astype('int').unique().tolist())))
    servant_room = st.selectbox('Servant room', ['Yes', 'No'])
    luxury_type = st.selectbox('Luxury category', ['Low', 'Medium', 'High'])

with col2:
    sector = st.selectbox('Sector', sorted(df['sector'].unique().tolist()))
    bathroom = float(st.selectbox('Bathrooms', sorted(df['bathroom'].astype('int').unique().tolist())))
    study_room = st.selectbox('Study room', ['Yes', 'No'])
    area = float(st.number_input('Built-up area (sqft)', min_value=100.0, step=50.0))

st.markdown('</div>', unsafe_allow_html=True)

# ── predict button ──
predict_clicked = st.button('Estimate price range →')

if predict_clicked:
    data = pd.DataFrame({
        'sector': [sector],
        'property_type': [property_type],
        'bedRoom': [bedroom],
        'bathroom': [bathroom],
        'builtUpArea': [area],
        'servant room': [servant_room],
        'study room': [study_room],
        'luxury_category': [luxury_type]
    })
    pred = pipeline.predict(data)
    pred = np.expm1(pred)[0]
    low  = round(pred - 0.24, 2)
    high = round(pred + 0.24, 2)
    mid  = round(pred,2)

    st.session_state['results'] = (low, high, mid)
    st.session_state['pred_data'] = {
        'type': property_type.capitalize(),
        'sector': sector.capitalize(),
        'beds': int(bedroom),
        'baths': int(bathroom),
        'area': int(area),
        'luxury': luxury_type
    }

    # ── result card ──
    if st.session_state['results'] is not None:
        low, high, mid = st.session_state['results']
        mid = str(mid)[:4]
        d = st.session_state['pred_data']

        st.markdown(f"""
        <div class="result-card">
            <div class="result-eyebrow">Estimated fair value</div>
            <div class="result-range">₹{low} – ₹{high} Cr</div>
            <div class="result-sub">Mid-point estimate · ₹{mid} Cr · Based on XGBoost model trained on Gurgaon market data</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div style="background:#FAFAF8;border:1px solid #EBEBEB;border-radius:0 0 12px 12px;padding:0 32px 32px;margin-top:-12px;">
            <div style="display:flex;gap:12px;flex-wrap:wrap;padding-top:20px;">
                <div style="flex:1;min-width:140px;background:#FFF;border:1px solid #EBEBEB;border-radius:8px;padding:14px 16px;">
                    <div style="font-size:10px;font-weight:500;letter-spacing:.8px;text-transform:uppercase;color:#BBB;margin-bottom:4px;font-family:'DM Sans',sans-serif;">Property</div>
                    <div style="font-size:14px;font-weight:500;color:#1A1A1A;font-family:'DM Sans',sans-serif;">{d['type']} · {d['sector']}</div>
                </div>
                <div style="flex:1;min-width:140px;background:#FFF;border:1px solid #EBEBEB;border-radius:8px;padding:14px 16px;">
                    <div style="font-size:10px;font-weight:500;letter-spacing:.8px;text-transform:uppercase;color:#BBB;margin-bottom:4px;font-family:'DM Sans',sans-serif;">Configuration</div>
                    <div style="font-size:14px;font-weight:500;color:#1A1A1A;font-family:'DM Sans',sans-serif;">{d['beds']} bed · {d['baths']} bath</div>
                </div>
                <div style="flex:1;min-width:140px;background:#FFF;border:1px solid #EBEBEB;border-radius:8px;padding:14px 16px;">
                    <div style="font-size:10px;font-weight:500;letter-spacing:.8px;text-transform:uppercase;color:#BBB;margin-bottom:4px;font-family:'DM Sans',sans-serif;">Built-up area</div>
                    <div style="font-size:14px;font-weight:500;color:#1A1A1A;font-family:'DM Sans',sans-serif;">{d['area']:,} sqft</div>
                </div>
                <div style="flex:1;min-width:140px;background:#FFF;border:1px solid #EBEBEB;border-radius:8px;padding:14px 16px;">
                    <div style="font-size:10px;font-weight:500;letter-spacing:.8px;text-transform:uppercase;color:#BBB;margin-bottom:4px;font-family:'DM Sans',sans-serif;">Luxury tier</div>
                    <div style="font-size:14px;font-weight:500;color:#1A1A1A;font-family:'DM Sans',sans-serif;">{d['luxury']}</div>
                </div>
            </div>
            <div style="margin-top:20px;padding-top:20px;border-top:1px solid #F0F0F0;">
                <div style="display:flex;justify-content:space-between;font-size:12px;color:#999;font-family:'DM Sans',sans-serif;margin-bottom:6px;">
                    <span>Model confidence (R² = 0.90)</span><span>90%</span>
                </div>
                <div style="width:100%;height:6px;background:#EBEBEB;border-radius:3px;overflow:hidden;">
                    <div style="height:100%;background:#1D9E75;border-radius:3px;width:90%;"></div>
                </div>
            </div>
            <p style="font-size:11px;color:#BBB;margin-top:12px;font-family:'DM Sans',sans-serif;font-style:italic;">
                Price range uses ±0.24 Cr band around the point estimate. Actual transaction prices may vary based on floor, facing, age, and negotiation.
            </p>
            <div style="display:flex;gap:8px;flex-wrap:wrap;margin-top:20px;padding-top:16px;border-top:1px solid #EBEBEB;">
                <span style="font-size:11px;background:#E8F5EF;border:1px solid #B8DFD0;color:#1D6B4E;font-weight:500;padding:4px 12px;border-radius:20px;font-family:'DM Sans',sans-serif;">XGBoost · deployed</span>
                <span style="font-size:11px;background:#FAFAF8;border:1px solid #E8E8E8;color:#888;padding:4px 12px;border-radius:20px;font-family:'DM Sans',sans-serif;">R² 0.90</span>
                <span style="font-size:11px;background:#FAFAF8;border:1px solid #E8E8E8;color:#888;padding:4px 12px;border-radius:20px;font-family:'DM Sans',sans-serif;">MAE 0.48 Cr</span>
                <span style="font-size:11px;background:#FAFAF8;border:1px solid #E8E8E8;color:#888;padding:4px 12px;border-radius:20px;font-family:'DM Sans',sans-serif;">15+ engineered features</span>
            </div>
        </div>
        """, unsafe_allow_html=True)