# 🎯 Customer Segmentation ML Project
An end-to-end Machine Learning project to segment customers
using RFM Analysis and K-Means Clustering.

## 🚀 Live Demo
- 🎯 Streamlit: https://customer-segmentation-prediction-mythili.streamlit.app/
- 🤗 HuggingFace: https://huggingface.co/spaces/Mythili-Pandiyarajan/customer-segmentation

## 🔍 Project Overview
This project uses RFM (Recency, Frequency, Monetary) analysis
to group customers into meaningful segments using K-Means Clustering.

**Segments Identified:**
* 💎 Active High Value — recent, frequent, high spenders
* ⚠️ Inactive Low Value — lapsed, infrequent, low spenders

## 📁 Project Structure
| File | Description |
|------|-------------|
| `customer_segmentation.ipynb` | ML notebook with EDA and model training |
| `app.py` | Streamlit web application |
| `customer_segmentation_model.pkl` | Trained KMeans model + scaler |
| `requirements.txt` | Required libraries |

## 🛠️ Libraries Used
* Python
* Pandas, NumPy
* Scikit-learn
* Streamlit
* Matplotlib, Seaborn

## 🚀 How to Run Locally
```bash
git clone https://github.com/Mythili-Pandiyarajan/customer-segmentation.git
cd customer-segmentation
pip install -r requirements.txt
streamlit run app.py
```

## 📊 Model Details
| Parameter | Value |
|-----------|-------|
| Algorithm | K-Means Clustering |
| Number of Clusters | 2 |
| Features Used | Recency, Frequency, Monetary |
| Preprocessing | StandardScaler |

## 📌 Dataset
Dataset sourced from Kaggle — Online Retail / Customer Transaction Data

## 👩‍💻 Author
Mythili Pandiyarajan __[GitHub Profile](https://github.com/Mythili-Pandiyarajan)__
