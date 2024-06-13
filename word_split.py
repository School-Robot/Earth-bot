import json


def split(message):
    # 截取json部分
    word_split = []
    a=-1
    for i in range(len(message)):
        if message[i] == "{" and a == -1:
            a = i
            break
    word = message[a:len(message)]
    # 解析json，如异常则抛出
    try:
        word_split = json.loads(word)
        return word_split
    except json.decoder.JSONDecodeError as e:
        print(f"发生JSON解析错误：{e}")
        return None
