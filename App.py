from sklearn.feature_extraction.text import TfidfVectorizer
import io
import json
from sklearn.svm import SVC
from sklearn.metrics import roc_auc_score

# listFile = ['bad_comment_train.json', 'good_comment_train.json']
#
# def loadAll():
#     data = []
#     for i in range(0, len(listFile)):
#         with io.open(listFile[i], 'r', encoding='utf8') as f:
#             data_file = json.load(f)
#             for j in range(0, len(data_file)):
#                 data.append(data_file[j]['comment'])
#         f.close()
#     return data


import io
import json
from HandleData.handleData import handleInputData
value1 = 1
beginData = loadAll()
while value1 != 0:
    value = input("Nhập đầu vào: ")
    data = []
    with io.open('input.json', 'w', encoding='utf8') as f:
        data.append({
            'rating' : 0.0,
            'comment' : value
        })
        json.dump(data, f)
        f.close()
    handleInputData('input.json')
    with io.open('input.json', 'r', encoding='utf8') as f:
        data = json.load(f)
        if len(beginData) > 9000:
            del beginData[-1]
        beginData.append(data[0]['comment'])
        tfidf_vectorizer = TfidfVectorizer(use_idf=True)
        tfidf_vectorizer_vectors = tfidf_vectorizer.fit_transform(beginData)
        X_train = tfidf_vectorizer_vectors[0:9000]
        X_test = tfidf_vectorizer_vectors[9000:]
        index = 4500
        y_train = []
        for i in range(0, index * 2):
            if (i < index):
                y_train.append(0)
            else:
                y_train.append(1)

        # Train
        clf = SVC(probability=True, kernel='rbf')
        clf.fit(X_train, y_train)
        if(clf.predict(X_test)[0] == 1):
            print("Tích cực")
        else:
            print("Tiêu cực")
        f.close()
