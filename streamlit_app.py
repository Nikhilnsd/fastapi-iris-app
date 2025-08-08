import streamlit as st
import pandas as pd
import plotly.express as px
import requests

# Shared color map
color_map = {
    'setosa': 'lightblue',
    'versicolor': 'lightgreen',
    'virginica': 'lightcoral'
}

# Load iris dataset
iris_df = px.data.iris()

# Prepare treemap data (percentage only)
species_counts = iris_df['species'].value_counts(normalize=True).reset_index()
species_counts.columns = ['species', 'percentage']
species_counts['percentage'] = round(species_counts['percentage'] * 100, 1)
species_counts['label'] = species_counts['species'] + '<br>' + \
                          'Percent: ' + species_counts['percentage'].astype(str) + '%'

# 🌸 App Title
st.set_page_config(layout="wide")
st.title("🌸 Iris Flower Prediction App")
st.markdown("Use the sliders to input flower measurements. The model will predict the Iris species.")

# 🌿 Sliders with scrollable sidebar
with st.sidebar:
    st.header("📏 Flower Measurements")
    sepal_length = st.slider("Sepal Length (cm)", 0.0, 7.0, 5.1, step=0.1)
    sepal_width = st.slider("Sepal Width (cm)", 0.0, 3.0, 3.0, step=0.1)
    petal_length = st.slider("Petal Length (cm)", 0.0, 7.0, 1.4, step=0.1)
    petal_width = st.slider("Petal Width (cm)", 0.0, 3.0, 0.2, step=0.1)

# Variables to store prediction
predicted_species = None
highlight_df = pd.DataFrame()

# 🔍 Prediction Button
if st.button("🔍 Predict"):
    input_data = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }

    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=input_data)
        if response.status_code == 200:
            predicted_species = response.json().get("species", "Unknown")
            st.success(f"🌼 **Predicted Iris Species:** {predicted_species}")

            # Prepare highlighted point
            highlight_df = pd.DataFrame([input_data])
            highlight_df["species"] = predicted_species
        else:
            st.error("❌ Failed to get prediction from API.")
    except Exception as e:
        st.error(f"🚫 Error contacting prediction API: {e}")

# 🧬 Treemap: Percentage only
st.markdown("### 🧬 Iris Species Distribution (Treemap) - Percentage Only")
treemap = px.treemap(
    species_counts,
    path=['species'],
    values='percentage',
    color='species',
    color_discrete_map=color_map,
    hover_data={'percentage': True},
    custom_data=['label']
)
treemap.update_traces(texttemplate="%{customdata[0]}")
st.plotly_chart(treemap, use_container_width=True)

# 📊 Full Scatter Plot
st.markdown("### 📊 Petal Length vs Petal Width - All Flowers")
scatter_all = px.scatter(
    iris_df,
    x="petal_length",
    y="petal_width",
    color="species",
    symbol="species",
    color_discrete_map=color_map,
    labels={"petal_length": "Petal Length (cm)", "petal_width": "Petal Width (cm)"}
)
st.plotly_chart(scatter_all, use_container_width=True)

# 📍 Predicted Flower Highlighted
if not highlight_df.empty:
    st.markdown("### 📍 Where is Your Predicted Flower?")
    highlight_plot = px.scatter(
        iris_df,
        x="petal_length",
        y="petal_width",
        color="species",
        symbol="species",
        color_discrete_map=color_map,
        labels={"petal_length": "Petal Length (cm)", "petal_width": "Petal Width (cm)"}
    )
    highlight_plot.add_scatter(
        x=highlight_df["petal_length"],
        y=highlight_df["petal_width"],
        mode='markers',
        marker=dict(color='red', size=14, symbol='star'),
        name="Predicted Flower"
    )
    st.plotly_chart(highlight_plot, use_container_width=True)
