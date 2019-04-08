from argparse import ArgumentParser
import socket
import datetime
import jim
import settings


def get_presence_msg():
    time = datetime.datetime.now()
    msg = {
        "action": "presence",
        "time": time.isoformat(),
        "type": "status",
        "user": {
                "account_name":  "anonim",
                "status":      "Yep, I am here!"
        }
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
    sock.connect((host, port))
    print(f'Client started with {host}:{port}')
    while True:
        msg = get_presence_msg()
        sock.sendall(msg)
        response = sock.recv(settings.BUFFERSIZE)
        response = jim.unpack(response)
        print('Got next response from server:', response)

except KeyboardInterrupt:
    print('Client  closed')



