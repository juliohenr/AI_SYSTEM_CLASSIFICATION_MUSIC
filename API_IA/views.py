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
from django.shortcuts import redirect

LOCAL_PATH = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(LOCAL_PATH,'model.h5')

PICKLE_PATH = os.path.join(LOCAL_PATH,'tokenizer.pickle')

ENCODE_PATH = os.path.join(LOCAL_PATH,'label_encoder.pickle')


AVG_WORDS_FUNK = 24

AVG_WORDS_GOSPEL = 25

AVG_WORDS_SERTANEJO = 27

AVG_WORDS_BOSSA_NOVA = 20



AVG_DIFERENT_WORDS_FUNK = 5

AVG_DIFERENT_WORDS_GOSPEL = 15

AVG_DIFERENT_WORDS_SERTANEJO = 18

AVG_DIFERENT_WORDS_BOSSA_NOVA = 20



model = keras.models.load_model(MODEL_PATH)

with open(PICKLE_PATH, 'rb') as handle:

    tokenizer = pickle.load(handle)

with open(ENCODE_PATH, 'rb') as handle:

    encode_label = pickle.load(handle)

data_global = {"data_global":None}


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



def calculate_number_words(text):

    quantity_of_words = text.split(" ")

    quantity_of_words = len(quantity_of_words)

    return quantity_of_words



def calculate_number_diferent_words(text):

    quantity_of_diferent_words = text.split(" ")

    quantity_of_diferent_words = set(quantity_of_diferent_words)

    quantity_of_diferent_words = list(quantity_of_diferent_words)

    quantity_of_diferent_words = len(quantity_of_diferent_words)

    return quantity_of_diferent_words


def calculate_most_frequents_words(text,number_words=5):

    words_split = text.split(" ")

    qnt_words = len(words_split)

    df_words = pd.DataFrame({"WORDS":words_split})

    df_words["COUNT"] = 1

    df_words = df_words.groupby("WORDS").count().sort_values(by=['COUNT'],ascending=False)

    df_words["COUNT"] = df_words["COUNT"]/qnt_words

    df_words['WORDS'] =  list(df_words.index)

    df_words.reset_index(drop=True,inplace=True)

    frequenties_words = list(df_words['WORDS'].values)

    frequenties_words = frequenties_words[0:number_words]

    frequenty = list(df_words['COUNT'].values*100)

    frequenty = frequenty[0:number_words]



    return {"WORDS":frequenties_words,"COUNT":frequenty}





@csrf_exempt
def index(request):

    #received_json_data=json.loads(request.POST['data'])


    if data_global["data_global"]:


        dados = data_global["data_global"]

        print("\n")
        print("\n")
        print("\n")


        print(data_global["data_global"])

        print("\n")
        print("\n")
        print("\n")

        #return JsonResponse({"class_predicted":class_predicted.tolist()[0],"proba_predicted":class_proba.astype(float)})

        return render(request,"index.html",dados)

    else:


        print("\n")
        print("\n")
        print("\n")


        print(data_global["data_global"])

        print("\n")
        print("\n")
        print("\n")

        dados = {"class_predicted":"NO CLASS","probability":[0,1],
        "probabilities":[0,0,0,0],
        "lime":[0,0,0,0,0],
        "probabilityText":"0%","confidence":"No probability"}


        return render(request,"index.html",dados)

        #return JsonResponse({"class_predicted":"teste"})


@csrf_exempt
def results(request):


    

    #received_json_data=json.loads(request.POST['data'])


    data = json.loads(json.dumps(request.POST))


    #data = json.loads(request.body)

    text = text_cleaner(data['text'])

    number_of_words = calculate_number_words(text)

    number_of_diferent_words = calculate_number_diferent_words(text)

    frequenties_words = calculate_most_frequents_words(text,number_words=5)

    quantity_words_statistics = [ 100*(number_of_words/AVG_WORDS_BOSSA_NOVA - 1),
                                 100*(number_of_words/AVG_WORDS_FUNK - 1),
                                100*(number_of_words/AVG_WORDS_GOSPEL - 1),
                                 100*(number_of_words/AVG_WORDS_SERTANEJO - 1)]


    quantity_diferent_words_statistics = [100*(number_of_diferent_words/AVG_DIFERENT_WORDS_BOSSA_NOVA - 1),
                                        100*(number_of_diferent_words/AVG_DIFERENT_WORDS_FUNK - 1) ,
                                        100*(number_of_diferent_words/AVG_DIFERENT_WORDS_GOSPEL - 1),
                                         100*(number_of_diferent_words/AVG_DIFERENT_WORDS_SERTANEJO - 1)]



    sample_converted = tokenizer.texts_to_matrix([text],mode='tfidf')

    predict = model.predict(sample_converted)

    class_proba = np.max(predict[0])

    class_predicted = np.argmax(predict[0])

    class_predicted = encode_label.inverse_transform([class_predicted])

    all_classes = encode_label.inverse_transform([0,1,2,3])

    print("\n")
    print("\n")
    print("\n")
    print("\n")

    print(all_classes)

    print("\n")
    print("\n")
    print("\n")
    print("\n")

    if int(class_proba*100)<50 :

        confidence_status = "LOW CONFIDENCE"

    elif int(class_proba*100)>=50 and int(class_proba*100)<70:

        confidence_status = "MEDIUM CONFIDENCE"

    else:

        confidence_status = "HIGH CONFIDENCE"

    dados = {"class_predicted":class_predicted[0],"probability":[class_proba,1-class_proba],
    "probabilities":list(predict[0]*100),
    "probabilityText":str(int(class_proba*100)) + "%","confidence":confidence_status,
    "quantity_words_statistics":quantity_words_statistics,
    "quantity_diferent_words_statistics":quantity_diferent_words_statistics,
    "frequenties_words":frequenties_words}

    data_global["data_global"] = dados


    #return JsonResponse({"class_predicted":class_predicted.tolist()[0],"proba_predicted":class_proba.astype(float)})


    return JsonResponse({"class_predicted":class_predicted.tolist()[0],"proba_predicted":class_proba.astype(float)})




