~~~python
import streamlit as st

# Sidebar for navigation
st.sidebar.title("Navigation")
app_mode=st.sidebar.selectbox("Choose the app",
                              ["A. Data Visualization#, "B. Machine Learning", "C. Recommendations"])
                               if app_mode=="A. Data Visualization":
                               st.title("Data Visualization Dashboard")
                               st.info("Coming Soon: Upload your CSV to see the magic!")

                               elif app_mode=="B. Machine Learning":
                               st.title("ML Model Demo")
                               st.info("Coming Soon: Test the power of AI here.")

                               elif app_mode=="C. Recommendations":
                               st.title("Recommendation Engine")
                               st.info("Coming Soon: Find your next favorite thing.")
