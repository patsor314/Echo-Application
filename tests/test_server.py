import unittest
from unittest.mock import patch, ANY, call
import types

import selectors

from socket_services.MultiConnectionServer import MultiConnectionServer

class ServerTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_register = patch('socket_services.MultiConnectionServer.selectors.DefaultSelector.register').start()

        self.mock_socket = patch('socket_services.MultiConnectionServer.socket.socket').start()
        self.mock_setblocking = self.mock_socket.return_value.setblocking
        self.mock_accept = self.mock_socket.return_value.accept
        self.mock_bind = self.mock_socket.return_value.bind
        self.mock_listen = self.mock_socket.return_value.listen

        self.test_server = MultiConnectionServer('127.0.0.1', 123)

        self.mock_send = patch('socket_services.MultiConnectionServer.socket.socket.send').start()
        self.mock_recv = patch('socket_services.MultiConnectionServer.socket.socket.recv').start()

        self.mock_data = types.SimpleNamespace(addr=('127.0.0.1', ANY), inb=b'', outb=b'')
        self.mock_write_data = types.SimpleNamespace(addr=('127.0.0.1', ANY), inb=b'', outb=b'test')


    def test_init_server_success(self):
        self.mock_socket.reset_mock()
        self.mock_register.reset_mock()

        test_init_server = MultiConnectionServer('127.0.0.2', 123)
        self.assertEqual(test_init_server.host, '127.0.0.2')
        self.assertEqual(test_init_server.port, 123)

        self.mock_socket.assert_called_once()
        self.mock_bind.assert_called_once_with(('127.0.0.2', 123))
        self.mock_listen.assert_called_once()
        self.mock_setblocking.assert_called_once_with(False)
        self.mock_register.assert_called_once_with(ANY, 1, data=None)

    @patch('socket_services.MultiConnectionServer.socket.socket.setblocking')
    @patch('socket_services.MultiConnectionServer.socket.socket.accept')
    def test_accept_wrapper_success(self, mock_accept, mock_blocking):
        mock_accept.return_value = (self.mock_socket, ('127.0.0.1', ANY))
        register_calls = [call(ANY, 1, data=None), call(ANY, 3, data=self.mock_data)]

        self.test_server._MultiConnectionServer__accept_wrapper(self.mock_socket)

        mock_accept.assert_called_once()
        self.mock_setblocking.assert_called_once_with(False)
        mock_blocking.assert_called_once_with(False)
        self.mock_register.assert_has_calls(register_calls)

    def test_service_connection_successful_echo(self):
        mock_key = selectors.SelectorKey(fileobj=self.mock_socket, fd=5, events=3, data=self.mock_data)
        mask = 3
        self.mock_recv.return_value = b'test'
        self.mock_send.return_value = len(b'test')

        self.test_server._MultiConnectionServer__service_connection(mock_key, mask)

        self.mock_recv.assert_called_once()
        self.mock_send.assert_called_once_with(b'test')

    @patch('socket_services.MultiConnectionServer.socket.socket.close')
    @patch('socket_services.MultiConnectionServer.selectors.DefaultSelector.unregister')
    def test_service_connection_successful_client_connection(self, mock_unregister, mock_close):
        mock_key = selectors.SelectorKey(fileobj=self.mock_socket, fd=5, events=3, data=self.mock_data)
        mask = 3
        self.mock_recv.return_value = b''

        self.test_server._MultiConnectionServer__service_connection(mock_key, mask)

        self.mock_recv.assert_called_once()
        mock_unregister.assert_called_once()
        mock_close.assert_called_once()
        self.mock_send.assert_not_called()


    def tearDown(self) -> None:
        self.mock_register.stop()
        self.mock_socket.stop()
        self.mock_send.stop()
        self.mock_recv.stop()
