from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, request, HttpResponseRedirect
# Create your views here.
import os
from django.conf import settings
from handleData import handleInputData
import pickle
from sklearn.pipeline import Pipeline
import io
import json
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfVectorizer
from django.core.serializers.json import DjangoJSONEncoder
c = 4
clf = SVC(probability=True, kernel='rbf')
tfidf_vectorizer = TfidfVectorizer(use_idf=True, min_df=30)



def handleInput(value):
    data = []
    with io.open('input.json', 'w', encoding='utf8') as f:
        data.append({
            'rating' : 0.0,
            'comment' : value
        })
        json.dump(data, f)
        f.close()



def app():
    loop = 'N'
    countT = 0
    count = 0
    with open('model.pickle', 'rb') as f:
        model = pickle.load(f)
    while True:
        inputData = input("Nhập nội dung: ")
        count += 1
        handleInput(inputData)
        handleInputData('input.json')
        # y_test = caculateTfidf(tfidf_vectorizer)
        # result = clf.predict(y_test)
        with io.open('input.json', 'r', encoding='utf8') as f:
            data = json.load(f)
            y_test = [data[0]['comment']]
        result = model.predict(y_test)
        if result[0] == 1:
            print("Tích cực")
        else:
            print("Tiêu cực")
        print("Số lương: ", count)
        print("----------------------------------------")
        #loop = input("Bạn muốn tiếp tục không  ? ")


def index(request):
    if request.method == "GET":
        return render(request, 'p/index.html')
    else:
        print(True)
        # load model
        with open('model.pickle', 'rb') as f:
            model = pickle.load(f)
        comment = request.POST.get('comment')
        handleInput(comment)
        handleInputData('input.json')

        with io.open('input.json', 'r', encoding='utf8') as f:
            data = json.load(f)
            y_test = [data[0]['comment']]
        result = model.predict(y_test)
        return render(request, 'p/index.html', {"comment" : comment, "result" : result[0], "prepare_data" : y_test[0].strip() })

def train(request):
    app()
    return HttpResponse("Ok")


