from joblib import dump, load
import pickle
from HandleData.handleData import handleInputData
import io
import json
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline

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
    # pipe = Pipeline([('tfidf_vectorizer', TfidfVectorizer(use_idf=True, min_df=30)), ('clf', SVC(probability=True, kernel='rbf'))])
    # # pipe.fit(X_train, y_train)
    # pipe.fit(dataN, y_train)
    # with open('model.pickle', 'wb') as f:
    #     pickle.dump(pipe, f)

def test():
    data = []
    for i in range(0, 1):
        with io.open('testfile1.json', 'r', encoding='utf8') as f:
            data_file = json.load(f)
            for j in range(0, len(data_file)):
                data.append(data_file[j]['comment'])
    data1 = []
    for i in range(0, 1):
        with io.open('testfile1.json', 'r', encoding='utf8') as f:
            data_file = json.load(f)
            for j in range(0, len(data_file)):
                data1.append(data_file[j]['comment'])
    index = 2000
    X_test = tfidf_vectorizer.transform(data)
    y_test = []
    for i in range(0, index * 2):
        if i < index:
            y_test.append(0)
        else:
            y_test.append(1)
    result =  clf.predict(X_test)
    countT = countF = count = 0
    for i in range(0, len(result)):
        if(result[i] == y_test[i]):
            count += 1
        elif result[i] == 0:
            countT += 1
            print("Tích cực: ", print(data[i]))
            print("..........", print(data1[i]), end='\n\n')
        elif result[i] == 1:
            countF += 1
            print("Tiêu cực: ", print(data[i]))
            print("..........", print(data1[i]), end='\n\n')
        print()
    print("Văn bản đúng: ", countT)
    print("Văn bản sai: ", countF)
    print("Kết quả đúng là: ", str(count) + "/4000", " ~", count/4000)

def test1():
    test = ['bad_comment_test.json', 'good_comment_test.json']
    data = []
    for i in range(0, len(test)):
        with io.open(test[i], 'r', encoding='utf8') as f:
            data_file = json.load(f)
            for j in range(0, len(data_file)):
                data.append(data_file[j]['comment'])
    X_test = tfidf_vectorizer.transform(data)
    y_test = []
    index = 2000
    for i in range(0, index * 2):
        if i < index:
            y_test.append(0)
        else:
            y_test.append(1)
    result = clf.predict(X_test)
    countT = countF = count = 0
    for i in range(0, len(result)):
        if(result[i] == y_test[i]):
            count += 1
        elif result[i] == 0:
            countT += 1
        elif result[i] == 1:
            countF += 1

    print("Văn bản đúng: ", countT)
    print("Văn bản sai: ", countF)
    print("Kết quả đúng là: ", str(count) + "/4000", " ~", count / 4000)


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
        #y_test = caculateTfidf(tfidf_vectorizer)
        #result = clf.predict(y_test)
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


#init()
#test1()
#test()
app()
#test()
#app()
