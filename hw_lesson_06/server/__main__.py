from argparse import ArgumentParser
import socket
import datetime
import logging
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

handler = logging.FileHandler('main.log', encoding=settings.ENCODING)
error_handler = logging.FileHandler('error.log', encoding=settings.ENCODING)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        handler,
        error_handler,
        logging.StreamHandler(),
    ]
)

def main():
    try:
        sock = socket.socket()
        sock.bind((host, port))
        sock.listen(5)
        logging.info(f'Server started with {host}:{port}')
        while True:
            client, address = sock.accept()

            logging.info(f'Client detected {address}')

            b_request = client.recv(settings.BUFFERSIZE)
            request = jim.unpack(b_request)

            action_name = request.get('action')

            if validate_request(request):
                controller = resolve(action_name)
                if controller:
                    try:
                        response = controller(request)
                        if response.get('code') != 200:
                            logging.error('Wrong request format')
                        else:
                            logging.info(f'Request is valid and processed by controller')
                    except Exception as err:
                        logging.critical(err)
                        response = make_response(
                            request, 500, 'Internal server error'
                        )
                else:
                    logging.error(f'Action {action_name} does not exits')
                    response = make_404(request)
            else:
                logging.error('Request is not valid')
                response = make_400(request)

            response = jim.pack(response)
            logging.info('Send response to client')
            client.sendall(response)
    except KeyboardInterrupt:
        logging.info('Server  closed')


main()
