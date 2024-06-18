import socket
import os
import json
from faker import Faker

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

config = json.load(open('config.json'))
server_address = config['server_socket_path']
fake = Faker()

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

print('starting up on {}'.format(server_address))

sock.bind(server_address)

while True:
    print('\nwaiting to receive message')

    data, address = sock.recvfrom(4096)

    print('received {} bytes from {}'.format(len(data), address))
    print(data)

    if data:
        dataStr = data.decode('utf-8')
        message = 'Hello {}! My name is {}'.format(dataStr, fake.name())
        sent = sock.sendto(bytes(message, 'utf-8'), address)
        print('sent {} bytes back to {}'.format(sent, address))