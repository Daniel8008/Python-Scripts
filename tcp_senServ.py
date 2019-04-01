import socket
port = 5000
host = "192.168.43.31"
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#print(host)
#binding the server to a port
address = (host, port)
s.bind(address)
s.listen(5) #backlog 5 connections from client

print("<<__00__>>Listening!!")
print("\t as:{}",host)


#setting loop to listen incoming client connections

while True:
    conn, addr = s.accept()
    print("<<__00__>GOT CONN!!>>{}:{}".format(addr[0],addr[1]))
    data = conn.recv(1024)
    print("Server received",repr(data))


    filename = 'coin.json' #file to send to client 
    f = open(filename,'rb') #open the file in binary
    l = f.read(1024) #read a buffer to send 1024 bytes

    while l:
        conn.send(l)
        print("<<__Data sent('00')",repr(l))
        l=f.read(1024) #read 1024 bytes if f 1
    f.close()
    
    print("___00__")
    print("[__00__]")
    print("Done sending the data!!!!")
    conn.send(b"Thank you for connecting. Bye") #returning an ACK
    conn.close()
