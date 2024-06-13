import pickle


# 用来生成词库用的
data = {
    "你好":"你好你好大家好",
        "我不好":"不好就爬",
        "这是什么群":"这是我们学校的CTF校队招新群",
        "CTF是什么":"CTF（Capture The Flag）中文一般译作夺旗赛，在网络安全领域中指的是网络安全技术人员之间进行技术竞技的一种比赛形式。--源自百度百科",
        "CTF是学什么的":"CTF主要分为Web、Misc、Crypto、Reverse、Pwn。Web顾名思义主攻Web安全，主要研究网站的渗透，Misc则是杂项，主要涵盖隐写、社工之类的杂七杂八的东西，Crypto是密码学，主要学习古典密码、现代密码等各种加密算法，Reverse是逆向工程,主要学习程序逆向破解，Pwn则是二进制安全，主要研究各种漏洞的利用。",
        "你们这是什么群啊":"真是害人不浅呐",
        "不好":"不好就爬",
        "老子他妈":"触发违禁词"
        }
 
# 将字典保存到本地文件
with open('wordlist.pickle', 'wb') as f:
    pickle.dump(data, f)
    
# 从本地文件加载字典
with open('wordlist.pickle', 'rb') as f:
    loaded_data = pickle.load(f)


print(loaded_data)  # 输出