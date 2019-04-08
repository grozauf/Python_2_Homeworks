from argparse import ArgumentParser
import socket
import datetime
import jim
import settings


def get_response_msg():
    msg = {
        "response": 200,
        "alert": "Необязательное сообщение/уведомление"
    }
    return jim.pack(msg)


host = getattr(settings, 'HOST', '127.0.0.1')
port = getattr(settings, 'PORT', 7777)

parser = ArgumentParser()
parser.add_argument('-a', '--addr', type=str, help='Sets ip address')
parser.add_argument('-p', '--port', type=int, help='Sets port')

args = parser.parse_args()

if args.ip:
    host = args.ip
if args.port:
    port = args.port

try:
    sock = socket.socket()
    sock.bind((host, port))
    sock.listen(5)
    print(f'Server started with {host}:{port}')
    while True:
        client, address = sock.accept()
        print(f'Client detected { address }')
        request = client.recv(settings.BUFFERSIZE)
        request = jim.unpack(request)
        print('Got next request from client:', request)
        msg = get_response_msg()
        client.sendall(msg)
except KeyboardInterrupt:
    print('Server  closed')
