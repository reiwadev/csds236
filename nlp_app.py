# Create a file, import all the junk
import streamlit as st
from textblob import TextBlob
from nltk.stem.wordnet import WordNetLemmatizer
import re
import nltk


# Create the GUI that takes user input for sentiment analysis
# Provide a title, define a text area
# Create a button "Analyze" that will return the sentiment polarity and sentiment for the text

st.title("""Language Interpreter""")
st.write("Hello")
text = st.text_area("Insert the text to analyze here")

# Use the following code to clean the text
#Keeping only Text and digits
text = re.sub(r"[^A-Za-z0-9]", " ", text)
#Removes Whitespaces
text = re.sub(r"\'s", " ", text)
# Removing Links if any
text = re.sub(r"http\S+", " link ", text)
# Removes Punctuations and Numbers
text = re.sub(r"\b\d+(?:\.\d+)?\s+", "", text)
# Splitting Text
text = text.split()
# Lemmatizer
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in text]
text = " ".join(lemmatized_words)

# Process the cleaned text when Analyze Button is clicked
if st.button("Analyze Text"):
        blob = TextBlob(text)
        sentiment_score = blob.sentiment.polarity
        if sentiment_score > 0:
            custom_emoji = ':blush:'
            st.success('Happy : {}'.format(custom_emoji))
        elif sentiment_score < 0:
            custom_emoji = ':disappointed:'
            st.warning('Sad : {}'.format(custom_emoji))
        else:
            custom_emoji = ':confused:'
            st.info('Confused : {}'.format(custom_emoji))
        st.success("Polarity Score is: {}".format(sentiment_score))
