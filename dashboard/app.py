import streamlit as st

# Set page to wide format.
st.set_page_config(layout = 'wide')

import sys

from pathlib import Path

# Set root and add to Python path search.
project_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_root))

from routes import pages

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