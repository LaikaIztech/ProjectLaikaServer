import socket
import time
if __name__ == "__main__":
    s = socket.socket()
    s.bind(('0.0.0.0', 8080))
    bytes_ = bytes()
    s.listen(0)
    while True:
        client, addr = s.accept()
        while True:
            content = client.recv(1024000000)
            if len(content) > 0:
                print("hit")
                with open(f"capture{time.time()}.jpeg", "wb+") as file_:
                    file_.write(content)
        client.close()
