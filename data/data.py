import pickle


# 词库
data = {
        "你好":"你好你好大家好",
        "我不好":"不好就爬",
        "你们这是什么群啊":"真是害人不浅呐",
        "不好":"不好就爬",
        "笑死我了":"别死"
        }

# 图库
img = {
    "难吗":"https://gchat.qpic.cn/gchatpic_new/2066045898/595564638-2168361552-C68E41C9B5C9866DC3429F4AAF347179/0"
}

# 将字典保存到本地文件
def save(data,img):
    with open('wordlist.pickle', 'wb') as f:
        pickle.dump(data, f)
    with open('img.pickle', 'wb') as f:
        pickle.dump(img, f)
    
# 从本地文件加载字典
def load(data,img):
    with open('wordlist.pickle', 'rb') as f:
        loaded_data = pickle.load(f)
    with open('img.pickle', 'rb') as i:
        loaded_img = pickle.load(i)
    load22 = str(loaded_img)+str(loaded_data)
    return load22


save(data,img)
print(load(data,img))
