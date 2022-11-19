import socket
import threading

host = '192.168.170.109'
port = 5000
f = 'utf-8'
players = ['', '']

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))


def cope_with_client(con_socket, addr):
    name = con_socket.recv(1024).decode(f)
    print(f"Player {name} connected the server")
    num = int(threading.current_thread().name[7:8]) - 1
    while True:
        r_msg = con_socket.recv(1024).decode(f)
        if r_msg == "close":
            break
        print(f"Received: {r_msg}")
        players[num] = r_msg
        print(players)
        wait = True
        while wait:
            if players[0] != '' and players[1] != '':
                wait = False
        if players[0] == players[1]:
            result = 'Tie!'
        elif (players[0] == 'r' and players[1] == 's') or (players[0] == 'p' and players[1] == 'r') or (
                players[0] == 's' and players[1] == 'p'):
            if num == 0:
                result = 'You win!'
            else:
                result = 'You lose.'
        elif (players[0] == 's' and players[1] == 'r') or (players[0] == 'r' and players[1] == 'p') or (
                players[0] == 'p' and players[1] == 's'):
            if num == 0:
                result = 'You lose.'
            else:
                result = 'You win!'
        con_socket.send(result.encode(f))
    print(f"Player {name} left the game.")
    con_socket.close()


def start_server():
    s.listen(2)
    while True:
        con_socket, addr = s.accept()
        thread = threading.Thread(target=cope_with_client, args=(con_socket, addr))
        thread.start()


start_server()
