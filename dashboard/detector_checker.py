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
        st.error(
            'Detector model is missing!\n\n'
            'Please download it from:\n'
            'https://github.com/AntDBuck/Website-Phish-Detection/releases/tag/v1.0\n\n'
            'Place the file in:\n' 
            'saved_data/trained_models/'
        ) 

        st.stop()