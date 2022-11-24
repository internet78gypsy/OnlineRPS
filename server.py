import socket
import threading

host = socket.gethostbyname(socket.gethostname())
port = 5000
f = 'utf-8'
players = ['', '']
names = ['', '']


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))


def cope_with_client(con_socket, addr):
    name = con_socket.recv(1024).decode(f)
    num = int(threading.current_thread().name[7:8]) - 1
    names[num] = name
    print(f"Connection from {addr}")
    print(f"{names[num]} joined the game")
    while True:
        if names[abs(num - 1)] != '':
            break
    msg = f"{names[abs(num - 1)]} joined the game"
    con_socket.send(msg.encode(f))

    while True:
        r_msg = con_socket.recv(1024).decode(f)
        if r_msg == "close":
            break
        print(f"{names[num]} played: {r_msg}")
        players[num] = r_msg
        wait = True
        result = ''
        while wait:
            if players[0] != '' and players[1] != '':
                wait = False
        if players[0] == players[1]:
            result = f'{names[abs(num - 1)]} played {players[abs(num - 1)]}. \nTie.'
        elif (players[0] == 'r' and players[1] == 's') or (players[0] == 'p' and players[1] == 'r') or (
                players[0] == 's' and players[1] == 'p'):
            if num == 0:
                result = f'{names[abs(num - 1)]} played {players[abs(num - 1)]}. \nYou win!'
            else:
                result = f'{names[abs(num - 1)]} played {players[abs(num - 1)]}. \nYou lose.'
        elif (players[0] == 's' and players[1] == 'r') or (players[0] == 'r' and players[1] == 'p') or (
                players[0] == 'p' and players[1] == 's'):
            if num == 0:
                result = f'{names[abs(num - 1)]} played {players[abs(num - 1)]}. \nYou lose.'
            else:
                result = f'{names[abs(num - 1)]} played {players[abs(num - 1)]}. \nYou win!'
        con_socket.send(result.encode(f))
        players[0] = ''
        players[1] = ''
    print(f"{names[num]} left the game.")
    names[num] = ''
    con_socket.close()


def start_server():
    while True:
        s.listen(2)
        con_socket, addr = s.accept()
        thread = threading.Thread(target=cope_with_client, args=(con_socket, addr))
        thread.start()


print(f"Server started at: {host}")
print("Waiting for players to join...")
start_server()
