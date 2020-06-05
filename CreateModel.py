
import io
import json
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import roc_auc_score

listFile = ['bad_comment_train.json', 'good_comment_train.json', 'bad_comment_test.json', 'good_comment_test.json']
listPrototypeFile  = ['bad_comment_full.json', 'good_comment_full.json']



def loadAll(begin, end):
    data = []
    for i in range(begin, end):
        with io.open(listFile[i], 'r', encoding='utf8') as f:
            data_file = json.load(f)
            for j in range(0, len(data_file)):
                data.append(data_file[j]['comment'])
    print(len(data))
    return data

def loadPrototypeData():
    data = []
    for i in range(0, len(listPrototypeFile)):
        with io.open(listPrototypeFile[i], 'r', encoding='utf8') as f:
            data_file = json.load(f)
            for j in range(4500, 6500):
                    data.append(data_file[j]['comment'])
    print(len(data))
    return data

dataPrototype = loadPrototypeData()
dataN = loadAll(0, 4)
dataT = dataN[9000:13000]
tfidf_vectorizer = TfidfVectorizer(use_idf=True)
tfidf_vectorizer.fit(dataN[0:9000])

import pickle
# chỗ này không có gì đâu ông, kiểu ddeerr tôi xây dựng model thôi, tất cả model t để sang file MyApp rồi !
from sklearn.pipeline import make_pipeline
X_train = tfidf_vectorizer.transform(dataN[0:9000])
pickle.dump(X_train, open("tran_comment_features.pickle", "wb"))
X_test = tfidf_vectorizer.transform(dataN[9000:])
print(X_train.shape, X_test.shape)
index = 4500
y_train = []
for i in range(0, index * 2):
    if(i < index):
        y_train.append(0)
    else:
        y_train.append(1)
# index = 2000
# y_test = []
# for i in range(0, index * 2):
#     if(i < index):
#         y_test.append(0)
#     else:
#         y_test.append(1)
#
#Train
# clf = SVC(probability=True, kernel='rbf')
# clf.fit(X_train, y_train)

# pipeline = make_pipeline(tfidf_vectorizer, clf)
# pipeline.fit(X_train, y_train)
# pickle.dump(pipeline, open("pipiline.pickle", "wb"))

import pickle
from joblib import dump, load
#
clf = load('model1.joblib')
print(clf)
clf.predict(X_test)
# dump(clf, 'model1.joblib')


#Predict
# predicts = clf.predict(X_test)
# print(len(predicts))
#
# count = 0
# countT = countF = 1
# for i in range(0, len(predicts)):
#     if(predicts[i] == y_test[i]):
#         count += 1
#     else:
#         prototypeContent = ""
#         if predicts[i] == 1:
#                 countT += 1
#                 prototypeContent = dataPrototype[i]
#                 print(prototypeContent)
#         else:
#             countF += 1
#             prototypeContent = dataPrototype[i]
#             print(prototypeContent)
#         print(dataT[i], predicts[i], end='\n\n')
#
# print("Sai Tich Cuc: ", countT)
# print("Sai Tieu Cuc: ", countF)
# print("Count :", count)
# print("Do chinh xac: ", count/4000)
