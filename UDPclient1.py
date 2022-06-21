import socket

target_host = "127.0.0.1"
target_port = 9997


#create socket object
#AF_INET means standard IPv4 address/hostname
#SOCK_STREAM means this is a TCP client
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#send_some data as bytes
client.send(b"AAABBBCCC", (target_host, target_port))

#recieve some data and print response
data, addr = client.recvfrom(4096)

print(data.decode())
client.close()