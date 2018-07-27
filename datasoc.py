import SocketServer

HOST, PORT = "localhost", 9999


class MyTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())


print("Creating the server, binding to localhost on port", PORT)
server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)


def activate_server():
    server.serve_forever()


def stop_server():
    print("Shutting the server on port", PORT)
    server.shutdown()


if __name__ == "__main__":
    activate_server()
