import streamlit as st

from routes import eval_figs, test_data

from utils import create_dataframe, format_cr

# Convert CSV files into suitable dataframes.
test_res_df = create_dataframe(str(test_data/'test_res_df.csv'), 'models')

test_res_bal_dt = create_dataframe(str(test_data/'test_res_bal_dt.csv'), '')
test_res_bal_rf = create_dataframe(str(test_data/'test_res_bal_rf.csv'), '')
test_res_bal_gb = create_dataframe(str(test_data/'test_res_bal_gb.csv'), '')

test_res_imbal_dt = create_dataframe(str(test_data/'test_res_imbal_dt.csv'), '')
test_res_imbal_rf = create_dataframe(str(test_data/'test_res_imbal_rf.csv'), '')
test_res_imbal_gb = create_dataframe(str(test_data/'test_res_imbal_gb.csv'), '')

st.title('🎯 Test Results', text_alignment = 'center')

st.header('🔬 Comprehensive Test Results', divider = 'blue')

st.dataframe(test_res_df)

# Format classification reports to show class splits.
st.header('📋 Class Split Results', divider = 'green')

col1, col2 = st.columns(2)

with col1:
    st.subheader('Balanced Decision Tree', text_alignment = 'center')
    st.dataframe(format_cr(test_res_bal_dt))

    st.subheader('Balanced Random Forest', text_alignment = 'center')
    st.dataframe(format_cr(test_res_bal_rf))

    st.subheader('Balanced Gradient Boosting', text_alignment = 'center')
    st.dataframe(format_cr(test_res_bal_gb))

with col2:
    st.subheader('Imbalanced Decision Tree', text_alignment = 'center')
    st.dataframe(format_cr(test_res_imbal_dt))

    st.subheader('Imbalanced Random Forest', text_alignment = 'center')
    st.dataframe(format_cr(test_res_imbal_rf))

    st.subheader('Imbalanced Gradient Boosting', text_alignment = 'center')
    st.dataframe(format_cr(test_res_imbal_gb))

st.header('📊 Graph Test Results', divider = 'red')

col3, col4 = st.columns(2)

with col3:
    st.image(str(eval_figs/'test_res_heatmap.png'), caption = 'Confusion matrices of best model predictions.')

with col4:
    st.image(str(eval_figs/'test_res_roc.png'),caption = 'ROC AUC graph of best models.')
