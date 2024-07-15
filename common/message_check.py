import pickle

from common.api import message,black_check,send_img

# 读取词库、图库
with open('data/wordlist.pickle', 'rb') as f:
    wordlist = pickle.load(f)
with open('data/img.pickle', 'rb') as i:
    imglist = pickle.load(i)




def filter_heart_beat(message):
    """
    过滤心跳检测
    :param message:
    :return: bool 是否为心跳检查
    """
    if "meta_event_type" in message.keys() and message['meta_event_type'] in ["heartbeat", "lifecycle"]:
        return True
    return False


def check(word_list):
    c = 0
    # 检查是否存在发送消息以外的事件
    if word_list != None:
        if "raw_message" in word_list:
            if word_list["message_type"] != None:

                    # 违禁词检查
                    black_check(word_list)

                    # 判断是私聊还是群聊
                    global id1,id2,name
                    if word_list["message_type"] == "private":
                        id1 = "user_id="
                        id2 = str(word_list["user_id"])
                        name ="[私聊]"
                    if word_list["message_type"] == "group":
                        id1 = "group_id="
                        id2 = str(word_list["group_id"])
                        name = "[群聊]"
                    # 检查消息是否为关键词
                    if word_list["raw_message"] in wordlist:
                        c = 1
                        message(word_list,c,id1,id2,name)
                    else:
                        # 不是关键词就直接在终端输出
                        message(word_list,c,id1,id2,name)

                    # 检查是否为图库关键词
                    if word_list["raw_message"] in imglist:
                        send_img(word_list,imglist,id1,id2)
