import re

def extract_features(url):
    features = {}
    features['UsingIP'] = 1 if re.match(r'^https?://\d+\.\d+\.\d+\.\d+/', url) else 0
    features['LongURL'] = len(url) > 75
    features['ShortURL'] = len(url) < 25
    features['Symbol@'] = 1 if '@' in url else 0
    features['Redirecting//'] = 1 if '//' in url else 0
    features['PrefixSuffix-'] = 1 if '-' in url else 0
    features['SubDomains'] = len(re.findall(r'\.', url))
    features['HTTPS'] = 1 if url.startswith('https://') else 0
    features['DomainRegLen'] = len(re.findall(r'\w+', re.split(r'\.', url)[0]))
    # Add more features extraction logic here
    return features

# Example usage
url = "https://www.example.com"
extracted_features = extract_features(url)
print(extracted_features)
