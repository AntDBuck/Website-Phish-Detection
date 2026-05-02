import streamlit as st

st.title('🏠 Home', text_alignment = 'center')

st.header('🧭 Guide', divider = 'rainbow')

st.markdown('This dashboard has been created to show the various results of my research at each stage of the pipeline. Moreover, each model\'s optimised parameters have been shared for ease of replication and the duplication of results.')

st.markdown('Below are brief explainations of each page:')

st.markdown('🔍 :green[EDA:] the exporatory data analysis of the top ten features based on status correlation (legit or phishing). The page includes barcharts, boxplots, a cluster graph, and a heatmap.')

st.markdown('📈 :green[Baseline Results:] the test results of the baseline classification models (default parameters). The page shows various evaluation tables, confusion matrices, and ROC AUC graphs.')

st.markdown('⚙️ :green[Training Results:] the optimal tuned models and the training and cross-validation recall scores.')

st.markdown('🎯 :green[Test Results:] the final evaulation scores for each model. The page displays results in tables and various graphs, including confusion matrices and ROC AUC graphs.')

st.markdown('🧠 :green[SHAP Results:] the feature importance explainations for each model. Global explainaitons are conveyed via beeswarm plots and local explainations via waterfall plots.')

st.markdown('🔧 :green[Detection Tool:] an interactive tool that allows users to input a URL and have it predicted as either legitimate or phishing. The detector also shows local explanations of how it made its decision based on it being legit or phishing.')