import re

from urllib.parse import urlparse

import tldextract

from . import url_features as url_feats

def url_feat_extractor(url):
    """
    Extract all required features from a URL.

    Parameters
    ----------
    url : str
        The full URL.

    Returns
    -------
    features : list[int | float]
        A list containing numeric feature data from a URL.
    """
    # Break down the URL into its smaller components and store them in variables.
    parsed = urlparse(url)
    extract = tldextract.extract(url)

    scheme = parsed.scheme
    hostname = parsed.hostname or ''
    path = parsed.path
    domain = extract.domain
    subdomain = extract.subdomain
    tld = extract.suffix

    # Original function provided with dataset - has been slightly modified.
    def words_raw_extraction(domain, subdomain, path):
        w_domain = re.split(r'[\-\.\/\?\=\@\&\%\:\_]', domain.lower())
        w_subdomain = re.split(r'[\-\.\/\?\=\@\&\%\:\_]', subdomain.lower())   
        w_path = re.split(r'[\-\.\/\?\=\@\&\%\:\_]', path.lower())
        
        raw_words = w_domain + w_path + w_subdomain
        w_host = w_domain + w_subdomain
        raw_words = list(filter(None, raw_words))
        w_host = list(filter(None, w_host))
        w_path = list(filter(None, w_path))
        
        return raw_words, w_host, w_path
    # End of function.

    raw_words, raw_host_words, raw_path_words = words_raw_extraction(domain, subdomain, path)

    # Pass the URL and components into the various functions defined in the url_features file.
    features = [
        url_feats.url_length(url),
        url_feats.url_length(hostname),
        url_feats.having_ip_address(url),
        url_feats.count_dots(url),
        url_feats.count_hyphens(url),
        url_feats.count_at(url),
        url_feats.count_exclamation(url),
        url_feats.count_and(url),
        url_feats.count_or(url),
        url_feats.count_equal(url),
        url_feats.count_underscore(url),
        url_feats.count_tilde(url),
        url_feats.count_percentage(url),
        url_feats.count_slash(url),
        url_feats.count_star(url),
        url_feats.count_colon(url),
        url_feats.count_comma(url),
        url_feats.count_semicolumn(url),
        url_feats.count_dollar(url),
        url_feats.count_space(url),
        url_feats.check_www(raw_words),
        url_feats.check_com(raw_words),
        url_feats.count_double_slash(url),
        url_feats.count_http_token(path),
        url_feats.https_token(scheme),
        url_feats.ratio_digits(url),
        url_feats.ratio_digits(hostname),
        url_feats.punycode(url),
        url_feats.port(url),
        url_feats.tld_in_path(tld, path),
        url_feats.tld_in_subdomain(tld, subdomain),
        url_feats.abnormal_subdomain(url),
        url_feats.count_subdomain(url),
        url_feats.prefix_suffix(url),
        url_feats.shortening_service(url),
        url_feats.path_extension(path),
        url_feats.length_word_raw(raw_words),
        url_feats.char_repeat(raw_words),
        url_feats.shortest_word_length(raw_words),
        url_feats.shortest_word_length(raw_host_words),
        url_feats.shortest_word_length(raw_path_words),
        url_feats.longest_word_length(raw_words),
        url_feats.longest_word_length(raw_host_words),
        url_feats.longest_word_length(raw_path_words),
        url_feats.average_word_length(raw_words),
        url_feats.average_word_length(raw_host_words),
        url_feats.average_word_length(raw_path_words),
        url_feats.phish_hints(url),          
        url_feats.suspecious_tld(tld)
    ]

    return features