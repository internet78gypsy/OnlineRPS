import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.170.109'
port = 5000
f = "utf-8"

print("Enter your name:")
player_name = input(" -> ")

s.connect((host, port))
s.send(player_name.encode(f))
print("Waiting for opponent to join...")
msg = s.recv(1024).decode(f)
print(msg)


while True:

    print("\nEnter: Rock(r) Paper(p) Scissors(s) Exit(close)")
    s_msg = input(" -> ")
    while True:
        if s_msg == 'r' or s_msg == 's' or s_msg == 'p' or s_msg == 'close':
            break
        s_msg = input(" -> ")
    if s_msg == 'close':
        s.send(s_msg.encode(f))
        break
    s.send(s_msg.encode(f))
    print(f"Waiting for opponent to play...")
    r_msg = s.recv(1024).decode(f)
    print(r_msg)

s.close()
