import streamlit as st

from routes import training_data

from utils import create_dataframe

# Convert CSV files into suitable dataframes.
best_train_res = create_dataframe(str(training_data/'best_train_res.csv'), 'Model')
dt_best_params_res = create_dataframe(str(training_data/'dt_best_params_res.csv'), 'Model')
rf_best_params_res = create_dataframe(str(training_data/'rf_best_params_res.csv'), 'Model')
gb_best_params_res = create_dataframe(str(training_data/'gb_best_params_res.csv'), 'Model')

st.title('⚙️ Training Results', text_alignment = 'center')

st.header('🥇 Best Model Parameters', divider = 'blue')

st.subheader('Decision Tree', text_alignment = 'center')
st.dataframe(dt_best_params_res)

st.subheader('Random Forest', text_alignment = 'center')
st.dataframe(rf_best_params_res)

st.subheader('Gradient Boosting', text_alignment = 'center')
st.dataframe(gb_best_params_res)

st.header('💡 Training Results', divider = 'green')

st.dataframe(best_train_res)