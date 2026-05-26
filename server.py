import os
import socket
import threading

IP = socket.gethostbyname(socket.gethostname())
PORT = 4460
ADDR = (IP, PORT)
SIZE = 4096
FORMAT = "utf-8"
SERVER_DATA_PATH = "server_data"

if not os.path.exists(SERVER_DATA_PATH):
    os.mkdir(SERVER_DATA_PATH)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    conn.send("OK@Welcome to the File Server.".encode(FORMAT))

    while True:
        try:
            data = conn.recv(SIZE).decode(FORMAT)
            if not data:
                break

            data = data.split("@")
            cmd = data[0]

            if cmd == "LIST":
                files = os.listdir(SERVER_DATA_PATH)
                send_data = "OK@"
                if not files:
                    send_data += "The server directory is empty."
                else:
                    send_data += "\n".join(files)
                conn.send(send_data.encode(FORMAT))

            elif cmd == "UPLOAD":
                filename, content = data[1], data[2]
                with open(os.path.join(SERVER_DATA_PATH, filename), "w") as f:
                    f.write(content)
                conn.send("OK@File uploaded successfully.".encode(FORMAT))

            elif cmd == "DELETE":
                filename = data[1]
                filepath = os.path.join(SERVER_DATA_PATH, filename)
                if os.path.exists(filepath):
                    os.remove(filepath)
                    conn.send("OK@File deleted successfully.".encode(FORMAT))
                else:
                    conn.send("OK@File not found.".encode(FORMAT))

            elif cmd == "READ":
                filename = data[1]
                filepath = os.path.join(SERVER_DATA_PATH, filename)
                if os.path.exists(filepath):
                    with open(filepath, "r") as f:
                        content = f.read()
                    conn.send(f"OK@{content}".encode(FORMAT))
                else:
                    conn.send("OK@File not found.".encode(FORMAT))

            elif cmd == "STATS":
                files = os.listdir(SERVER_DATA_PATH)
                total_files = len(files)
                total_size = sum(os.path.getsize(os.path.join(SERVER_DATA_PATH, f)) for f in files)
                stats = f"Total files: {total_files}\nTotal size: {total_size} bytes"
                conn.send(f"OK@{stats}".encode(FORMAT))

            elif cmd == "LOGOUT":
                break

            elif cmd == "HELP":
                help_text = (
                    "OK@"
                    "LIST - List all server files\n"
                    "UPLOAD <filename> <content> - Upload a file\n"
                    "DELETE <filename> - Delete file\n"
                    "READ <filename> - Read file content\n"
                    "STATS - Server file statistics\n"
                    "LOGOUT - Exit\n"
                )
                conn.send(help_text.encode(FORMAT))

        except Exception as e:
            print(f"[ERROR] {e}")
            break

    print(f"[DISCONNECTED] {addr} disconnected.")
    conn.close()

def main():
    print("[STARTING] Server is starting...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"[LISTENING] Server is listening on {IP}:{PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    main()