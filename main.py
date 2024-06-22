import time
import json
import threading

import websocket

import messagecheck
import word_split


api_url = 'ws://127.0.0.1:3001'
bot_id = '1940975548'
auth_token = ''


def on_message(ws, message):
    message = json.loads(message)
    is_heart_beat = messagecheck.filter_heart_beat(message)
    if not is_heart_beat:

        messagecheck.check(message)

    else:
        pass


def on_error(ws, error):
    print(f'WebSocket 错误: {error}')


def on_close(ws, close_status):
    print(f'WebSocket 连接已关闭: {close_status}')


def on_open(ws):
    def run():
        while True:
            time.sleep(30)  # 保持连接

    thread = threading.Thread(target=run)
    thread.start()


if __name__ == '__main__':
    header = {
        'Authorization': f'Bearer {auth_token}',
        'bot_id': bot_id
    }
    ws = websocket.WebSocketApp(api_url,
                                header=header,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
