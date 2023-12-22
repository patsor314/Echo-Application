import sys
import socket
import selectors
import types
from logging import Logger, getLogger

class MultiConnectionServer():
    __log: Logger = getLogger('SERVER')
    sel = selectors.DefaultSelector()

    def __init__(self, host, port):
        self.host = host
        self.port = port
        lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        lsock.bind((self.host, self.port))
        lsock.listen()
        print(f"Listening on {(self.host, self.port)}")
        lsock.setblocking(False)
        self.sel.register(lsock, selectors.EVENT_READ, data=None)

    def __accept_wrapper(self, sock):
        conn, addr = sock.accept()
        print(f"Accepted connection from {addr}")
        conn.setblocking(False)
        data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        self.sel.register(conn, events, data=data)

    def __service_connection(self, key, mask):
        sock = key.fileobj
        data = key.data
        if mask & selectors.EVENT_READ:
            recv_data = sock.recv(1024)
            if recv_data:
                data.outb += recv_data
            else:
                print(f"Closing connection to {data.addr}")
                self.sel.unregister(sock)
                sock.close()
        if mask & selectors.EVENT_WRITE:
            if data.outb:
                self.__log.info(f"Received \'{data.outb.decode()}\' from {data.addr}.")
                print(f"Echoing back \'{data.outb.decode()}\' to {data.addr}.")
                sent = sock.send(data.outb)  # Should be ready to write
                data.outb = data.outb[sent:]

    def receive_connections(self):
        try:
            while True:
                events = self.sel.select(timeout=None)
                for key, mask in events:
                    if key.data is None:
                        self.__accept_wrapper(key.fileobj)
                    else:
                        self.__service_connection(key, mask)
        except KeyboardInterrupt:
            print("Closing server")
        finally:
            self.sel.close()
