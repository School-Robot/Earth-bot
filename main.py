import socket
import messagecheck
import word_split

# 创建TCP socket
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 设置端口复用，让程序能够立即重新启动而不需要等待操作系统释放端口
tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 绑定端口
tcp_server_socket.bind(('', 8080))

# 设置为监听模式
tcp_server_socket.listen(1)

while True:
    # 接受一个新的连接
    client_socket, addr = tcp_server_socket.accept()

    # 接收数据，最多1024字节
    message = client_socket.recv(4096).decode()

    # 分离参数
    word_list = word_split.split(message)
    
    # 校验信息并执行
    messagecheck.check(word_list)

    # 关闭与客户端的连接
    client_socket.close()