import pickle


# 用来生成词库用的
data = {
    "你好":"你好你好大家好",
        "我不好":"不好就爬",
        "你们这是什么群啊":"真是害人不浅呐",
        "不好":"不好就爬",
        }
 
# 将字典保存到本地文件
with open('wordlist.pickle', 'wb') as f:
    pickle.dump(data, f)
    
# 从本地文件加载字典
with open('wordlist.pickle', 'rb') as f:
    loaded_data = pickle.load(f)


print(loaded_data)  # 输出