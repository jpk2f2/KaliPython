import socket

target_host = "127.0.0.1"
target_port = 80
#for simpleUdpSerever
#target_host = "0.0.0.0"
#target_port = 9000

#create a socket object
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#uncomment below if no server
#client.bind((target_host, target_port))

#send some data
client.sendto("AAABBBCCC",(target_host,target_port))

#recieve some data              
data, addr = client.recvfrom(4096)

print data
