import re
import tldextract
from urllib.parse import urlparse

def extract_features(url):
    features = []
    
    # Feature 1: URL Length
    features.append(len(url))

    # Feature 2: Has IP Address
    ip_pattern = re.compile(
        r"(http|https)?://(\d{1,3}\.){3}\d{1,3}")
    features.append(1 if ip_pattern.search(url) else 0)

    # Feature 3: '@' in URL
    features.append(1 if '@' in url else 0)

    # Feature 4: Count of dots
    features.append(url.count('.'))

    # Feature 5: Presence of HTTPS
    features.append(1 if 'https' in url else 0)

    # Feature 6: Double slash in path
    features.append(1 if url.count('//') > 1 else 0)

    # Feature 7: Presence of hyphen in domain
    domain = tldextract.extract(url).domain
    features.append(1 if '-' in domain else 0)

    # Feature 8: Length of domain
    features.append(len(domain))

    return features
