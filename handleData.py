import json
import io
import re
import unicodedata as ud
from pyvi import ViTokenizer

#list File
listFile = ['bad_comment_train.json', 'bad_comment_test.json', 'good_comment_test.json', 'good_comment_train.json']
#listFile = ['new_train_comment.json', 'testfile1.json']

# Đưa hết về viết thường
def changeToLowerCase(file):
    with io.open(file, 'r', encoding='utf8') as f:
        data = json.load(f)
        newData = []
        for i in range(0, len(data)):
            newData.append({
                'rating' : data[i]['rating'],
                'comment' : data[i]['comment'].lower()
            })
        with io.open(file, 'w', encoding='utf8') as f:
            json.dump(newData, f)

def changeToLowerCaseAll():
    for i in range(0, len(listFile)):
        changeToLowerCase(listFile[i])

# changeToLowerCaseAll()

# Loại bỏ các kí tự đặc biệt, số, không cần thiết
def removeSpecialCharacter(file):
    with io.open(file, 'r', encoding='utf8') as f:
        data = json.load(f)
        newData = []
        for i in range(0, len(data)):
            # newString = re.sub("\W+", " ", data[i]['comment'])
            # newString = re.sub("\d+", "", newString)
            # newString = re.sub("\W+", " ", newString).strip()
            newString = re.sub("[0-9]+.", " ", data[i]['comment'])
            newString = re.sub(
                "[^a-zàáãạảăắằẳẵặâấầẩẫậèéẹẻẽêềếểễệđìíĩỉịòóõọỏôốồổỗộơớờởỡợùúũụủưứừửữựỳỵỷỹýÀÁÃẠẢĂẮẰẲẴẶÂẤẦẨẪẬÈÉẸẺẼÊỀẾỂỄỆĐÌÍĨỈỊÒÓÕỌỎÔỐỒỔỖỘƠỚỜỞỠỢÙÚŨỤỦƯỨỪỬỮỰỲỴỶỸÝ]",
                " ", ud.normalize('NFC', newString)).strip()
            newString = re.sub("\W+", " ", newString)
            newData.append({
                'rating' : data[i]['rating'],
                'comment' : newString
            })
        with io.open(file, 'w', encoding='utf8') as f:
            json.dump(newData, f)

def removeSpecialCharacterAll():
    for i in range(0, len(listFile)):
        removeSpecialCharacter(listFile[i])

# removeSpecialCharacterAll()

#Chuẩn hóa k, ko -> không, bt -> bình thường
def chuanHoa(file):
    with io.open(file, 'r', encoding='utf8') as f:
        data = json.load(f)
        newData = []
        for i in range(0, len(data)):
           newString = data[i]['comment']
           rp = [" k ", " ko ", " kh ", " bt ", " toẹt ", " kout ", " khôg "]
           rp1 = [" không ", " không ", " không ", " bình thường ", " tuyệt ", " cao ", " không "]
           for j in range(0, len(rp)):
                 newString = newString.replace(rp[j], rp1[j])

           newData.append({
               'rating' : data[i]['rating'],
               'comment' : newString
           })


        with io.open(file, 'w', encoding='utf8') as f:
            json.dump(newData, f)

def chuanHoaAll():
    for i in range(0, len(listFile)):
        chuanHoa(listFile[i])

#chuanHoaAll()


#Tách từ
def tachTu(file):
    with io.open(file, 'r', encoding='utf8') as f:
        data = json.load(f)
        newData = []
        for i in range(0, len(data)):
           newString = ViTokenizer.tokenize(data[i]['comment'])
           newData.append({
               'rating' : data[i]['rating'],
               'comment' : newString
           })
           # print(newData[i]['comment'])

        with io.open(file, 'w', encoding='utf8') as f:
            json.dump(newData, f)

def tachTuAll():
    for i in range(0, len(listFile)):
        tachTu(listFile[i])
#tachTuAll()

#Loại bỏ từ dừng
def removeStopWord(file):
    with io.open('stopwords.txt', 'r', encoding='utf8') as f:
        stop_words = f.read().strip().split('\n')
        #print(stop_words)
    with io.open(file, 'r', encoding='utf8') as f:
        data = json.load(f)
        newData = []
        for i in range(0, len(data)):
            newString = data[i]['comment']
            for j in range(0, len(stop_words)):
                word = " " + stop_words[j] + " "
                if(word in newString):
                    newString = newString.replace(word, ' ')
                    newString = re.sub("\W+", " ", newString)
            newData.append({
                'rating' : data[i]['rating'],
                'comment' : newString
            })
    with io.open(file, 'w', encoding='utf8') as f:
        json.dump(newData, f)

def removeStopWordsAll():
    for i in range(0, len(listFile)):
        removeStopWord(listFile[i])
#removeStopWordsAll()

# string = "nước mắm kèm theo gọi thêm xiên thịt mà nhìn như nửa xiên làm hỏng cả bữa trưa chắc không bao giờ mua lại quán này nữa"
# string = ViTokenizer.tokenize(string)
#
# print(string)

def handleAll():
    changeToLowerCaseAll()
    removeSpecialCharacterAll()
    chuanHoaAll()
    removeStopWordsAll()
    tachTuAll()

#handleAll()

def handleInputData(file):
    changeToLowerCase(file)
    removeSpecialCharacter(file)
    chuanHoa(file)
    removeStopWord(file)
    tachTu(file)