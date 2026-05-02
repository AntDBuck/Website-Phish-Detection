import streamlit as st

from routes import eda_figs

st.title('🔍 EDA', text_alignment = 'center')

st.header('📊 Feature Distrubtions', divider = 'blue')

col1, col2 = st.columns(2)

with col1:
    st.subheader('Barcharts', text_alignment = 'center')
    st.image(str(eda_figs/'eda_barcharts.png'), caption = 'Barcharts showing the distrubtion of the top 10 features with the higest correlation split by status.')

with col2:
    st.subheader('Boxplots', text_alignment = 'center')
    st.image(str(eda_figs/'eda_boxplots.png'), caption = 'Boxplots of the top 10 features with the higest correlation split by status.')

st.header('🔥 Feature Correlations', divider = 'green')

col3, col4 = st.columns(2)

with col3:
    st.subheader('Heatmap', text_alignment = 'center')
    st.image(str(eda_figs/'eda_heatmap.png'), caption = 'Heatmap showing the relationship between each of the top 10 features with the higest correlation and status.')
    

with col4:
    st.subheader('Clusters', text_alignment = 'center')
    st.image(str(eda_figs/'eda_cluster.png'), caption = 'Cluster graph showing a split by status with feature relationship between the ratio of digits used in URL and the number of hyperlinks used.')