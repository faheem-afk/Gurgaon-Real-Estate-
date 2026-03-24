<h1 align="center">🏙️ Gurgaon Real Estate Intelligence System</h1>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?size=22&duration=3000&color=36BCF7&center=true&vCenter=true&width=750&lines=Predicting+Property+Prices+with+Real+Data;From+Web+Scraping+to+Live+Deployment;Built+for+Real-World+Decision+Making" />
</p>

<p align="center">
  <a href="https://realestate-byfaheem.streamlit.app">
    <img src="https://img.shields.io/badge/Live-Demo-brightgreen?style=for-the-badge&logo=streamlit" />
  </a>
  <img src="https://img.shields.io/badge/Model-XGBoost-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/R²-0.90-success?style=for-the-badge" />
</p>

---

## 📌 Overview

Most real estate platforms show listings.

This system tries to answer a harder question:

👉 *What should this property actually be worth?*

Built using real-world data from Gurgaon, this project takes raw listings and turns them into a **decision-ready pricing system**, deployed as an interactive application.

---

## 🧠 The Problem

Real estate pricing is messy:

- Prices vary heavily across sectors  
- Listings are inconsistent  
- Important features are hidden in text  
- No clear baseline for valuation  

The goal wasn’t just prediction.

👉 It was to build a system that **understands property structure and pricing patterns**

---

## ⚙️ What This System Does

- Predicts property price based on structured inputs  
- Captures hidden signals like **luxury level & property composition**  
- Transforms messy listing data into **clean, usable features**  
- Provides a **real-time interactive interface** for users  

---

## 🌐 Live Application

👉 https://realestate-byfaheem.streamlit.app

---

## 🏗️ End-to-End Pipeline

Web Scraping → Data Cleaning → Feature Engineering → Modeling → Deployment

---

## 🗃️ Data Pipeline

- Scraped data from **99acres.com** using BeautifulSoup  
- Separate cleaning pipelines for flats & houses  
- Merged into a unified dataset  
- Applied structured preprocessing workflows  

---

## 🧹 Data Engineering (Where Most Work Happened)

- Handled missing values using domain logic  
- Removed outliers via statistical analysis  
- Standardized inconsistent formats  
- Extracted structured features from unstructured text  

👉 Example:

`others` → split into:
- servant room  
- study room  
- store room  
- pooja room  

---

## 🧠 Feature Engineering

Created features that actually matter:

- `luxury score` → captures property quality  
- `area_to_bedroom` → density indicator  
- `agePossession` → categorized into meaningful buckets  

Encoding strategies:
- Target Encoding → location & categorical impact  
- Ordinal Encoding → luxury category  
- Experimental PCA + One-Hot  

---

## 📊 Model Performance

| Model            | R² Score | MAE   |
|------------------|----------|-------|
| **XGBoost**       | **0.90** | 0.48  |
| Random Forest     | 0.89     | 0.50  |
| Gradient Boosting | 0.88     | 0.57  |
| SVR               | 0.85     | 0.63  |

👉 Final model: **XGBoost**

---

## ⚡ Key Insight

Accuracy didn’t come from the model.

It came from:

👉 **how the data was structured and engineered**

---

## 🖥️ User Experience

Users can input:

- Property type  
- Sector  
- Bedrooms / Bathrooms  
- Area (sqft)  
- Amenities (servant room, study room)  
- Luxury category  

🔮 Output:
- Predicted price range (INR Crores)

---

## 🚀 Deployment

- **Frontend:** Streamlit  
- **Model:** Serialized pipeline (`joblib`)  
- **Hosting:** Streamlit Cloud  

---

## 🛠️ Tech Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,sklearn,streamlit" />
</p>

<p align="center">
  Pandas • NumPy • XGBoost • Category Encoders
</p>

---

## 💡 What I Learned

- Data cleaning > modeling  
- Feature engineering drives performance  
- Real-world data is noisy, not structured  
- End-to-end systems matter more than isolated models  

---

## 🔮 Future Improvements

- Integrate listing images (computer vision)  
- Ensemble / stacking models  
- Better geo-spatial features  
- Time-based pricing trends  

---

## 📫 Connect

- LinkedIn: https://www.linkedin.com/in/faheemb  
- Email: adahm7114@gmail.com  

---

<p align="center">
  ⭐ If you found this useful, consider starring the repo!
</p>


⸻
