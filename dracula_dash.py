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

input = st.text_input("Words to search for (separate words with space):","Dracula vampire")
words = input.split()
cD = {word:[] for word in words}

sents = nltk.sent_tokenize(data)

for sent in sents:

    toks = nltk.word_tokenize(sent)
    for word in words:


        dc = toks.count(word)
        if cD[word] == []:
            current = 0
        else:
            current = cD[word][-1]
        new = current + dc
        cD[word].append(new)

sentInt = list(range(len(sents)))    

plt.xlabel('Sentence number')
plt.ylabel('Cumulative counts')

for key in cD:
    plt.plot(sentInt,cD[key],label=key)

plt.legend()

st.pyplot()


