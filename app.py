import streamlit as st
import pickle
import numpy as np

# Load model bundle
with open("customer_segmentation_model.pkl", "rb") as f:
    bundle = pickle.load(f)

model       = bundle["kmeans"]
scaler      = bundle["scaler"]
segment_map = bundle["segment_map"]

st.title("Customer Segmentation App")
st.write("Enter customer RFM details below:")

# Input fields
recency   = st.number_input("Recency (days since last purchase)", min_value=0.0)
frequency = st.number_input("Frequency (number of purchases)",    min_value=0.0)
monetary  = st.number_input("Monetary (total spend $)",           min_value=0.0)

if st.button("Predict"):
    data = np.array([[recency, frequency, monetary]])

    # Scale
    data_scaled = scaler.transform(data)

    # Predict
    cluster    = model.predict(data_scaled)[0]
    segment    = segment_map[cluster]

    # Distance to each centroid → confidence proxy
    distances  = model.transform(data_scaled)[0]   # shape (n_clusters,)
    closest    = distances[cluster]
    total      = distances.sum()
    confidence = 1 - (closest / total)             # higher = more confident

    if segment == "Active High Value":
        st.success(f"💎 {segment}  ({confidence:.2%} confidence)")
    else:
        st.warning(f"⚠️  {segment}  ({confidence:.2%} confidence)")
