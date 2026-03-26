import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Universal Data Dashboard", layout="wide")

st.title("📊 Universal Data Visualization Dashboard")

# Upload file
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("📋 Dataset Preview")
    st.dataframe(df.head())

    st.subheader("📊 Dataset Info")
    st.write("Shape:", df.shape)
    st.write("Columns:", list(df.columns))

    # Select columns
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()

    if len(numeric_cols) == 0:
        st.warning("No numeric columns found for visualization")
    else:
        st.sidebar.header("⚙️ Visualization Settings")

        chart_type = st.sidebar.selectbox(
            "Select Chart Type",
            ["Histogram", "Bar Chart", "Box Plot", "Scatter Plot", "Heatmap"]
        )

        col1 = st.sidebar.selectbox("Select Column 1", numeric_cols)

        if chart_type == "Scatter Plot":
            col2 = st.sidebar.selectbox("Select Column 2", numeric_cols)

        # ---------------- Charts ---------------- #

        st.subheader(f"📈 {chart_type}")

        fig, ax = plt.subplots()

        if chart_type == "Histogram":
            ax.hist(df[col1], bins=10, edgecolor="black")

        elif chart_type == "Bar Chart":
            df[col1].value_counts().plot(kind="bar", ax=ax)

        elif chart_type == "Box Plot":
            sns.boxplot(y=df[col1], ax=ax)

        elif chart_type == "Scatter Plot":
            ax.scatter(df[col1], df[col2])

        elif chart_type == "Heatmap":
            sns.heatmap(df[numeric_cols].corr(), annot=True, ax=ax)

        st.pyplot(fig)

        # ---------------- Summary Stats ---------------- #
        st.subheader("📌 Summary Statistics")
        st.write(df.describe())

else:
    st.info("👆 Upload a CSV file to start visualization")