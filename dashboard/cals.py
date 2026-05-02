import streamlit as st

from routes import detector

from utils import convert_to_test_data

from feature_extraction.extract_features import url_feat_extractor

from joblib import load

from shap import Explainer

# Cache the random forest model for quicker loading after inital load.
@st.cache_resource
def load_rf():
    return load(detector)

# Cache the SHAP explainer for quicker loading.
@st.cache_resource
def load_explainer():
    return Explainer(load_rf())

def get_test_data(url):
    """
    Return URL as a suitable data for predictions.

    Paramters
    ---------
    url : str
        Cleaned user input.

    Returns
    -------
    test_record : pandas.DataFrame
        A dataframe object which can be used by model.
    """
    # Get features from feature extractor.
    features = url_feat_extractor(url)
    # Get suitable feature format for predictions.
    test_record = convert_to_test_data(features)

    return test_record

def predict_url(test_record, rf):
    """
    Predict the target of a URL.

    Parameters
    ----------
    url : string
        A user inputted URL.
    rf : RandomForestClassifier
        The loaded model which performs predictions.

    Returns
    -------
    pred : int
        Target prediction of either 0 for legit or 1 for phishing.
    proba : array
        Probability predictions for legitimate and phishing.
    """
    
    # Perform predictions.
    pred = rf.predict(test_record)[0]
    proba = rf.predict_proba(test_record)[0]
    
    return pred, proba

def shap_maker(test_data, explainer):
    """
    Create SHAP values from provided model and data.

    Parameters
    ----------
    test_data : pandas.DataFrame
        Test data provided in a dataframe.
    explainer : SHAP.Explainer
        Loaded explainer object to perform SHAP calculations.

    Returns
    -------
    shap_phish : shap.Explainer
        The SHAP object with phishing as the target.
    shap_legit : shap.Explainer
        The SHAP object with legit as the target.
    """
    # Create SHAP object.
    shap_obj = explainer(test_data)
    # SHAP values for phishing feature impact.
    shap_phish = shap_obj[:, :, 1]
    # SHAP values for legit feature impact.
    shap_legit = shap_obj[:, :, 0]
    
    return shap_phish, shap_legit