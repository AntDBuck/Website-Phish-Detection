import streamlit as st

from pathlib import Path

def check_detector_exists(detector_path: Path):
    """
    Checks if detector model file exists and if not displays a helpful message and stops app.

    Parameters
    ----------
    detector_path : Path
        A Path object that represents the detector model file path.
    """
    if not detector_path.exists():
        st.set_page_config(layout = 'wide')

        st.error('Detector Model Not Found!', icon = '🚫')
        
        st.markdown('Please download the model from:')
        st.markdown('https://github.com/AntDBuck/Website-Phish-Detection/releases/tag/v1.0')

        st.markdown('')

        st.markdown('Place the file in:')
        st.markdown('saved_data/trained_models/')

        st.stop()