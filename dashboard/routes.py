from pathlib import Path

# Define root directory location.
root = Path(__file__).resolve().parents[1]

# Define various routes.
pages = root/'dashboard'/'pages'
saved_data = root/'saved_data'

figs = saved_data/'figures'
eda_figs = figs/'eda_graphs'
eval_figs = figs/'evaluation_graphs'
shap_figs = figs/'shap_graphs'

data_res = saved_data/'data_results'
eda_data = saved_data/'eda'
baseline_data = data_res/'baseline_results'
training_data = data_res/'training_results'
test_data = data_res/'test_results'

detector = saved_data/'trained_models'/'best_url_rf.pkl'