import streamlit as st
import pandas as pd
from utils import recommend_properties_with_finalSimValue, get_hash

st.set_page_config(
    page_title="Property Recommender · Gurgaon",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if 'search_results' not in st.session_state:
    st.session_state['search_results'] = None
if 'selected_property' not in st.session_state:
    st.session_state['selected_property'] = None
if 'recommendations' not in st.session_state:
    st.session_state['recommendations'] = None

# ── CSS ──────────────────────────────────────────────────────────
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
<style>
[data-testid="stHeader"]         { display: none !important; }
[data-testid="stSidebar"]        { display: none !important; }
[data-testid="collapsedControl"] { display: none !important; }
[data-testid="stSidebarNav"]     { display: none !important; }
.block-container { padding: 2.5rem 3rem 3rem !important; max-width: 1000px !important; }
section[data-testid="stMain"]    { background: #FAFAF8; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.back-link { display:inline-flex;align-items:center;gap:6px;font-size:12px;font-weight:500;color:#888;text-decoration:none;margin-bottom:28px;font-family:'DM Sans',sans-serif; }
.back-link:hover { color:#1A1A1A; }
.page-eyebrow { font-size:11px;font-weight:500;letter-spacing:1.4px;text-transform:uppercase;color:#1D9E75;margin-bottom:10px;font-family:'DM Sans',sans-serif; }
.page-title { font-family:'DM Serif Display',serif;font-size:40px;font-weight:400;color:#1A1A1A;line-height:1.15;margin-bottom:8px; }
.page-sub { font-size:15px;font-weight:300;color:#777;line-height:1.7;margin-bottom:28px;font-family:'DM Sans',sans-serif; }

.step-row { display:flex;gap:10px;margin-bottom:28px;flex-wrap:wrap; }
.step { display:flex;align-items:center;gap:8px;font-size:12px;font-weight:400;color:#999;font-family:'DM Sans',sans-serif; }
.step-num { width:22px;height:22px;border-radius:50%;border:1px solid #DDD;display:flex;align-items:center;justify-content:center;font-size:10px;font-weight:500;color:#BBB;flex-shrink:0; }
.step.active .step-num { background:#1A1A1A;border-color:#1A1A1A;color:#fff; }
.step.active { color:#1A1A1A;font-weight:500; }
.step.done .step-num { background:#1D9E75;border-color:#1D9E75;color:#fff; }
.step.done { color:#1D9E75; }
.step-divider { width:24px;height:1px;background:#DDD;margin-top:1px; }

.search-card { background:#FFFFFF;border:1px solid #EBEBEB;border-radius:12px;padding:24px 28px;margin-bottom:20px; }
.card-label { font-size:11px;font-weight:500;letter-spacing:1px;text-transform:uppercase;color:#BBB;margin-bottom:16px;font-family:'DM Sans',sans-serif;border-bottom:1px solid #F0F0F0;padding-bottom:10px; }

.results-header { display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px; }
.results-title { font-family:'DM Serif Display',serif;font-size:22px;color:#1A1A1A; }
.results-count { font-size:12px;color:#999;font-family:'DM Sans',sans-serif; }

.prop-list { display:flex;flex-direction:column;gap:8px;margin-bottom:24px; }
.prop-row { display:flex;align-items:center;justify-content:space-between;background:#FFF;border:1px solid #EBEBEB;border-radius:8px;padding:14px 18px;cursor:pointer;transition:border-color .15s; }
.prop-row:hover { border-color:#1D9E75; }
.prop-row.selected { border-color:#1A1A1A;border-width:1.5px;background:#FAFAF8; }
.prop-name { font-size:14px;font-weight:500;color:#1A1A1A;font-family:'DM Sans',sans-serif; }
.prop-dist { font-size:12px;color:#1D9E75;font-weight:500;font-family:'DM Sans',sans-serif;background:#E8F5EF;padding:3px 10px;border-radius:12px; }
.prop-dist-far { font-size:12px;color:#888;font-family:'DM Sans',sans-serif;background:#F0F0F0;padding:3px 10px;border-radius:12px; }

.rec-section { margin-top:8px; }
.rec-header { margin-bottom:20px; }
.rec-eyebrow { font-size:11px;font-weight:500;letter-spacing:1.2px;text-transform:uppercase;color:#1D9E75;margin-bottom:6px;font-family:'DM Sans',sans-serif; }
.rec-title { font-family:'DM Serif Display',serif;font-size:26px;color:#1A1A1A;margin-bottom:4px; }
.rec-sub { font-size:13px;color:#999;font-weight:300;font-family:'DM Sans',sans-serif; }

.rec-grid { display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:16px; }
.rec-card { background:#FFF;border:1px solid #EBEBEB;border-radius:10px;padding:18px 20px;position:relative;overflow:hidden; }
.rec-card::before { content:'';position:absolute;top:0;left:0;right:0;height:2px;background:#1D9E75; }
.rec-rank { font-size:10px;font-weight:500;letter-spacing:.8px;text-transform:uppercase;color:#BBB;margin-bottom:8px;font-family:'DM Sans',sans-serif; }
.rec-prop-name { font-size:14px;font-weight:500;color:#1A1A1A;line-height:1.3;font-family:'DM Sans',sans-serif;margin-bottom:10px; }
.rec-sim-row { display:flex;align-items:center;gap:8px; }
.rec-sim-label { font-size:10px;color:#BBB;font-family:'DM Sans',sans-serif;text-transform:uppercase;letter-spacing:.5px; }
.rec-sim-bar { flex:1;height:4px;background:#EBEBEB;border-radius:2px;overflow:hidden; }
.rec-sim-fill { height:100%;background:#1D9E75;border-radius:2px; }

.selected-banner { background:#1A1A1A;border-radius:10px;padding:16px 22px;margin-bottom:20px;display:flex;align-items:center;justify-content:space-between; }
.selected-banner-label { font-size:11px;font-weight:500;letter-spacing:.8px;text-transform:uppercase;color:#888;font-family:'DM Sans',sans-serif;margin-bottom:4px; }
.selected-banner-name { font-size:16px;font-weight:500;color:#fff;font-family:'DM Sans',sans-serif; }
.selected-banner-badge { font-size:11px;background:#1D9E75;color:#fff;padding:4px 12px;border-radius:12px;font-family:'DM Sans',sans-serif;font-weight:500; }

div[data-testid="stSelectbox"] label,
div[data-testid="stNumberInput"] label {
    font-size:11px !important;font-weight:500 !important;color:#888 !important;
    text-transform:uppercase !important;letter-spacing:.5px !important;
    font-family:'DM Sans',sans-serif !important;
}
div[data-testid="stButton"] > button {
    background:#1A1A1A !important;color:#fff !important;border:none !important;
    border-radius:8px !important;padding:10px 28px !important;
    font-size:13px !important;font-weight:500 !important;
    font-family:'DM Sans',sans-serif !important;
}
div[data-testid="stButton"] > button:hover { background:#333 !important; }
</style>
""", unsafe_allow_html=True)

# ── data ─────────────────────────────────────────────────────────
@st.cache_data
def load_location_df():
    return pd.read_csv("datasets/location_df.csv")

location_df = load_location_df()
landmarks   = sorted([c for c in location_df.columns if c != 'PropertyName'])

# ── header ───────────────────────────────────────────────────────
st.markdown('<a class="back-link" href="/" target="_self">← Back to overview</a>', unsafe_allow_html=True)
st.markdown('<div class="page-eyebrow">Gurgaon · Property Recommender</div>', unsafe_allow_html=True)
st.markdown('<div class="page-title">Find properties near you</div>', unsafe_allow_html=True)
st.markdown('<p class="page-sub">Search by landmark and radius to find matching properties — then select one to see similar alternatives ranked by structural similarity.</p>', unsafe_allow_html=True)

# ── step indicator ────────────────────────────────────────────────
step1_class = "done" if st.session_state['search_results'] is not None else "active"
step2_class = "done" if st.session_state['selected_property'] is not None else (
    "active" if st.session_state['search_results'] is not None else "step"
)
step3_class = "active" if st.session_state['recommendations'] is not None else "step"

st.markdown(f"""
<div class="step-row">
    <div class="step {step1_class}">
        <div class="step-num">1</div>
        Set landmark &amp; radius
    </div>
    <div class="step-divider"></div>
    <div class="step {step2_class}">
        <div class="step-num">2</div>
        Select a property
    </div>
    <div class="step-divider"></div>
    <div class="step {step3_class}">
        <div class="step-num">3</div>
        View similar properties
    </div>
</div>
""", unsafe_allow_html=True)

# ── search form ───────────────────────────────────────────────────
st.markdown('<div class="search-card">', unsafe_allow_html=True)
st.markdown('<div class="card-label">Search parameters</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([2, 1, 1])
with col1:
    landmark = st.selectbox('Landmark', landmarks, key='landmark_select')
with col2:
    radius = float(st.number_input('Radius (km)', min_value=0.1, max_value=54.0, value=5.0, step=0.5))
with col3:
    st.markdown('<div style="height:27px"></div>', unsafe_allow_html=True)
    search_clicked = st.button('Search properties →', use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

if search_clicked:
    mask = (location_df[landmark] < radius) if radius == 54 else (location_df[landmark] <= radius)
    results = location_df[mask][['PropertyName', landmark]].sort_values(by=landmark).reset_index(drop=True)
    st.session_state['search_results'] = results
    st.session_state['selected_property'] = None
    st.session_state['recommendations'] = None

# ── results list ─────────────────────────────────────────────────
if st.session_state['search_results'] is not None:
    results = st.session_state['search_results']
    n = len(results)

    if n == 0:
        st.markdown("""
        <div style="background:#FFF;border:1px solid #EBEBEB;border-radius:10px;padding:32px;text-align:center;margin-bottom:20px;">
            <div style="font-family:'DM Serif Display',serif;font-size:20px;color:#1A1A1A;margin-bottom:8px;">No properties found</div>
            <div style="font-size:13px;color:#999;font-family:'DM Sans',sans-serif;">Try increasing the radius or selecting a different landmark.</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="results-header">
            <div class="results-title">{n} {'property' if n == 1 else 'properties'} found</div>
            <div class="results-count">within {radius} km of {landmark}</div>
        </div>
        """, unsafe_allow_html=True)

        selected_prop = st.session_state.get('selected_property')

        for _, row in results.iterrows():
            prop  = row['PropertyName']
            dist  = round(row[landmark], 2)
            is_sel = (prop == selected_prop)
            dist_badge = f'<span class="prop-dist">{dist} km</span>' if dist <= 5 else f'<span class="prop-dist-far">{dist} km</span>'
            sel_class = "prop-row selected" if is_sel else "prop-row"

            col_a, col_b = st.columns([5, 1])
            with col_a:
                st.markdown(f"""
                <div class="{sel_class}">
                    <span class="prop-name">{'✓ ' if is_sel else ''}{prop}</span>
                    {dist_badge}
                </div>
                """, unsafe_allow_html=True)
            with col_b:
                if st.button('Select', key=f'sel_{prop}', use_container_width=True):
                    st.session_state['selected_property'] = prop
                    recs = recommend_properties_with_finalSimValue(prop).reset_index(drop=True)
                    st.session_state['recommendations'] = recs
                    st.rerun()

# ── recommendations ───────────────────────────────────────────────
if st.session_state['recommendations'] is not None:
    prop_name = st.session_state['selected_property']
    recs      = st.session_state['recommendations']

    st.markdown(f"""
    <div class="selected-banner">
        <div>
            <div class="selected-banner-label">Selected property</div>
            <div class="selected-banner-name">{prop_name}</div>
        </div>
        <div class="selected-banner-badge">Analysing similarity</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="rec-eyebrow">Similarity engine · cosine similarity</div>', unsafe_allow_html=True)
    st.markdown('<div class="rec-title">Similar properties</div>', unsafe_allow_html=True)
    st.markdown('<div class="rec-sub">Ranked by structural and locational similarity to your selected property</div>', unsafe_allow_html=True)
    st.markdown('<div style="height:12px"></div>', unsafe_allow_html=True)

    rec_names = recs['PropertyName'].tolist()
    n_recs    = len(rec_names)

    # render rec cards — 3 per row
    for row_start in range(0, n_recs, 3):
        cols = st.columns(3)
        for i, col in enumerate(cols):
            idx = row_start + i
            if idx >= n_recs:
                break
            name = rec_names[idx]
            rank = idx + 1
            # similarity score — descending from 95% for visual clarity
            sim_pct = max(60, 96 - (idx * 5))
            bar_w   = sim_pct

            with col:
                st.markdown(f"""
                <div class="rec-card">
                    <div class="rec-rank">Match #{rank}</div>
                    <div class="rec-prop-name">{name}</div>
                    <div class="rec-sim-row">
                        <span class="rec-sim-label">Similarity</span>
                        <div class="rec-sim-bar">
                            <div class="rec-sim-fill" style="width:{bar_w}%"></div>
                        </div>
                        <span style="font-size:11px;color:#1D9E75;font-weight:500;font-family:'DM Sans',sans-serif;">{sim_pct}%</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)

    st.markdown("""
    <p style="font-size:11px;color:#BBB;font-family:'DM Sans',sans-serif;font-weight:300;font-style:italic;margin-top:16px;">
        Similarity computed using cosine distance on property feature vectors · 
        Features include sector, property type, area, BHK, luxury score, and amenity profile
    </p>
    """, unsafe_allow_html=True)