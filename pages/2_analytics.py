import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

st.set_page_config(
    page_title="Analytics · Gurgaon Property",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── CSS ──────────────────────────────────────────────────────────
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
<style>
[data-testid="stHeader"]         { display: none !important; }
[data-testid="stSidebar"]        { display: none !important; }
[data-testid="collapsedControl"] { display: none !important; }
[data-testid="stSidebarNav"]     { display: none !important; }
.block-container { padding: 2.5rem 3rem 3rem !important; max-width: 1100px !important; }
section[data-testid="stMain"]    { background: #FAFAF8; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.back-link { display:inline-flex; align-items:center; gap:6px; font-size:12px; font-weight:500; color:#888; text-decoration:none; margin-bottom:28px; font-family:'DM Sans',sans-serif; }
.back-link:hover { color:#1A1A1A; }
.page-eyebrow { font-size:11px; font-weight:500; letter-spacing:1.4px; text-transform:uppercase; color:#1D9E75; margin-bottom:10px; font-family:'DM Sans',sans-serif; }
.page-title { font-family:'DM Serif Display',serif; font-size:40px; font-weight:400; color:#1A1A1A; line-height:1.15; margin-bottom:8px; }
.page-sub { font-size:15px; font-weight:300; color:#777; line-height:1.7; margin-bottom:8px; font-family:'DM Sans',sans-serif; }
.insight-box { background:#1A1A1A; border-radius:10px; padding:18px 22px; margin:16px 0 24px; display:flex; gap:14px; align-items:flex-start; }
.insight-dot { width:6px; height:6px; border-radius:50%; background:#1D9E75; flex-shrink:0; margin-top:6px; }
.insight-text { font-size:13px; font-weight:300; color:#C8C8C8; line-height:1.65; font-family:'DM Sans',sans-serif; }
.insight-text strong { color:#fff; font-weight:500; }
.chart-label { font-size:11px; font-weight:500; letter-spacing:1px; text-transform:uppercase; color:#1D9E75; margin-bottom:6px; font-family:'DM Sans',sans-serif; }
.chart-title { font-family:'DM Serif Display',serif; font-size:22px; color:#1A1A1A; margin-bottom:4px; }
.chart-sub { font-size:13px; color:#999; font-weight:300; font-family:'DM Sans',sans-serif; margin-bottom:16px; }
.stat-strip { display:flex; gap:0; border:1px solid #EBEBEB; border-radius:10px; overflow:hidden; background:#FFF; margin-bottom:24px; }
.stat-item { flex:1; padding:18px 16px; text-align:center; border-right:1px solid #EBEBEB; }
.stat-item:last-child { border-right:none; }
.stat-num { font-family:'DM Serif Display',serif; font-size:26px; color:#1A1A1A; line-height:1; margin-bottom:4px; }
.stat-desc { font-size:11px; color:#999; font-family:'DM Sans',sans-serif; }

/* tab styling */
div[data-testid="stTabs"] button {
    font-family: 'DM Sans', sans-serif !important;
    font-size: 13px !important;
    font-weight: 500 !important;
    color: #888 !important;
    letter-spacing: 0.3px !important;
}
div[data-testid="stTabs"] button[aria-selected="true"] {
    color: #1A1A1A !important;
    border-bottom-color: #1D9E75 !important;
}
div[data-testid="stSelectbox"] label {
    font-size: 11px !important; font-weight: 500 !important;
    color: #888 !important; text-transform: uppercase !important;
    letter-spacing: 0.5px !important; font-family: 'DM Sans', sans-serif !important;
}
</style>
""", unsafe_allow_html=True)

# ── data ─────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    df       = pd.read_csv('datasets/gurgaon_properties_missing_value_imputed.csv')
    wc_df    = pd.read_csv('datasets/word_cloud_df.csv')
    group_df = pd.read_csv('datasets/group_df.csv')
    return df, wc_df, group_df

df, wc_df, group_df = load_data()

# ── header ───────────────────────────────────────────────────────
st.markdown('<a class="back-link" href="/" target="_self">← Back to overview</a>', unsafe_allow_html=True)
st.markdown('<div class="page-eyebrow">Gurgaon · Market Analytics</div>', unsafe_allow_html=True)
st.markdown('<div class="page-title">Property market intelligence</div>', unsafe_allow_html=True)
st.markdown('<p class="page-sub">Six analytical lenses on the Gurgaon real estate market — from pricing patterns to neighbourhood DNA.</p>', unsafe_allow_html=True)

# ── summary stats strip ───────────────────────────────────────────
total      = len(df)
avg_price  = round(df['price'].mean(), 2)
avg_area   = round(df['builtUpArea'].mean())
sectors    = df['sector'].nunique()

st.markdown(f"""
<div class="stat-strip">
  <div class="stat-item"><div class="stat-num">{total:,}</div><div class="stat-desc">Total listings</div></div>
  <div class="stat-item"><div class="stat-num">₹{avg_price} Cr</div><div class="stat-desc">Avg listing price</div></div>
  <div class="stat-item"><div class="stat-num">{avg_area:,}</div><div class="stat-desc">Avg area (sqft)</div></div>
  <div class="stat-item"><div class="stat-num">{sectors}</div><div class="stat-desc">Sectors covered</div></div>
</div>
""", unsafe_allow_html=True)

# ── tabs ──────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Market overview",
    "Area vs price",
    "Sector intelligence",
    "BHK analysis",
    "Neighbourhood DNA"
])


# ══════════════════════════════════════════
# TAB 1 — Market overview
# ══════════════════════════════════════════
with tab1:
    st.markdown('<div style="height:20px"></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="insight-box">
        <div class="insight-dot"></div>
        <div class="insight-text">
            <strong>Key finding:</strong> Flats dominate the Gurgaon market by volume, but houses show a wider price distribution — 
            suggesting higher variance in land value across sectors. The overlap zone (₹1–3 Cr) is where most transactions occur.
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="chart-label">Price distribution</div>', unsafe_allow_html=True)
        st.markdown('<div class="chart-title">Flat vs house pricing</div>', unsafe_allow_html=True)
        st.markdown('<div class="chart-sub">Density curves showing price spread by property type</div>', unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(6, 4))
        fig.patch.set_facecolor('#FAFAF8')
        ax.set_facecolor('#FAFAF8')
        sns.histplot(data=df[df['property_type'] == 'house'], x='price',
                     color='#1A1A1A', label='House', kde=True,
                     stat='density', alpha=0.15, ax=ax)
        sns.histplot(data=df[df['property_type'] == 'flat'], x='price',
                     color='#1D9E75', label='Flat', kde=True,
                     stat='density', alpha=0.15, ax=ax)
        ax.legend(frameon=False, fontsize=10)
        ax.set_xlabel('Price (₹ Cr)', fontsize=10, color='#888')
        ax.set_ylabel('Density', fontsize=10, color='#888')
        ax.tick_params(colors='#AAA', labelsize=9)
        for spine in ax.spines.values():
            spine.set_edgecolor('#EBEBEB')
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    with col2:
        st.markdown('<div class="chart-label">BHK split</div>', unsafe_allow_html=True)
        st.markdown('<div class="chart-title">Overall bedroom distribution</div>', unsafe_allow_html=True)
        st.markdown('<div class="chart-sub">Share of listings by bedroom count across all sectors</div>', unsafe_allow_html=True)
        fig = px.pie(
            df, names='bedRoom',
            color_discrete_sequence=['#1A1A1A','#1D9E75','#5DCAA5','#9FE1CB','#D3D1C7'],
            hole=0.45
        )
        fig.update_layout(
            paper_bgcolor='#FAFAF8', plot_bgcolor='#FAFAF8',
            font_family='DM Sans', font_color='#555',
            legend=dict(orientation='v', font=dict(size=11)),
            margin=dict(l=0, r=0, t=10, b=0), height=320
        )
        fig.update_traces(textposition='inside', textinfo='percent+label',
                          textfont_size=11)
        st.plotly_chart(fig, use_container_width=True)


# ══════════════════════════════════════════
# TAB 2 — Area vs price
# ══════════════════════════════════════════
with tab2:
    st.markdown('<div style="height:20px"></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="insight-box">
        <div class="insight-dot"></div>
        <div class="insight-text">
            <strong>Key finding:</strong> Area is a strong price predictor up to ~3,000 sqft — beyond that, 
            price variance increases sharply, driven by sector location and luxury tier rather than size alone. 
            4+ BHK listings cluster in the high-price, high-area quadrant as expected.
        </div>
    </div>
    """, unsafe_allow_html=True)

    prop_type = st.selectbox('Property type', ['flat', 'house'], key='scatter_type')

    st.markdown('<div class="chart-label">Scatter analysis</div>', unsafe_allow_html=True)
    st.markdown('<div class="chart-title">Built-up area vs listing price</div>', unsafe_allow_html=True)
    st.markdown('<div class="chart-sub">Each point is a listing — coloured by bedroom count</div>', unsafe_allow_html=True)

    viz_df = df[df['property_type'] == prop_type]
    fig = px.scatter(
        viz_df, x='builtUpArea', y='price', color='bedRoom',
        color_continuous_scale=['#D3D1C7','#9FE1CB','#1D9E75','#0F6E56','#1A1A1A'],
        labels={'builtUpArea': 'Built-up area (sqft)', 'price': 'Price (₹ Cr)', 'bedRoom': 'Bedrooms'},
        height=480, opacity=0.65
    )
    fig.update_layout(
        paper_bgcolor='#FAFAF8', plot_bgcolor='#FFFFFF',
        font_family='DM Sans', font_color='#555',
        xaxis=dict(gridcolor='#F0F0F0', linecolor='#EBEBEB', title_font_size=12),
        yaxis=dict(gridcolor='#F0F0F0', linecolor='#EBEBEB', title_font_size=12),
        margin=dict(l=0, r=0, t=10, b=0)
    )
    fig.update_traces(marker=dict(size=6))
    st.plotly_chart(fig, use_container_width=True)


# ══════════════════════════════════════════
# TAB 3 — Sector intelligence
# ══════════════════════════════════════════
with tab3:
    st.markdown('<div style="height:20px"></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="insight-box">
        <div class="insight-dot"></div>
        <div class="insight-text">
            <strong>Key finding:</strong> Price per sqft varies dramatically by geography — not just by sector name. 
            The geomap reveals spatial clustering of premium pricing, validating location as the dominant feature 
            in the prediction model. Sectors near Golf Course Road consistently command the highest rates.
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])
    with col2:
        st.markdown('<div class="chart-label">Sector BHK split</div>', unsafe_allow_html=True)
        sector_pie = st.selectbox(
            'Filter by sector',
            ['Overall'] + sorted(df['sector'].unique()),
            key='sector_pie'
        )

    st.markdown('<div class="chart-label">Geomap</div>', unsafe_allow_html=True)
    st.markdown('<div class="chart-title">Price per sqft across Gurgaon</div>', unsafe_allow_html=True)
    st.markdown('<div class="chart-sub">Bubble size = built-up area · Colour = price per sqft</div>', unsafe_allow_html=True)

    fig = px.scatter_mapbox(
        group_df, lat='latitude', lon='longitude',
        color='price_per_sqft', size='builtUpArea',
        color_continuous_scale=['#9FE1CB','#1D9E75','#0F6E56','#1A1A1A'],
        zoom=10, mapbox_style='open-street-map',
        height=480, hover_name=group_df.index
    )
    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        font_family='DM Sans',
        coloraxis_colorbar=dict(x=.97, xanchor='left', len=0.75, thickness=12,
                                title=dict(text='₹/sqft', font=dict(size=11)))
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown('<div style="height:16px"></div>', unsafe_allow_html=True)
    st.markdown('<div class="chart-label">BHK breakdown</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="chart-title">Bedroom split — {sector_pie}</div>', unsafe_allow_html=True)

    pie_data = df if sector_pie == 'Overall' else df[df['sector'] == sector_pie]
    fig = px.pie(
        pie_data, names='bedRoom',
        color_discrete_sequence=['#1A1A1A','#1D9E75','#5DCAA5','#9FE1CB','#D3D1C7'],
        hole=0.45
    )
    fig.update_layout(
        paper_bgcolor='#FAFAF8', font_family='DM Sans',
        margin=dict(l=0, r=0, t=10, b=0), height=280
    )
    fig.update_traces(textposition='inside', textinfo='percent+label', textfont_size=10)
    st.plotly_chart(fig, use_container_width=True)


# ══════════════════════════════════════════
# TAB 4 — BHK analysis
# ══════════════════════════════════════════
with tab4:
    st.markdown('<div style="height:20px"></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="insight-box">
        <div class="insight-dot"></div>
        <div class="insight-text">
            <strong>Key finding:</strong> Price variance increases with bedroom count — 3 BHK shows the widest 
            distribution, reflecting high sector-level variability for mid-range properties. 
            1 BHK is tightly clustered under ₹1 Cr, making it the most predictable segment.
        </div>
    </div>
    """, unsafe_allow_html=True)

    sector_box = st.selectbox(
        'Filter by sector',
        ['Overall'] + sorted(df['sector'].unique()),
        key='sector_box'
    )

    st.markdown('<div class="chart-label">Box plot</div>', unsafe_allow_html=True)
    st.markdown('<div class="chart-title">Price variation by bedroom count</div>', unsafe_allow_html=True)
    st.markdown('<div class="chart-sub">Median, IQR, and outliers — filtered to 1–4 BHK for clarity</div>', unsafe_allow_html=True)

    box_df = df if sector_box == 'Overall' else df[df['sector'] == sector_box]
    box_df = box_df[box_df['bedRoom'] <= 4]

    fig = px.box(
        box_df, x='bedRoom', y='price',
        color='bedRoom',
        color_discrete_sequence=['#D3D1C7','#9FE1CB','#1D9E75','#0F6E56'],
        labels={'bedRoom': 'Bedrooms', 'price': 'Price (₹ Cr)'},
        height=440
    )
    fig.update_layout(
        paper_bgcolor='#FAFAF8', plot_bgcolor='#FFFFFF',
        font_family='DM Sans', font_color='#555',
        showlegend=False,
        xaxis=dict(gridcolor='#F0F0F0', linecolor='#EBEBEB'),
        yaxis=dict(gridcolor='#F0F0F0', linecolor='#EBEBEB'),
        margin=dict(l=0, r=0, t=10, b=0)
    )
    st.plotly_chart(fig, use_container_width=True)


# ══════════════════════════════════════════
# TAB 5 — Neighbourhood DNA
# ══════════════════════════════════════════
with tab5:
    st.markdown('<div style="height:20px"></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="insight-box">
        <div class="insight-dot"></div>
        <div class="insight-text">
            <strong>Key finding:</strong> Feature text extracted from listings reveals what each sector 
            is actually selling — premium sectors lead with amenity keywords (gym, pool, concierge) 
            while peripheral sectors surface structural terms (parking, lift, security). 
            This signal directly informed the luxury_score feature in the prediction model.
        </div>
    </div>
    """, unsafe_allow_html=True)

    sector_wc = st.selectbox(
        'Select sector',
        sorted(wc_df['sector'].unique()),
        key='sector_wc'
    )

    st.markdown('<div class="chart-label">Word cloud</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="chart-title">Listing features — {sector_wc}</div>', unsafe_allow_html=True)
    st.markdown('<div class="chart-sub">Most frequent amenity and feature keywords from raw listing text</div>', unsafe_allow_html=True)

    feature_text = []
    for i in wc_df[wc_df['sector'] == sector_wc]['features'].values:
        feature_text += map(
            lambda x: x.replace("'", ""),
            i.replace("[", "").replace("]", "").split(",")
        )
    feature_text = ' '.join(feature_text)

    wordcloud = WordCloud(
        width=900, height=420,
        background_color='#FAFAF8',
        colormap='Greens',
        stopwords=set(['s']),
        min_font_size=11,
        prefer_horizontal=0.85
    ).generate(feature_text)

    fig, ax = plt.subplots(figsize=(9, 4.2))
    fig.patch.set_facecolor('#FAFAF8')
    ax.set_facecolor('#FAFAF8')
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    plt.tight_layout(pad=0)
    st.pyplot(fig)
    plt.close()

    st.markdown("""
    <p style="font-size:12px;color:#BBB;font-family:'DM Sans',sans-serif;font-weight:300;font-style:italic;margin-top:8px;">
        Text extracted from raw 99acres.com listing descriptions · Stopwords removed · Min frequency threshold applied
    </p>
    """, unsafe_allow_html=True)