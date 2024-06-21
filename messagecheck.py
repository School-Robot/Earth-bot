import requests
import pickle

# 发送消息的接口
send="http://127.0.0.1:3000/send_msg?"

# 撤回消息接口
delete = "http://127.0.0.1:3000/delete_msg?"

# 群组禁言接口

ban = "http://127.0.0.1:3000/set_group_ban?"

# 读取词库
with open('wordlist.pickle', 'rb') as f:
    wordlist = pickle.load(f)

# 违禁词名单
blacklist = ["老子他妈","你妈","尼玛","傻逼","煞笔"]


def private_message(word_list):
    message = "[私聊]" + word_list["sender"]["nickname"] + ":" + word_list["raw_message"] + "\n"
    print(message)
    f = open("message.txt", "a", encoding="utf-8")
    f.write(message)


def group_message(word_list):
    message = "[群聊" + str(word_list["group_id"]) + "]" + word_list["sender"]["nickname"] + ":" + word_list[
        "raw_message"] + "\n"
    print(message)
    f = open("message.txt", "a", encoding="utf-8")
    f.write(message)


def check(word_list):
    # 检查是否存在发送消息以外的事件
    if word_list != None:
        if "raw_message" in word_list:
            if word_list["message_type"] != None:
                    # 违禁词检查
                    for i in blacklist:
                        if i in word_list["raw_message"]:
                            delete_url = delete + "message_id=" + str(word_list["message_id"])
                            requests.get(delete_url)
                            send_url = send + "group_id=" + str(word_list["group_id"]) + "&message=触发违禁词"
                            requests.get(send_url)
                            ban_url = ban + "group_id=" + str(word_list["group_id"]) + "&user_id=" + str(word_list["user_id"]) + "&duration=3600"
                            requests.get(ban_url)
                            group_message(word_list)
                    # 检查消息是否为关键词
                    if word_list["raw_message"] in wordlist:
                        # 判断是私聊还是群聊
                        if word_list["message_type"] == "private":
                            send_url = send + "user_id=" + str(word_list["user_id"]) + "&message=" + wordlist[word_list["raw_message"]]
                            requests.get(send_url)
                            private_message(word_list)
                        if word_list["message_type"] == "group":
                            send_url = send + "group_id=" + str(word_list["group_id"]) + "&message=" + wordlist[word_list["raw_message"]]
                            requests.get(send_url)
                            group_message(word_list)


                    else:
                        # 不是关键词就直接在终端输出不做其余处理
                        if word_list["message_type"] == "private":
                            private_message(word_list)
                        if word_list["message_type"] == "group":
                            group_message(word_list)