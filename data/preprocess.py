import re
import nltk
from nltk.corpus import stopwords
import spacy

nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
lemma = spacy.load('en_core_web_sm')
class Preprocess:
    def __init__(self):
        pass

    def preprocess_topic_detection(self, text):
        text = text.lower()

        text = re.sub(r'http\S+|www\S+|https\S+', '', text)
        text = re.sub(r'@\w+', '', text)
        text = re.sub(r'#', '', text)
        emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               "]+", flags=re.UNICODE)
        text = emoji_pattern.sub(r'', text)
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        text = re.sub(r'\s+', ' ', text).strip()

        doc = lemma(text)
        tokens = [token.lemma_ for token in doc if token.text not in stop_words and not token.is_punct]
    
        return ' '.join(tokens)

# preprocess = Preprocess()
# comment = "I LOOOVE this product!!! It's amazing 🔥 #bestpurchase"
# print(preprocess.preprocess_topic_detection(comment))