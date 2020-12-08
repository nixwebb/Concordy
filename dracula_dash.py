# Dashboard experiment

import streamlit as st
import urllib.request
import nltk
import ssl
import matplotlib.pyplot as plt

context = ssl._create_unverified_context()

nltk.download('punkt')

st.title('Dashboard: Dracula')


def load_text(fileName):
    response = urllib.request.urlopen(fileName)
    data = response.read()      # a `bytes` object
    text = data.decode('utf-8-sig') # a `str`; this step can't be used if data is binary
    return(text)


data_load_state = st.text('Loading data...')

fileName = "http://www.gutenberg.org/cache/epub/345/pg345.txt"
data = load_text(fileName)

data_load_state.text('Loading data...done!')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Dracula in Dracula')

sents = nltk.sent_tokenize(data)
dracula_counts = []
for sent in sents:
    toks = nltk.word_tokenize(sent)
    dc = toks.count('Dracula')
    if dracula_counts == []:
        current = 0
    else:
        current = dracula_counts[-1]
    new = current + dc
    dracula_counts.append(new)

sentInt = list(range(len(sents)))    

plt.xlabel('Sentence number')
plt.ylabel('Cumulative counts')
plt.plot(sentInt,dracula_counts)

st.pyplot()


