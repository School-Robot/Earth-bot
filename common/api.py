import requests
import pickle

# 发送消息的接口
send="http://127.0.0.1:3000/send_msg?"

# 群组禁言接口
ban = "http://127.0.0.1:3000/set_group_ban?"

# 违禁词名单
blacklist = ["老子他妈"]

# 读取词库、图库
with open('data/wordlist.pickle', 'rb') as f:
    wordlist = pickle.load(f)
with open('data/img.pickle', 'rb') as i:
    imglist = pickle.load(i)


def message(word_list,c,id1,id2,name):
    if c:
        send_url = send + id1 + id2 + "&message=" + wordlist[word_list["raw_message"]]
        requests.get(send_url)
    message = name + id2 + word_list["sender"]["nickname"] + ":" + word_list["raw_message"] + "\n"
    print(message)
    f = open("data/message/"+name+id2+".txt", "a", encoding="utf-8")
    f.write(message)


def black_check(word_list):
    for i in blacklist:
        if i in word_list["raw_message"]:
            send_url = send + "group_id=" + str(word_list["group_id"]) + "&message=触发违禁词"
            requests.get(send_url)
            ban_url = ban + "group_id=" + str(word_list["group_id"]) + "&user_id=" + str(
                word_list["user_id"]) + "&duration=3600"
            requests.get(ban_url)
            message(word_list)
            return None


def send_img(word_list,imglist,id1,id2):
    img_url = imglist[word_list["raw_message"]]
    img_cq_code = f"[CQ:image,file={img_url}]"
    send_url = send + id1 + id2 + "&message=" + img_cq_code
    requests.get(send_url)
