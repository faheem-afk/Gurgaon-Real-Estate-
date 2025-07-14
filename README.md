Gurgaon Real Estate Price Prediction

This project aims to predict property prices in Gurgaon, India, using a machine learning pipeline trained on real estate data scraped from 99acres. The prediction interface is deployed via Streamlit, allowing users to input property features and receive a price range estimate.

📌 Project Overview

The goal is to build a robust regression model that can predict the selling price of flats and houses based on various features such as sector, area, number of rooms, and luxury category.

🗃️ Dataset
	•	Source: Scraped from 99acres.com using BeautifulSoup.
	•	Location: Gurgaon city
	•	Types: Includes both flats and houses/apartments.
	•	Files Used:
	•	Data_Cleaning_flats.ipynb
	•	Data_cleaning_houses.ipynb
	•	Final_cleaning.ipynb
	•	Missing_value_imputation.ipynb
	•	outlier_detection.ipynb
	•	univariate_analysis.ipynb
	•	featureEngineering.ipynb
	•	Feature_selection.ipynb
	•	baseline_model.ipynb

🔧 Features Used

Final selected features:
	•	sector
	•	property_type
	•	bedRoom
	•	bathroom
	•	servant room
	•	study room
	•	luxury_category
	•	Target: price

🧹 Data Preprocessing Steps
	1.	Web Scraping: Properties data was scraped from multiple pages and stored.
	2.	Cleaning: Performed separately for flats and houses, including parsing strings, standardizing formats.
	3.	Merging: Cleaned dataframes were merged into a single unified dataset.
	4.	Missing Value Imputation: Used custom rules and domain knowledge.
	5.	Outlier Detection: Identified and removed outliers using univariate analysis.
	6.	Feature Engineering:
	•	Split additional room information into: others, pooja room, servant room, store room, study room
	•	Categorized agePossession into: Relatively New, New Property, Moderately Old, Undefined, Old 
    •	Extracted details from 'features' column, and developed a feature called 'luxury score'. 
    Property, Under Construction
	•	Created derived features like area_to_bedroom for outlier_detection.
	7.	Encoding Techniques:
	•	Ordinal Encoding: luxury_category
	•	Target Encoding: sector, property_type, servant room, study room
	•	Tried One-Hot Encoding + PCA (experimentally)
	8.	Feature Selection Techniques:
	•	Feature Recursive Elimination (RFE)
	•	Permutation Importance
	•	Random Forest, Decision Tree, Linear Regression, Lasso, Gradient Boosting
	•	Correlation Analysis
	9.	Scaling: Applied StandardScaler on numerical features

📈 Modeling

Model	R² Score	MAE	Std Dev
XGBoost	0.9022	0.4851	0.0170
Random Forest	0.8919	0.5034	0.0180
Gradient Boosting	0.8832	0.5707	0.0186
Decision Tree	0.8059	0.6305	0.0373
SVR	0.8568	0.6381	0.0239
MLP Regressor	0.8510	0.6905	0.0220
Extra Trees	0.7751	0.7250	0.0321
AdaBoost	0.8170	0.7702	0.0215
Linear Regression	0.8151	0.8289	0.0186
Ridge	0.8151	0.8292	0.0186
Lasso	-0.0021	1.6760	0.0027

	•	✅ Final Model Used: XGBoost

🎯 Deployment
	•	Frontend: Streamlit App (app.py)
	•	Backend: Trained pipeline serialized via joblib and loaded for predictions
	•	App hosted on: realestate-byfaheem.streamlit.app

🖥️ User Input Interface

Users can enter:
	•	Property Type
	•	Sector
	•	Number of Bedrooms/Bathrooms
	•	Area in sqft
	•	Presence of Servant/Study Room
	•	Luxury Category

The model predicts a price range in Crores (INR).

📦 Requirements

Python 3.10 and the following libraries:

joblib==1.5.0
numpy==1.23.5
pandas==1.5.3
streamlit==1.45.1
scikit-learn==1.6.1
category_encoders==2.8.1
xgboost==3.0.2

🚀 How to Run

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py

🔍 Future Work
	•	Incorporate image data from listings
	•	Add more advanced model stacking
	•	Use LightGBM or further tune XGBoost
	•	Enable filtering by date or location clusters

🧑‍💻 Author: Faheem Bhat

This project is being developed as part of a capstone portfolio on data science and real estate modeling.