import pandas as pd

# Load the dataset
df = pd.read_csv('path_to_your_downloaded_sms_spam_dataset.csv', encoding='latin-1')

# Display the first few rows of the dataset
df.head()

import re
from nltk.corpus import stopwords

# Clean the SMS text
def clean_text(text):
    text = re.sub(r'\W', ' ', text)  # Remove non-word characters (like punctuation)
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'^\s+|\s+?$', '', text)  # Remove leading/trailing spaces
    return text

df['cleaned_text'] = df['v2'].apply(clean_text)

# Check the cleaned text
df[['v2', 'cleaned_text']].head()

from sklearn.feature_extraction.text import TfidfVectorizer

# Convert the text data into numerical features using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X = vectorizer.fit_transform(df['cleaned_text'])

# Convert labels (ham = 0, spam = 1)
y = df['v1'].map({'ham': 0, 'spam': 1})
