import json
import io

def divideData(file, file1, file2):
    with io.open(file, 'r', encoding='utf8') as f:
        data = json.load(f)
        data_train = data[0: 4500]
        data_test = data[4500: 6500]
        print(len(data_train), len(data_test))
        with io.open(file1, 'w', encoding='utf8') as f:
            json.dump(data_train, f)
        with io.open(file2, 'w', encoding='utf8') as f:
            json.dump(data_test, f)
divideData('bad_comment_full.json', 'bad_comment_train.json', 'bad_comment_test.json')
divideData('good_comment_full.json', 'good_comment_train.json', 'good_comment_test.json')