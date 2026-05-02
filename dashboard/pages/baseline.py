import streamlit as st

from routes import baseline_data, eval_figs

from utils import create_dataframe, format_cr

# Convert CSV files into suitable dataframes.
bal_baseline_df = create_dataframe(str(baseline_data/'bal_baseline_df.csv'), 'models')
imbal_baseline_df = create_dataframe(str(baseline_data/'imbal_baseline_df.csv'), 'models')

bal_baseline_cr_dt = create_dataframe(str(baseline_data/'bal_baseline_cr_dt.csv'), '')
bal_baseline_cr_rf = create_dataframe(str(baseline_data/'bal_baseline_cr_rf.csv'), '')
bal_baseline_cr_gb = create_dataframe(str(baseline_data/'bal_baseline_cr_gb.csv'), '')

imbal_baseline_cr_dt = create_dataframe(str(baseline_data/'imbal_baseline_cr_dt.csv'), '')
imbal_baseline_cr_rf = create_dataframe(str(baseline_data/'imbal_baseline_cr_rf.csv'), '')
imbal_baseline_cr_gb = create_dataframe(str(baseline_data/'imbal_baseline_cr_gb.csv'), '')

st.title('📈 Baseline Results', text_alignment = 'center')

st.header('🔬 Comprehensive Test Results', divider = 'blue')

col1, col2 = st.columns(2)

with col1:
    st.subheader('Balanced Models', text_alignment = 'center')
    st.dataframe(bal_baseline_df)

with col2:
    st.subheader('Imbalanced Models', text_alignment = 'center')
    st.dataframe(imbal_baseline_df)

# Format classification reports to show class splits.
st.header('📋 Class Split Results', divider = 'green')

col3, col4 = st.columns(2)

with col3:
    st.subheader('Balanced Decision Tree', text_alignment = 'center')
    st.dataframe(format_cr(bal_baseline_cr_dt))

    st.subheader('Balanced Random Forest', text_alignment = 'center')
    st.dataframe(format_cr(bal_baseline_cr_rf))

    st.subheader('Balanced Gradient Boosting', text_alignment = 'center')
    st.dataframe(format_cr(bal_baseline_cr_gb))

with col4:
    st.subheader('Imbalanced Decision Tree', text_alignment = 'center')
    st.dataframe(format_cr(imbal_baseline_cr_dt))

    st.subheader('Imbalanced Random Forest', text_alignment = 'center')
    st.dataframe(format_cr(imbal_baseline_cr_rf))

    st.subheader('Imbalanced Gradient Boosting', text_alignment = 'center')
    st.dataframe(format_cr(imbal_baseline_cr_gb))

st.header('📊 Graphs', divider = 'red')

st.subheader('Confusion Matrices', text_alignment = 'center')

col5, col6 = st.columns(2)

with col5:
    st.image(str(eval_figs/'bal_baseline_heatmap.png'), caption = 'Confusion matrices of balanced baseline model predictions.')

with col6:
    st.image(str(eval_figs/'imbal_baseline_heatmap.png'), caption = 'Confusion matrices of imbalanced baseline model predictions.')

st.subheader('ROC AUC Graphs', text_alignment = 'center')

col7, col8 = st.columns(2)

with col7:
    st.image(str(eval_figs/'bal_baseline_roc.png'), caption = 'ROC AUC graph of balanced baseline models.')

with col8:
    st.image(str(eval_figs/'imbal_baseline_roc.png'), caption = 'ROC AUC graph of imbalanced baseline models.')