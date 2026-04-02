~~~python
import streamlit as st
import pandas as pd
import plotpy.express as px

st.sidebar.title("Navigation")
app_mode=st.sidebar.selectbox("Choose the app",
                              ["A. Data Visualization#, "B. Machine Learning", "C. Recommendations"])
                               if app_mode=="A. Data Visualization":
                                 st.title("Data Visualization Dashboard")
                                 st.markdown("Upload a CSV file to explore your data interactively.")
                               
                                 uploaded_file=st.file_uploader("Choose a CSV file", type="csv")
                                            if uploaded_file is not None:
                                                df=pd.read_csv(uploaded_file)
st.subheader("Raw Data Preview")
st.dataframe(df.head())

st.subheader("Data Statistices")
st.write(df.describe())

st.subheader("Visual Analysis")
columns=df.columns.tolist()
x_axis=st.selectbox("Select X axis", columns)
y_axis=st.selectbox("Select Y axis", columns)

fig=px.scatter(df, x=x_axis, y=y_axis, title=f'{y_axis} vs {x_axis}")
st.plotly_chart(fig)
else:
st.info("Please upload a CSV file to get started.")

                                            else:
                                            st.info("Please upload a CSV file to get started.")


                               elif app_mode=="B. Machine Learning":
                               st.title("ML Model Demo")
                               st.info("Coming Soon: Test the power of AI here.")

                               elif app_mode=="C. Recommendations":
                               st.title("Recommendation Engine")
                               st.info("Coming Soon: Find your next favorite thing.")
