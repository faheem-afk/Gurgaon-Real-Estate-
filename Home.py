import streamlit as st

st.set_page_config(
    page_title="Gurgaon Property Pricer",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
<style>
[data-testid="stHeader"] { display: none !important; }
[data-testid="stSidebar"] { display: none !important; }
.block-container { padding: 2rem 3rem 3rem !important; max-width: 900px !important; }
section[data-testid="stMain"] { background: #FAFAF8; }
h1,h2,h3{font-family:'DM Serif Display',serif !important;font-weight:400 !important;color:#1A1A1A !important;}
p,li,span,div,label{font-family:'DM Sans',sans-serif !important;}
.eyebrow{display:inline-block;font-size:11px;font-weight:500;letter-spacing:1.4px;text-transform:uppercase;color:#1D6B4E;background:#E8F5EF;border:1px solid #B8DFD0;padding:5px 14px;border-radius:20px;margin-bottom:16px;}
.hero-title{font-family:'DM Serif Display',serif !important;font-size:52px !important;font-weight:400 !important;color:#1A1A1A !important;line-height:1.15 !important;letter-spacing:-0.5px !important;margin-bottom:16px !important;}
.hero-title em{font-style:italic;color:#1D9E75;}
.hero-sub{font-size:16px !important;font-weight:300 !important;color:#666 !important;line-height:1.75 !important;margin-bottom:32px !important;}
.stats-row{display:flex;gap:0;border:1px solid #EBEBEB;border-radius:10px;overflow:hidden;background:#FFF;margin:40px 0 48px;}
.stat-item{flex:1;padding:24px 20px;text-align:center;border-right:1px solid #EBEBEB;}
.stat-item:last-child{border-right:none;}
.stat-num{font-family:'DM Serif Display',serif;font-size:34px;color:#1A1A1A;line-height:1;margin-bottom:6px;}
.stat-desc{font-size:12px;color:#999;}
.section-tag{font-size:11px;font-weight:500;letter-spacing:1.4px;text-transform:uppercase;color:#1D9E75;margin-bottom:8px;}
.section-h{font-family:'DM Serif Display',serif;font-size:30px;font-weight:400;color:#1A1A1A;line-height:1.2;margin-bottom:10px;}
.section-body{font-size:14px;font-weight:300;color:#666;line-height:1.75;margin-bottom:28px;}
.divider{border:none;border-top:1px solid #EBEBEB;margin:48px 0;}
.pipeline{display:flex;align-items:center;flex-wrap:wrap;margin:20px 0 8px;}
.pip-node{font-size:13px;font-weight:500;padding:9px 18px;border:1px solid #D8D8D8;border-radius:6px;background:#FFF;color:#1A1A1A;white-space:nowrap;margin:4px 4px 4px 0;}
.pip-node.active{background:#1A1A1A;color:#fff;border-color:#1A1A1A;}
.pip-arrow{font-size:16px;color:#C8C8C8;padding:0 4px;}
.prob-grid{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:20px 0;}
.prob-card{background:#FFF;border:1px solid #EBEBEB;border-radius:10px;padding:22px;}
.prob-num{font-family:'DM Serif Display',serif;font-size:26px;color:#E8E4DF;line-height:1;margin-bottom:8px;}
.prob-title{font-size:13px;font-weight:500;color:#1A1A1A;margin-bottom:5px;}
.prob-body{font-size:12px;font-weight:300;color:#888;line-height:1.6;}
.feat-grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px;margin:20px 0;}
.feat-card{background:#FAFAF8;border:1px solid #EBEBEB;border-radius:10px;padding:18px;border-top:2px solid #1D9E75;}
.feat-mono{font-family:monospace;font-size:11px;color:#1D6B4E;background:#E8F5EF;padding:3px 8px;border-radius:4px;display:inline-block;margin-bottom:8px;}
.feat-title{font-size:13px;font-weight:500;color:#1A1A1A;margin-bottom:5px;}
.feat-body{font-size:12px;font-weight:300;color:#888;line-height:1.55;}
.model-wrap{border:1px solid #EBEBEB;border-radius:10px;overflow:hidden;background:#FFF;margin:20px 0;}
.model-table{width:100%;border-collapse:collapse;font-size:13px;}
.model-table th{padding:12px 18px;text-align:left;font-size:11px;font-weight:500;letter-spacing:.8px;text-transform:uppercase;color:#999;border-bottom:1px solid #EBEBEB;background:#FAFAF8;}
.model-table td{padding:14px 18px;border-bottom:1px solid #F0F0F0;color:#1A1A1A;font-size:13px;}
.model-table tr:last-child td{border-bottom:none;}
.model-table tr.best td{background:#F2FAF6;}
.model-table tr.best td:first-child{border-left:3px solid #1D9E75;padding-left:15px;}
.dep-badge{font-size:10px;font-weight:500;background:#1D9E75;color:#fff;padding:2px 8px;border-radius:10px;margin-left:8px;}
.bar-wrap{display:flex;align-items:center;gap:8px;}
.bar-track{width:70px;height:5px;background:#EBEBEB;border-radius:3px;overflow:hidden;display:inline-block;}
.bar-fill{height:100%;background:#1D9E75;border-radius:3px;}
.bar-dim{height:100%;background:#C8DDD6;border-radius:3px;}
.bar-dimmer{height:100%;background:#DCDCDC;border-radius:3px;}
.insight{background:#1A1A1A;color:#fff;border-radius:10px;padding:26px 30px;margin-top:20px;display:flex;gap:18px;align-items:flex-start;}
.insight-quote{font-family:'DM Serif Display',serif;font-size:40px;color:#1D9E75;line-height:1;flex-shrink:0;}
.insight-text{font-size:14px;font-weight:300;color:#C8C8C8;line-height:1.7;}
.insight-text strong{color:#fff;font-weight:500;}
.tech-row{display:flex;flex-wrap:wrap;gap:8px;margin-top:16px;}
.tech-pill{font-size:13px;background:#FFF;border:1px solid #D8D8D8;color:#1A1A1A;padding:6px 14px;border-radius:20px;}
.footer-wrap{background:#1A1A1A;border-radius:10px;padding:32px 40px;text-align:center;margin-top:48px;}
.footer-name{font-family:'DM Serif Display',serif;font-size:20px;color:#fff;margin-bottom:8px;}
.footer-links{font-size:13px;color:#888;}
.footer-links a{color:#1D9E75;text-decoration:none;}
</style>
""", unsafe_allow_html=True)

# HERO
st.markdown('<div class="eyebrow">Gurgaon · Real Estate Intelligence</div>', unsafe_allow_html=True)
st.markdown('<h1 class="hero-title">What should this property <em>actually</em> be worth?</h1>', unsafe_allow_html=True)
st.markdown('<p class="hero-sub">Most platforms show you listings. This system prices them — using scraped market data, rigorous feature engineering, and a production XGBoost pipeline deployed live.</p>', unsafe_allow_html=True)

c1, c2, c3 = st.columns([1, 1, 1])
with c1:
    if st.button("Get a price estimate →", type="primary", use_container_width=True):
        st.switch_page("pages/1_price_prediction.py")
with c2:
    if st.button("Find similar properties", use_container_width=True):
        st.switch_page("pages/3_recommender_system.py")
with c3:
    if st.button("Want to look at analytics?", use_container_width=True):
        st.switch_page("pages/2_analytics.py")

st.markdown("""
<div class="stats-row">
  <div class="stat-item"><div class="stat-num">0.90</div><div class="stat-desc">R² score</div></div>
  <div class="stat-item"><div class="stat-num">0.48</div><div class="stat-desc">MAE in ₹ crores</div></div>
  <div class="stat-item"><div class="stat-num">50.5%</div><div class="stat-desc">lower error vs baseline</div></div>
  <div class="stat-item"><div class="stat-num">15+</div><div class="stat-desc">engineered features</div></div>
</div>
<hr class="divider">
""", unsafe_allow_html=True)

# PIPELINE
st.markdown('<div class="section-tag">End-to-end pipeline</div>', unsafe_allow_html=True)
st.markdown("""
<div class="pipeline">
  <div class="pip-node">Web scraping</div><div class="pip-arrow">→</div>
  <div class="pip-node">Data cleaning</div><div class="pip-arrow">→</div>
  <div class="pip-node">Feature engineering</div><div class="pip-arrow">→</div>
  <div class="pip-node">Modelling</div><div class="pip-arrow">→</div>
  <div class="pip-node active">Deployment</div>
</div>
<p style="font-size:12px;color:#999;margin-top:8px;font-weight:300;">Scraped from 99acres.com · Separate pipelines for flats &amp; houses · Merged into unified dataset · Serialised with joblib</p>
<hr class="divider">
""", unsafe_allow_html=True)

# PROBLEM
st.markdown('<div class="section-tag">The problem</div>', unsafe_allow_html=True)
st.markdown('<div class="section-h">Real estate pricing is broken</div>', unsafe_allow_html=True)
st.markdown('<p class="section-body">Listings are inconsistent, prices swing wildly across sectors, and the signals that drive value are buried in unstructured text. The goal was not just prediction — it was to build a system that understands property structure.</p>', unsafe_allow_html=True)
st.markdown("""
<div class="prob-grid">
  <div class="prob-card"><div class="prob-num">01</div><div class="prob-title">Prices vary heavily across sectors</div><div class="prob-body">Premium Gurgaon sectors command 2× the price of peripheral sectors — location encoding was the single biggest accuracy lever.</div></div>
  <div class="prob-card"><div class="prob-num">02</div><div class="prob-title">Listings are deeply inconsistent</div><div class="prob-body">Same property type described ten different ways. Separate cleaning pipelines built for flats and houses before data could be merged.</div></div>
  <div class="prob-card"><div class="prob-num">03</div><div class="prob-title">Important features hidden in text</div><div class="prob-body">Luxury level, servant rooms, study rooms, pooja rooms — all buried in a single "others" field. Extracted with domain logic, not guesswork.</div></div>
  <div class="prob-card"><div class="prob-num">04</div><div class="prob-title">No reliable pricing baseline</div><div class="prob-body">Buyers and sellers negotiate blind. This system gives both sides a data-backed reference — a fair value estimate, not a listing price.</div></div>
</div>
<hr class="divider">
""", unsafe_allow_html=True)

# FEATURE ENGINEERING
st.markdown('<div class="section-tag">Feature engineering</div>', unsafe_allow_html=True)
st.markdown('<div class="section-h">Where the accuracy came from</div>', unsafe_allow_html=True)
st.markdown('<p class="section-body">The model did not win on algorithm choice — XGBoost and Random Forest were within 0.01 R² of each other. The gap came entirely from how the data was structured before training.</p>', unsafe_allow_html=True)
st.markdown("""
<div class="feat-grid">
  <div class="feat-card"><span class="feat-mono">luxury_score</span><div class="feat-title">Composite quality score</div><div class="feat-body">Captures property tier from amenities and finishes. Ordinally encoded — preserves the hierarchy from standard to ultra-luxury.</div></div>
  <div class="feat-card"><span class="feat-mono">area_to_bedroom</span><div class="feat-title">Density indicator</div><div class="feat-body">Area per bedroom ratio. Signals whether a property is spacious or cramped relative to its configuration — a proxy for livability.</div></div>
  <div class="feat-card"><span class="feat-mono">agePossession</span><div class="feat-title">Age in buckets</div><div class="feat-body">Possession age binned into ranges — new, mid-age, mature. Raw numeric age added noise; categorical buckets improved signal.</div></div>
  <div class="feat-card"><span class="feat-mono">target_encoding</span><div class="feat-title">Location impact</div><div class="feat-body">Sector encoded by mean target price. Preserves the pricing signal of location without high-cardinality one-hot explosion.</div></div>
  <div class="feat-card"><span class="feat-mono">others → rooms</span><div class="feat-title">Text field extraction</div><div class="feat-body">Unstructured "others" field split into four binary features: servant room, study room, store room, pooja room.</div></div>
  <div class="feat-card"><span class="feat-mono">cosine_similarity</span><div class="feat-title">Recommendation layer</div><div class="feat-body">Similar properties surfaced alongside predictions — converting a number output into a full decision-support tool for buyers.</div></div>
</div>
<hr class="divider">
""", unsafe_allow_html=True)

# MODEL TABLE
st.markdown('<div class="section-tag">Model selection</div>', unsafe_allow_html=True)
st.markdown('<div class="section-h">Four models evaluated, one deployed</div>', unsafe_allow_html=True)
st.markdown('<p class="section-body">Every model trained on the same engineered feature set and evaluated on held-out data. XGBoost took the top spot on both R² and MAE.</p>', unsafe_allow_html=True)
st.markdown("""
<div class="model-wrap">
<table class="model-table">
  <thead><tr><th>Model</th><th>R² score</th><th>MAE (₹ Cr)</th><th>Notes</th></tr></thead>
  <tbody>
    <tr class="best">
      <td>XGBoost <span class="dep-badge">deployed</span></td>
      <td><div class="bar-wrap">0.90&nbsp;<div class="bar-track"><div class="bar-fill" style="width:90%"></div></div></div></td>
      <td>0.48</td><td style="color:#1D6B4E">Best R² + lowest error</td>
    </tr>
    <tr>
      <td>Random Forest</td>
      <td><div class="bar-wrap">0.89&nbsp;<div class="bar-track"><div class="bar-dim" style="width:89%"></div></div></div></td>
      <td>0.50</td><td style="color:#AAA">Close second</td>
    </tr>
    <tr>
      <td>Gradient Boosting</td>
      <td><div class="bar-wrap">0.88&nbsp;<div class="bar-track"><div class="bar-dim" style="width:88%"></div></div></div></td>
      <td>0.57</td><td style="color:#AAA">Slower convergence</td>
    </tr>
    <tr>
      <td>SVR</td>
      <td><div class="bar-wrap">0.85&nbsp;<div class="bar-track"><div class="bar-dimmer" style="width:85%"></div></div></div></td>
      <td>0.63</td><td style="color:#AAA">Weakest on MAE</td>
    </tr>
  </tbody>
</table>
</div>
<div class="insight">
  <div class="insight-quote">"</div>
  <div class="insight-text"><strong>Accuracy did not come from the model.</strong> It came from how the data was structured and engineered beforehand. XGBoost and Random Forest were within 0.01 R² of each other — the real gap was between raw features and engineered ones, not between algorithms.</div>
</div>
<hr class="divider">
""", unsafe_allow_html=True)

# TECH STACK
st.markdown('<div class="section-tag">Tech stack</div>', unsafe_allow_html=True)
st.markdown("""
<div class="tech-row">
  <span class="tech-pill">Python</span><span class="tech-pill">XGBoost</span>
  <span class="tech-pill">Pandas</span><span class="tech-pill">NumPy</span>
  <span class="tech-pill">Scikit-learn</span><span class="tech-pill">Category Encoders</span>
  <span class="tech-pill">BeautifulSoup</span><span class="tech-pill">joblib</span>
  <span class="tech-pill">Streamlit</span><span class="tech-pill">Streamlit Cloud</span>
</div>
""", unsafe_allow_html=True)

# FOOTER
st.markdown("""
<div class="footer-wrap">
  <div class="footer-name">Faheem Bashir Bhat</div>
  <div class="footer-links">
    <a href="https://realestate-byfaheem.streamlit.app">realestate-byfaheem.streamlit.app</a>
    &nbsp;·&nbsp;
    <a href="https://github.com/faheem-afk">github.com/faheem-afk</a>
  </div>
</div>
""", unsafe_allow_html=True)