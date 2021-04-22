from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import requests

def taianh(keyword):

    PATH = 'F:/forpython/dataset/chromedriver.exe'

    # 1 Khai báo biến browser(đại diện cho trình duyệt)
    driver = webdriver.Chrome(PATH)
    # vào trang gg
    driver.get('https://www.google.com')

    # Chọn cái element Search Box (lấy selector - vị trí của element)
    search_box = driver.find_element_by_name('q')
    # ghi vào search box là kid face
    search_box.send_keys(keyword)
    # ghi vào search nút enter
    search_box.send_keys(Keys.RETURN)

    # Image Button
    image_button = driver.find_element_by_class_name('hide-focus-ring')
    image_button.click()

    # cuộn xuống hết
    for i in range(5):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        #click vào hiện tất cả
    showfullimage = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[4]/div[2]/input')
    showfullimage.click()
    time.sleep(5)

    #cuộn xuống dưới tiếp
    for i in range(7):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)


    # Nhắm đến tất cả các thẻ img (in ra 1 list selenium items)
    images = driver.find_elements_by_tag_name('img')
    # images = driver.find_elements_by_xpath('//img')
    print(len(images))
    print(images)

    # Lấy giá trị của thuộc tính src trong thẻ img - cái đường link để tải về
    images = [image.get_attribute('src') for image in images]
    print(images[:1])

    #tạo thư mục để lưu ảnh
    try:
        path = os.getcwd() # đưa đến địa chỉ thư mục đang đứng
        path = os.path.join(path,'anh') # đổi đường dẫn mới =  thêm path ở trên với 1 tên folder ảnh nữa
        os.mkdir(path) # tạo ra cái folder ở trên
    except:
        pass
    try:
        path = os.path.join(path, keyword)
        os.mkdir(path) # tạo ra cái folder ở trên
    except FileExistsError as e:
        print(e)
# os.makedirs(path)
# os.makedirs(path, exist_ok = True)
    # lưu ảnh
    counter = 0
    for image in images:
        keyword_arr = keyword.split()
        save_as = os.path.join(path, keyword_arr[0] + '_' + keyword_arr[1] + '_' + str(counter)+ '.jpg') # Kid Face -> Kid_Face_0
        print(save_as)
        print(image)

        if image != None:
            if "base64" in image:
                continue
            result = requests.get(image)
            with open(save_as, 'wb') as f:
                f.write(result.content)
            counter += 1

keywords = ['Kid Face','Man Face','Oldman Face','Oldwoman Face','Woman Face']
for keyword in keywords:
    taianh(keyword)

