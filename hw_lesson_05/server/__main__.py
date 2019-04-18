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

logger = logging.getLogger('main')
handler = logging.FileHandler('server.log', encoding=settings.ENCODING)
handler_error = logging.FileHandler('server_errors.log', encoding=settings.ENCODING)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)

handler_error.setLevel(logging.ERROR)
handler_error.setFormatter(formatter)

logger.setLevel(logging.DEBUG)
logger.addHandler(handler)
logger.addHandler(handler_error)

try:
    sock = socket.socket()
    sock.bind((host, port))
    sock.listen(5)
    logger.info(f'Server started with {host}:{port}')
    while True:
        client, address = sock.accept()

        logger.info(f'Client detected {address}')

        b_request = client.recv(settings.BUFFERSIZE)
        request = jim.unpack(b_request)

        action_name = request.get('action')

        if validate_request(request):
            controller = resolve(action_name)
            if controller:
                try:
                    response = controller(request)
                    if response.get('code') != 200:
                        logger.error('Wrong request format')
                    else:
                        logger.info(f'Request is valid and processed by controller: {controller.__name__}')
                except Exception as err:
                    logger.critical(err)
                    response = make_response(
                        request, 500, 'Internal server error'
                    )
            else:
                logger.error(f'Action {action_name} does not exits')
                response = make_404(request)
        else:
            logger.error('Request is not valid')
            response = make_400(request)

        response = jim.pack(response)
        logger.info('Send response to client')
        client.sendall(response)
except KeyboardInterrupt:
    logger.info('Server  closed')
