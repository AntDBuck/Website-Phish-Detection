import streamlit as st

# Show message while waiting for resouces to load.
load_msg = st.empty()
load_msg.info('Loading Resources, Please Wait...')

from shap.plots import waterfall

import matplotlib.pyplot as plt

from utils import input_handler

from cals import get_test_data, predict_url, shap_maker, load_rf, load_explainer

# Load model and SHAP explainer once, then cached.
rf = load_rf()
explainer = load_explainer()

# Remove loading message when resources loaded.
load_msg.empty()

st.title('🔧 Detection Tool', text_alignment = 'center')

st.header('🔽 URL Input', divider = 'blue')

# Text box input.
user_input = st.text_input('Enter Full URL Here:', placeholder = 'http://www.example-site.com')

# Button.
submit = st.button('Detect')

# If button is clicked then...
if submit:
    # Clean user input.
    url = input_handler(user_input)

    # If URL is None, display warning message and prompt user to try again.
    if not url:
        st.warning('Input is not a valid URL. Please try again.')
    else:
        # Show user's inputted URL for visual feedback.
        st.text(f'Provided URL: {url}')

        # Create test data from URL.
        test_data = get_test_data(url)

        # Get predictions and class probabilities.
        pred, proba = predict_url(test_data, rf)
        legit_proba = proba[0]
        phish_proba = proba[1]

        st.header('🛡️ Results', divider = 'rainbow')

        # If prediction is phishing print error message.
        if pred == 1:
            st.error('The URL has been predicted as phishing!')
        else:
            # If prediction is legit print success message.
            st.success('The URL has been predicted as legitimate!')

        # Get SHAP values for the instance. 
        phish_values, legit_values = shap_maker(test_data, explainer)
        
        legit_col, phish_col = st.columns(2)
        
        with legit_col:
            st.subheader('Legitimate Clues')

            # Display probabilty as metric.
            st.metric('Legitmate Website Probability', f'{legit_proba:.0%}')

            # Dispaly waterfall plot.
            plt.figure(figsize = (10, 8), constrained_layout = True)
            waterfall(legit_values[0], show = False)
            st.pyplot(plt.gcf())
            plt.clf()

        with phish_col:
            st.subheader('Phishing Clues')

            # Display probabilty as metric.
            st.metric('Phishing Website Probability:', f'{phish_proba:.0%}')

            # Dispaly waterfall plot.
            plt.figure(figsize = (10, 8), constrained_layout = True)
            waterfall(phish_values[0], show = False)
            st.pyplot(plt.gcf())
            plt.clf()
