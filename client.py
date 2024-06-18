import socket
import os
import json

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)


config = json.load(open('config.json'))
server_address = config['server_socket_path']
address = config['client_socket_path']


try:
    os.unlink(address)
except FileNotFoundError:
    pass

message = input('Enter your name: ')

sock.bind(address)

try:
    print('sending {!r}'.format(message))
    sent = sock.sendto(bytes(message, 'utf-8'), server_address)

    print('waiting to receive')
    data, server = sock.recvfrom(4096)
    strData = data.decode('utf-8')
    print('received {!r}'.format(strData))

finally:
    print('closing socket')
    sock.close()