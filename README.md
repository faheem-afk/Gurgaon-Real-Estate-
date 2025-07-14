# 🏙️ Gurgaon Real Estate Price Prediction

This project aims to predict property prices in **Gurgaon, India**, using a machine learning pipeline trained on real estate data scraped from **99acres.com**.  
The prediction interface is deployed via **Streamlit**, allowing users to input property features and receive a price range estimate.

---

## 📌 Project Overview

The goal is to build a robust regression model that can predict the selling price of flats and houses based on various features such as **sector**, **area**, **number of rooms**, and **luxury category**.

---

## 🗃️ Dataset

- **Source:** Scraped from [99acres.com](https://99acres.com) using `BeautifulSoup`
- **Location:** Gurgaon city
- **Property Types:** Flats and houses/apartments
- **Files Used:**
  - `Data_Cleaning_flats.ipynb`
  - `Data_cleaning_houses.ipynb`
  - `Final_cleaning.ipynb`
  - `Missing_value_imputation.ipynb`
  - `outlier_detection.ipynb`
  - `univariate_analysis.ipynb`
  - `featureEngineering.ipynb`
  - `Feature_selection.ipynb`
  - `baseline_model.ipynb`

---

## 🔧 Features Used

**Final selected features:**
- `sector`
- `property_type`
- `bedRoom`
- `bathroom`
- `servant room`
- `study room`
- `luxury_category`

🎯 **Target:** `price`

---

## 🧹 Data Preprocessing Steps

1. **Web Scraping:** Scraped multiple pages of listings and stored data.
2. **Cleaning:** Standardized formats separately for flats and houses.
3. **Merging:** Unified cleaned dataframes into one dataset.
4. **Missing Value Imputation:** Used domain rules for imputation.
5. **Outlier Detection:** Removed outliers using univariate analysis.
6. **Feature Engineering:**
   - Split `others` column into:
     - `pooja room`, `servant room`, `store room`, `study room`, etc.
   - Categorized `agePossession` into:
     - `Relatively New`, `New Property`, `Moderately Old`, `Old`, `Under Construction`, `Undefined`
   - Created derived features like `area_to_bedroom`
   - Developed a feature called `luxury score`
7. **Encoding Techniques:**
   - **Ordinal Encoding:** `luxury_category`
   - **Target Encoding:** `sector`, `property_type`, `servant room`, `study room`
   - Tried **One-Hot Encoding + PCA** (experimentally)
8. **Feature Selection:**
   - Recursive Feature Elimination (RFE)
   - Permutation Importance
   - Random Forest, Decision Tree, Linear Regression, Lasso, Gradient Boosting
   - Correlation Analysis
9. **Scaling:**
   - Applied `StandardScaler` on numerical columns

---

## 📈 Modeling Performance

| Model              | R² Score | MAE     | Std Dev |
|--------------------|----------|---------|---------|
| **XGBoost**         | 0.9022   | 0.4851  | 0.0170  |
| Random Forest       | 0.8919   | 0.5034  | 0.0180  |
| Gradient Boosting   | 0.8832   | 0.5707  | 0.0186  |
| Decision Tree       | 0.8059   | 0.6305  | 0.0373  |
| SVR                 | 0.8568   | 0.6381  | 0.0239  |
| MLP Regressor       | 0.8510   | 0.6905  | 0.0220  |
| Extra Trees         | 0.7751   | 0.7250  | 0.0321  |
| AdaBoost            | 0.8170   | 0.7702  | 0.0215  |
| Linear Regression   | 0.8151   | 0.8289  | 0.0186  |
| Ridge Regression    | 0.8151   | 0.8292  | 0.0186  |
| Lasso Regression    | -0.0021  | 1.6760  | 0.0027  |

✅ **Final Model Used:** `XGBoost`

---

## 🎯 Deployment

- **Frontend:** Streamlit App (`app.py`)
- **Backend:** Trained pipeline serialized with `joblib`
- **Hosted on:** [realestate-byfaheem.streamlit.app](https://realestate-byfaheem.streamlit.app)

---

## 🖥️ User Input Interface

The web app allows users to enter:
- Property Type
- Sector
- Number of Bedrooms / Bathrooms
- Area (in sqft)
- Whether a Servant Room / Study Room exists
- Luxury Category

🔮 **Output:** The predicted price range (in Crores, INR)

---

## 📦 Requirements

🧰 Python 3.10 and the following libraries:

```txt
joblib==1.5.0
numpy==1.23.5
pandas==1.5.3
streamlit==1.45.1
scikit-learn==1.6.1
category_encoders==2.8.1
xgboost==3.0.2