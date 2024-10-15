# Phishing Website Detector

## Overview

This Jupyter Notebook-based project is a Phishing Website Detector that employs machine learning algorithms to classify websites as legitimate or phishing. It utilizes the following algorithms:

| Algorithm            | Accuracy | F-score | Recall | Precision |
|----------------------|----------|---------|--------|-----------|
| Gradient Boost       | 0.96| 0.95| 0.96| 0.96|
| Random Forest        | 0.97| 0.96| 0.95| 0.97|
| Decision Tree        | 0.96| 0.95| 0.96| 0.95|
| K-nearest neighbor   | 0.96| 0.95| 0.95| 0.96|

## About Phishing Websites

Phishing websites are fraudulent sites designed to impersonate trusted entities, aiming to deceive users into disclosing sensitive information. These websites employ methods such as email phishing, spear phishing, vishing, and smishing.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/MSVelan/Phishing-Website-Tracker
    ```

2. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Data Collection

- For this project, we collected a dataset of URLs, including both legitimate and phishing URLs. Several online sources, such as web archives and known phishing websites, were used to obtain these URLs.

## Feature Extraction

This section outlines the key features extracted from the collected URLs to classify them as legitimate or phishing:

1. **Address Bar-Based Features:** These features include domain extraction, IP address presence, "@" symbol, URL length, depth, redirection indicators, "http/https" in the domain, URL shortening, and prefix/suffix checks.

2. **Domain-Based Features:** Derived from domain information, these include DNS record availability, web traffic rank, domain age, and time until domain expiration.

3. **HTML and JavaScript-Based Features:** Features such as IFrame presence, status bar customization, right-click disablement, and website forwarding indicators.

4. **Computing URL Features:** A function is developed to extract these features for building a dataset.

The dataset, including legitimate and phishing URLs' features, will be used for training machine learning models to differentiate between the two.

## Data Processing

- The dataset was preprocessed to handle missing values and format issues, ensuring data integrity.
- It was then divided into training and testing subsets for subsequent model development and evaluation.

## Usage

Within the Jupyter Notebook, follow the provided instructions to execute the detector with your preferred algorithm. You will find code cells and explanations to guide you through the process.

## Data

The detector uses a dataset of website features to train and test the models. The dataset should be located in a file named `data.csv`. Ensure that your dataset follows the required format.

## Results

After running the detector within the Jupyter Notebook, you will see the classification results, including accuracy and other relevant metrics, depending on the algorithm used. These results will help you assess the detector's performance.
