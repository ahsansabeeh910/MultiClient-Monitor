import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 4460
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 4096

def send_request(request: str) -> str:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(ADDR)
        s.recv(SIZE)  # Welcome message
        s.send(request.encode(FORMAT))
        resp = s.recv(SIZE).decode(FORMAT)
        return resp