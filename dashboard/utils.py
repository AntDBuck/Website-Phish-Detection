import pandas as pd

from urllib.parse import urlparse

import tldextract

def create_dataframe(dir_loc, index_title):
    """
    Convert CSV file to dataframe, reset index column, and set index title.

    Parameters
    ----------
    dir_loc : Path
        Path object pointing to directory.
    index_title : str
        Name of index title.

    Returns
    -------
    df : pandas.DataFrame
        Dataframe version of CSV file.
    """
    df = pd.read_csv(str(dir_loc), index_col = 0)
    df.index.name = index_title
    
    return df

def format_cr(df):
    """
    Remove accuracy rows and focus on class split metrics.

    Parameters
    ----------
    df : pandas.DataFrame
        Classification report held in a dataframe.

    Returns
    -------
    new_df : pandas.DataFrame
        DataFrame containing the class rows.
    """
    new_df = df.loc[['Legitimate', 'Phishing']]
    
    return new_df

def input_handler(user_input = None):
    """
    Handle user input by removing leading spaces and appending scheme if not provided.

    Parameters
    ----------
    user_input : str
        Input provided from user.

    Returns
    -------
    url : str or None
        Checked URL with possible scheme appended and reject spaces, empty hostnames, and empty TLDs, or None if input is empty.
    """
    # If user inputted no string return None.
    if user_input is None:
        return None

    # Remove extra spaces from input and check URL is not None.
    url = user_input.strip()
    if not url:
        return None

    # If URL contains any spaces (not allowed in aa URL) then return None.
    if ' ' in url:
        return None

    # If URL does not have a scheme, appended one.
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    
    parsed = urlparse(url)

    # If no hostname return None.
    if not parsed.hostname:
        return None

    extract = tldextract.extract(url)

    # If no TLD return None.
    if not extract.suffix:
        return None
    
    return url

def convert_to_test_data(features):
    """
    Combine extracted features and column names into a DataFrame.

    Parameters
    ----------
    features : list[int | float]
        The numeric feature values from the extracted URL.

    Returns
    -------
    df : pandas.DataFrame
        A DataFrame containing feature column names and values.
    """
    col_names = [
        'length_url', 'length_hostname', 'ip', 'nb_dots', 
        'nb_hyphens', 'nb_at', 'nb_qm', 'nb_and', 'nb_or', 
        'nb_eq', 'nb_underscore', 'nb_tilde', 'nb_percent', 
        'nb_slash', 'nb_star', 'nb_colon', 'nb_comma',
        'nb_semicolumn', 'nb_dollar', 'nb_space', 'nb_www', 
        'nb_com', 'nb_dslash', 'http_in_path', 'https_token', 
        'ratio_digits_url', 'ratio_digits_host', 'punycode', 
        'port', 'tld_in_path', 'tld_in_subdomain', 
        'abnormal_subdomain', 'nb_subdomains', 'prefix_suffix',
        'shortening_service', 'path_extension', 'length_words_raw', 
        'char_repeat', 'shortest_words_raw', 'shortest_word_host', 
        'shortest_word_path', 'longest_words_raw', 'longest_word_host',
        'longest_word_path', 'avg_words_raw', 'avg_word_host', 
        'avg_word_path', 'phish_hints', 'suspecious_tld'
    ]

    df = pd.DataFrame(data = [features], columns = col_names)

    return df