from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from tensorflow import keras
import json
from tensorflow.keras.preprocessing.text import Tokenizer
import pickle
import numpy as np
import re
from unicodedata import normalize as norm
import pandas as pd
import os

import os

LOCAL_PATH = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(LOCAL_PATH,'model.h5')

PICKLE_PATH = os.path.join(LOCAL_PATH,'tokenizer.pickle')

ENCODE_PATH = os.path.join(LOCAL_PATH,'label_encoder.pickle')


model = keras.models.load_model(MODEL_PATH)

with open(PICKLE_PATH, 'rb') as handle:

    tokenizer = pickle.load(handle)

with open(ENCODE_PATH, 'rb') as handle:

    encode_label = pickle.load(handle)


def text_cleaner(text):
    
    #nltk_stopwords = stopwords.words('portuguese')

    collection_text = [ {"text" : text}]
    text = pd.DataFrame(collection_text)

    text['text'] = text['text'].astype('str')
    text['text'] = text['text'].str.lower()
    text['text'] = text['text'].str.replace('\n',' ')
    text['text'] = text['text'].str.replace('\r',' ')
    text['text'] = text['text'].apply(lambda x: norm('NFKD', x).encode('ascii', 'ignore').decode())
    text['text'] = text['text'].apply(lambda x: re.sub(r'[^a-zA-Z0-9]',' ',x))
    text['text'] = text['text'].apply(lambda x: re.sub(r'\s+',' ',x))
    #pat = r'\b(?:{})\b'.format('|'.join(nltk_stopwords))
    #text['text'] = text['text'].str.replace(pat,'')
    text = text['text'].values[0]

    return text






@csrf_exempt
def index(request):

    #received_json_data=json.loads(request.POST['data'])


    if request.method == 'POST':

        data = json.loads(request.body)

        print(data)


        text = text_cleaner(data['text'])

        sample_converted = tokenizer.texts_to_matrix([text],mode='tfidf')

        predict = model.predict(sample_converted)

        class_proba = np.max(predict[0])

        class_predicted = np.argmax(predict[0])

        class_predicted = encode_label.inverse_transform([class_predicted])


        dados = {"class_predicted":class_predicted.tolist()[0],"proba_predicted":class_proba.astype(float)}

        #return JsonResponse({"class_predicted":class_predicted.tolist()[0],"proba_predicted":class_proba.astype(float)})

        return render(request,"index.html",dados)

    elif request.method == 'GET':

        dados = {"class_predicted":"NO CLASS","probability":[0,1],
        "probabilities":[0,0,0,0],
        "lime":[0,0,0,0,0],
        "probabilityText":"0%","confidence":"No probability"}


        return render(request,"index.html",dados)

