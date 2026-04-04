import streamlit as st
import pandas as pd
import plotly.express as px

st.sidebar.title("Navigation")
app_mode=st.sidebar.selectbox("Choose the app",
                              ["A. Data Visualization", "B. Machine Learning", "C. Recommendations"])
if app_mode=="A. Data Visualization":
  st.title("Data Visualization Dashboard")
  st.markdown("Upload a CSV file to explore your data interactively.")
                               
  uploaded_file=st.file_uploader("Choose a CSV file", type="csv")
  if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.subheader("Raw Data Preview")
    st.dataframe(df.head())
    st.subheader("Data Statistics")
    st.write(df.describe())
    st.subheader("Visual Analysis")
    columns=df.columns.tolist()
    x_axis=st.selectbox("Select X axis", columns)
    y_axis=st.selectbox("Select Y axis", columns)
    fig=px.scatter(df, x=x_axis, y=y_axis, title=f'{x_axis} vs {y_axis}')
    st.plotly_chart(fig)
  else:
    st.info("Please upload a CSV file to get started.")


elif app_mode=="B. Machine Learnining":
  st.title("ML Model Demo")
  st.markdown("Predict the type of flower based on its measurements.")
  from sklearn.datasets import load_iris
  from sklearn.ensemble import RandomForestClassifier

  iris=load_iris()
  X=iris.data
  Y=iris.target
  model=RandomForestClassifier()
  model.fit(X, Y)

  st.sidebar.header("Input Prameters")
  def user_input_features():
    sepal_length=st.sidebar.slider("Sepal length", 4.3, 7.9, 5.4)
    sepal_width=st.sidebar.slider("Sepal width", 2.0, 4.4, 3.4)
    petal_length=st.sidebar.slider("Petal length", 1.0, 6.9, 1.3)
    petal_width=st.sidebar.slider("Petal width", 0.1, 2.5, 0.2)
    data=[[sepal_length, sepal_width, petal_length, petal_width]]
    return data
                                
  input_df=user_input_features()

  prediction=model.predict(input_df)
  prediction_proba=model.predict_proba(input_df)

  st.subheader("Prediction")
  st.write(iris.target_names[prediction][0])
  st.subheader("Prediction Probability")
  st.write(prediction_proba)

elif app_mode=="C. Recommendations":
  st.title("Smart Movie Recommender")
  st.markdown("Find the best movies based on your favorite genre and rating.")
  data={
    "Title":["Inception", "Interstellar", "The Matrix", "Toy Story", "Coco", "The Lion King", "The Godfather", "Pulp Fiction"],
    "Genre":["Sci-Fi", "Sci-Fi", "Sci-Fi", "Animation", "Animation", "Animation", "Crime", "Crime"],
    "Rating":[8.8, 8.6, 8.7, 8.3, 8.4, 8.5, 9.2, 8.9]
  }
  df_movies=pd.DataFrame(data)

  st.sidebar.header("Filter Options")
  selected_genre=st.sidebar.multiselect("Select Genre", df_movies["Genre"].unique(), default=df_movies["Genre"].unique())
  min_rating=st.sidebar.slider("Minimum Rating", 0.0, 10.0, 8.5)

  filtered_df=df_movies[(df_movies["Genre"].isin(selected_genre))&(df_movies["Rating"]>=min_rating)]

  st.subheader(f"Recommended Movies({len(filtered_df)})")
  if not filtered_df.empty:
    st.table(filtered_df.sort_values(by="Rating", ascending=False))
    st.success("Found the perfect matches for you!")
  else:
    st.warning("No movies found. Try adjusting the filters.")


