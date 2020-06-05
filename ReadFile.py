import json
import io

data1 = []
data2 = []
with io.open('stopwords.txt', 'r', encoding='utf8') as f:
    # data = json.load(f)
    # print(len(data))
    # for i in range(0, len(data)):
    #     print(data[i]['comment'].strip(), ":", data[i]['rating'], end='\n\n')
    data1 = f.read().strip().split('\n')
    print(data1)
with io.open('vietnamese-stopwords.txt', 'r', encoding='utf8') as f:
    # data = json.load(f)
    # print(len(data))
    # for i in range(0, len(data)):
    #     print(data[i]['comment'].strip(), ":", data[i]['rating'], end='\n\n')
    data2 = f.read().strip().split('\n')
for i in range(0, len(data2)):
    if data2[i] not in data1:
        print(data2[i])
# đây là dữ liệu file tệ ông ạ, thế là ông toàn dưới 4 vs trên 7 à, ừm
# dưới 4.5, và >= 7.5 để chắc chắn dữ liệu phân loại là chuẩn
# oke, để t xem lại cái của t, có j hôm sau teamview tiếp n há, ochaán thật, t thấy của ông chạy đoạn dài ok mthaatjoke hnay t tét tiếp
# off nhá ok