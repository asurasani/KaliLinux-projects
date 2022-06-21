import socket

target_host = "www.google.com"
target_port = 80


#create socket object
#AF_INET means standard IPv4 address/hostname
#SOCK_STREAM means this is a TCP client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect the client to the TCPserver 
client.connect((target_host,target_port))

#send_some data as bytes
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#recieve some data and print response
response = client.recv(4096)

print(response.decode())
client.close()