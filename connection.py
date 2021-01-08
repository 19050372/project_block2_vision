import socket
import sys

# Port en adres van de PLC TCP/IP server
host = "192.168.0.30"
port = 2000

# Maak een TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Verbind de socket met de port van de server 
server_address = (host, port)
print('connecting to %s port %s' % server_address, file=sys.stderr)
sock.connect(server_address)

message = "test"

try:
    print('sending: "%d"' % message)
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('received "%s"' % data)

finally:
    print('closing socket')
    sock.close()