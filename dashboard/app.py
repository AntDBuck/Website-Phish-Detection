import streamlit as st

import sys

from routes import root

sys.path.insert(0, str(root))

from routes import pages

# Set page to wide format.
st.set_page_config(layout = 'wide')

# Define pages from page files.
home = st.Page(str(pages/'home.py'), title = 'Home', icon = '🏠')
eda = st.Page(str(pages/'eda.py'), title = 'EDA', icon = '🔍')
baseline = st.Page(str(pages/'baseline.py'), title = 'Baseline Results', icon = '📈')
training = st.Page(str(pages/'training.py'), title = 'Training Results', icon = '⚙️')
results = st.Page(str(pages/'results.py'), title = 'Test Results', icon = '🎯')
shap = st.Page(str(pages/'shap.py'), title = 'SHAP Results', icon = '🧠')
tool = st.Page(str(pages/'detect_tool.py'), title = 'Detection Tool', icon = '🔧')

# Define router as navigation interface.
router = st.navigation([home, eda, baseline, training, results, shap, tool], position = 'top')

# Run router.
router.run()