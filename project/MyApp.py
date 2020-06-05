from joblib import dump, load
import pickle
from HandleData.handleData import handleInputData
import io
import json
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
import pickle

clf = SVC(probability=True, kernel='rbf')
tfidf_vectorizer = TfidfVectorizer(use_idf=True, min_df=30)

#List file train
listFile = ['bad_comment_train.json', 'good_comment_train.json', 'new_train_comment.json']

#Read file
def loadAll():
    data = []
    for i in range(0, len(listFile)):
        with io.open(listFile[i], 'r', encoding='utf8') as f:
            data_file = json.load(f)
            for j in range(0, len(data_file)):
                data.append(data_file[j]['comment'])
    print(len(data))
    return data

#Caculate tfidf
def caculateTfidf(vector):
    # python 3 ko can io mà :)), t search thấy thế để đọc utf8 nên t dùng ấy, tưởng nó xịn cơ ;3
    with io.open('input.json', 'r', encoding='utf8') as f:
        data = json.load(f)
    print(data[0]['comment'])
    y_test = vector.transform([data[0]['comment']])
    return y_test

def handleInput(value):
    data = []
    with io.open('input.json', 'w', encoding='utf8') as f:
        data.append({
            'rating' : 0.0,
            'comment' : value
        })
        json.dump(data, f)
        f.close()

def readFileInput():
    with io.open('input.json', 'r', encoding='utf8') as f:
        data = json.load(f)
    return data[0]['comment']

def init():
    dataN = loadAll()
    tfidf_vectorizer.fit(dataN)
    X_train = tfidf_vectorizer.transform(dataN)
    print(X_train.shape)
    index = 4500
    y_train = []
    for i in range(0, index * 2):
        if (i < index):
            y_train.append(0)
        else:
            y_train.append(1)
    new_comment = 4500
    for i in range(0, new_comment * 2):
        if i < new_comment:
            y_train.append(0)
        else:
            y_train.append(1)
    clf.fit(X_train, y_train)


def app():
    loop = 'N'
    countT = 0
    count = 0
    while True:
        inputData = input("Nhập nội dung: ")
        count += 1
        handleInput(inputData)
        handleInputData('input.json')
        y_test = caculateTfidf(tfidf_vectorizer)
        result = clf.predict(y_test)
        if result[0] == 1:
            print("Tích cực")
        else:
            print("Tiêu cực")
        print("Số lương: ", count)
        print("----------------------------------------")
        #loop = input("Bạn muốn tiếp tục không  ? ")

init()
app()
#test()
#app()
