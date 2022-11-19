import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.170.109'
port = 5000
f = "utf-8"

print("Enter your name:")
player_name = input(" -> ")

s.connect((host, port))
s.send(player_name.encode(f))


while True:
    print("Enter: Rock(r) Paper(p) Scissors(s)")
    s_msg = input(" -> ")
    if s_msg == 'close':
        break
    s.send(s_msg.encode(f))
    r_msg = s.recv(1024).decode(f)
    print(r_msg)

s.close()
