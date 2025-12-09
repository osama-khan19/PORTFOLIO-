import streamlit as st
from PIL import Image, ImageDraw
import base64
import io
import numpy as np

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(
    page_title="Osama Khan | Portfolio",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------------------
# GLOBAL DARK THEME CSS (WORKS 100%)
# ---------------------------
st.markdown("""
<style>
/* Makes EVERYTHING black */
html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"], .main {
    background-color: #000000 !important;
    color: #ffffff !important;
}

/* Text colors */
h1, h2, h3, h4, h5, h6, p, div {
    color: #e3e3e3 !important;
}

/* Neon title */
.neon {
    color: #00eaff !important;
    text-shadow: 0px 0px 12px #00eaff;
    font-weight: bold;
}

/* Section box */
.section {
    padding: 40px 10px;
    border-bottom: 1px solid #111;
}

/* Project card */
.project-box {
    padding: 20px;
    background: #0d0d0d;
    border-radius: 12px;
    margin-bottom: 20px;
    box-shadow: 0 0 15px rgba(0,255,255,0.15);
}

/* Button glow */
.btn-glow {
    background: #00eaff;
    color: black !important;
    padding: 12px 26px;
    border-radius: 10px;
    font-weight: bold;
    text-decoration: none;
    box-shadow: 0 0 18px #00eaff;
}
.btn-glow:hover {
    box-shadow: 0 0 28px #00eaff;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# IMAGE LOAD + PERFECT CIRCLE FIX
# ---------------------------
img_path = "D:\\Downloads\\osama_profile.jpg"  # SAME NAME YOU UPLOADED EARLIER
img = Image.open(img_path)

# ---- PERFECT CIRCLE FUNCTION (NO STRETCH) ----
def make_circle(image):
    image = image.convert("RGBA")
    size = min(image.size)
    image = image.resize((size, size))  # ensures perfect square → perfect circle

    mask = Image.new('L', (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)

    circle_img = image.copy()
    circle_img.putalpha(mask)
    return circle_img

circle_img = make_circle(img)

# Convert to base64
buffered = io.BytesIO()
circle_img.save(buffered, format="PNG")
img_b64 = base64.b64encode(buffered.getvalue()).decode()

# -----------------------------------------------------------
# HEADER
# -----------------------------------------------------------
st.markdown(f"""
<div style="text-align:center; padding-top:20px;">
    <img src="data:image/png;base64,{img_b64}" width="170" style="border-radius:50%; box-shadow:0 0 18px #00eaff;">
    <h1 class="neon">OSAMA KHAN</h1>
    <h3>Data Scientist | ML Engineer | Data Analyst</h3>
    <br>
    <a href="#contact" class="btn-glow">Hire Me</a>
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------
# SKILLS
# -----------------------------------------------------------
st.markdown("<div class='section'><h2 class='neon'>⚡ Skills</h2>", unsafe_allow_html=True)

skills = [
    "Machine Learning", "Deep Learning", "Python",
    "NLP", "Streamlit", "Excel", "MySQL",
    "Pandas", "NumPy", "Seaborn", "Matplotlib",
    "Time Series", "Web Scraping","PowerBI"
]

cols = st.columns(3)
idx = 0
for col in cols:
    with col:
        for _ in range(5):
            if idx < len(skills):
                st.markdown(f"✔ **{skills[idx]}**")
                idx += 1

st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------------------------------------
# PROJECTS
# -----------------------------------------------------------
st.markdown("<div class='section'><h2 class='neon'>📚 Projects</h2>", unsafe_allow_html=True)

projects = {
    "Heart Disease Prediction (Logistic Regression – 83% Accuracy)": 
    "• Built ML model\n• Feature scaling & analysis\n• Performance evaluation",

    "Data Cleaning & Preprocessing (Raw → Clean Dataset)": 
    "• Removed missing values\n• Outlier fixing\n• Encoding & normalization",

    "Torrent Power Price Forecasting (Time Series – Prophet)": 
    "• Trend + Seasonality\n• Forecast graph\n• Insights for energy use",

    "Hand Sign Recognition A–Z (Deep Learning – CNN)": 
    "• Trained CNN model\n• Augmentation\n• Real-time webcam predictions",
}

for title, desc in projects.items():
    st.markdown(f"""
        <div class="project-box">
            <h3 class='neon'>{title}</h3>
            <pre style="color:white;">{desc}</pre>
        </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------------------------------------
# CONTACT
# -----------------------------------------------------------
st.markdown("<div id='contact' class='section'><h2 class='neon'>📬 Contact</h2>", unsafe_allow_html=True)

st.markdown("""
**Email:** osamkhan7977@gmail.com  
**LinkedIn:** www.linkedin.com/in/osama-khan77  
""")

st.markdown("</div>", unsafe_allow_html=True)
