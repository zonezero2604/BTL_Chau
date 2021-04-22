from os import listdir
from os.path import isfile, join
import os
import cv2
from matplotlib import pyplot as plt
import multiprocessing as mp

def doc_anh(keyword):
    # đầu vào đường dẫn đầu ra data(thông tin ảnh), tên nhãn
    # List  ra toàn bộ file trong folder
    mypath = 'F:/forpython/dataset/anh/' + keyword
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    # In ra tổng số ảnh
    global lenLabels
    lenLabel = len(onlyfiles)
    lenLabels.append(lenLabel)
    # print(lenLabel)
    print(lenLabels)

    #
    # print(onlyfiles[:1][0])
    data=[]
    heights=[]
    for i in range(len(onlyfiles)):
        pic = cv2.imread('F:/forpython/dataset/anh/' + '/' + keyword + '/' + onlyfiles[i])
        # print(pic.shape)#It returns a tuple of the number of rows, columns, and channels (if the image is color):
        height,width,chanels = pic.shape
        # print([height,width,chanels])
        heights.append(height)
        output = [[height,width,chanels],keyword]
        data.append(output)
        # print(output)
    print(data)
    return heights

lenLabels=[]
keywords = ['Kid Face','Man Face','Oldman Face','Oldwoman Face','Woman Face']
for keyword in keywords:
    doc_anh(keyword)

# pool = mp.Pool(mp.cpu_count()-1)
# results = pool.map(doc_anh,[keyword for keyword in keywords])
# pool.close()
# print(results)


# Biểu đồ số lượng ảnh của từng nhãn
fig = plt.figure(figsize = (10, 5))

plt.title('Biểu đồ số lượng ảnh của từng nhãn\n')
plt.xlabel('Nhãn dán')
plt.ylabel('Số lượng (ảnh)')

plt.bar(keywords, lenLabels)

plt.show()


# Vẽ biểu đồ thống kê về chiều cao
cao= doc_anh('Kid Face')
plt.hist(cao,bins=6, edgecolor='black')
plt.title('Chieu cao cua kid face')
plt.show()


