from argparse import ArgumentParser
import socket
import datetime
import jim
import settings
from routes import resolve, get_server_routes
from protocol import (
    validate_request, make_response,
    make_400, make_404
)


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

if args.addr:
    host = args.addr
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
        b_request = client.recv(settings.BUFFERSIZE)
        request = jim.unpack(b_request)

        action_name = request.get('action')

        if validate_request(request):
            controller = resolve(action_name)
            if controller:
                try:
                    response = controller(request)
                except Exception as err:
                    print(err)
                    response = make_response(
                        request, 500, 'Internal server error'
                    )
            else:
                print('Action { action_name } does not exits')
                response = make_404(request)
        else:
            print('Request is not valid')
            response = make_400(request)

        response = jim.pack(response)
        client.sendall(response)
except KeyboardInterrupt:
    print('Server  closed')
