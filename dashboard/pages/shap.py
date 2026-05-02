import streamlit as st

from routes import shap_figs

st.title('🧠 SHAP Results', text_alignment = 'center')

st.header('🌐 Global Explainations - Beeswarm Plots', divider = 'blue')

col1, col2 = st.columns(2)

with col1:
        st.subheader('Balanced Decision Tree', text_alignment = 'center')
        st.image(str(shap_figs/'bal_dt_beeswarm.png'), caption = 'Beeswarm SHAP graph of balanced decision tree predictions.')

        st.subheader('Balanced Random Forest', text_alignment = 'center')
        st.image(str(shap_figs/'bal_rf_beeswarm.png'), caption = 'Beeswarm SHAP graph of balanced random forest predictions.')

        st.subheader('Balanced Gradient Boosting', text_alignment = 'center')
        st.image(str(shap_figs/'bal_gb_beeswarm.png'), caption = 'Beeswarm SHAP graph of balanced gradient boosting predictions.')

with col2:
        st.subheader('Imbalanced Decision Tree', text_alignment = 'center')
        st.image(str(shap_figs/'imbal_dt_beeswarm.png'), caption = 'Beeswarm SHAP graph of imbalanced decision tree predictions.')

        st.subheader('Imbalanced Random Forest', text_alignment = 'center')
        st.image(str(shap_figs/'imbal_rf_beeswarm.png'), caption = 'Beeswarm SHAP graph of imbalanced random forest predictions.')

        st.subheader('Imbalanced Gradient Boosting', text_alignment = 'center')
        st.image(str(shap_figs/'imbal_gb_beeswarm.png'), caption = 'Beeswarm SHAP graph of imbalanced gradient boosting predictions.')

st.header('📍 Local Explainations - Waterfall Plots', divider = 'green')

st.subheader('Balanced Decision Tree', text_alignment = 'center')

col3, col4 = st.columns(2)

with col3:
        st.markdown('Legitimate Website Record', text_alignment = 'center')
        st.image(str(shap_figs/'bal_dt_legit_waterfall.png'), caption = 'Waterfall SHAP graph of balanced decision tree prediction on a legitimate website record.')

with col4:
        st.markdown('Phishing Website Record', text_alignment = 'center')
        st.image(str(shap_figs/'bal_dt_phish_waterfall.png'), caption = 'Waterfall SHAP graph of balanced decision tree prediction on a phishing website record.')

st.subheader('Imbalanced Decision Tree', text_alignment = 'center')

col5, col6 = st.columns(2)

with col5:
        st.markdown('Legitimate Website Record', text_alignment = 'center')
        st.image(str(shap_figs/'imbal_dt_legit_waterfall.png'), caption = 'Waterfall SHAP graph of imbalanced decision tree prediction on a legitimate website record.')

with col6:
        st.markdown('Phishing Website Record', text_alignment = 'center')
        st.image(str(shap_figs/'imbal_dt_phish_waterfall.png'), caption = 'Waterfall SHAP graph of imbalanced decision tree prediction on a phishing website record.')

st.subheader('Balanced Random Forest', text_alignment = 'center')

col7, col8 = st.columns(2)

with col7:
        st.markdown('Legitimate Website Record', text_alignment = 'center')
        st.image(str(shap_figs/'bal_rf_legit_waterfall.png'), caption = 'Waterfall SHAP graph of balanced random forest prediction on a legitimate website record.')

with col8:
        st.markdown('Phishing Website Record', text_alignment = 'center')
        st.image(str(shap_figs/'bal_rf_phish_waterfall.png'), caption = 'Waterfall SHAP graph of balanced random forest prediction on a phishing website record.')

st.subheader('Imbalanced Random Forest', text_alignment = 'center')

col9, col10 = st.columns(2)

with col9:
        st.markdown('Legitimate Website Record', text_alignment = 'center')
        st.image(str(shap_figs/'imbal_rf_legit_waterfall.png'), caption = 'Waterfall SHAP graph of imbalanced random forest prediction on a legitimate website record.')

with col10:
        st.markdown('Phishing Website Record', text_alignment = 'center')
        st.image(str(shap_figs/'imbal_rf_phish_waterfall.png'), caption = 'Waterfall SHAP graph of imbalanced random forest prediction on a phishing website record.')

st.subheader('Balanced Gradient Boosting', text_alignment = 'center')

col11, col12 = st.columns(2)

with col11:
        st.markdown('Legitimate Website Record', text_alignment = 'center')
        st.image(str(shap_figs/'bal_gb_legit_waterfall.png'), caption = 'Waterfall SHAP graph of balanced gradient boosting prediction on a legitimate website record.')

with col12:
        st.markdown('Phishing Website Record', text_alignment = 'center')
        st.image(str(shap_figs/'bal_gb_phish_waterfall.png'), caption = 'Waterfall SHAP graph of balanced gradient boosting prediction on a phishing website record.')

st.subheader('Imbalanced Gradient Boosting', text_alignment = 'center')

col13, col14 = st.columns(2)

with col13:
        st.markdown('Legitimate Website Record', text_alignment = 'center')
        st.image(str(shap_figs/'imbal_gb_legit_waterfall.png'), caption = 'Waterfall SHAP graph of imbalanced gradient boosting prediction on a legitimate website record.')

with col14:
        st.markdown('Phishing Website Record', text_alignment = 'center')
        st.image(str(shap_figs/'imbal_gb_phish_waterfall.png'), caption = 'Waterfall SHAP graph of imbalanced gradient boosting prediction on a phishing website record.')