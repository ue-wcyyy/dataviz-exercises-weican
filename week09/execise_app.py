import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Happiness vs Corruption", page_icon="🌐", layout="wide")
st.title("🌍 Happiness Score vs Perception of Corruption")
st.markdown("Class Exercise: Diverging Continuous Color Scale Chart")

DATA = Path(__file__).parent.parent / "data" / "world_happiness_2023.csv"
df['Corruption'] = pd.read_csv(DATA)

midpoint_val = df['Corruption'].median()

fig = px.scatter(
    df, 
    x='Corruption', 
    y='Score',
    color='Corruption', 
    color_continuous_scale='RdBu_r', 
    color_continuous_midpoint=midpoint_val,
    hover_name='Country', 
    hover_data={'Region': True, 'Score': ':.2f'},
    title="Happiness Score vs Perception of Corruption",
    template='plotly_white'
)

fig.add_vline(
    x=midpoint_val, 
    line_dash="dash", 
    line_color="gray",
    annotation_text=f"Median Corruption: {midpoint_val:.2f}", 
    annotation_position="top right"
)

fig.update_layout(
    xaxis_title="Perceptions of Corruption (Higher = More Corrupt)",
    yaxis_title="Happiness Score (0-10)",
    coloraxis_colorbar=dict(title="Corruption Level")
)

st.plotly_chart(fig, use_container_width=True)

st.divider()
st.caption("Built with Streamlit + Plotly")
