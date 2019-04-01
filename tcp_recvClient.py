import socket
host=socket.gethostbyname("")
port = 5000

#creating tcp client listener sock
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port)) ##send SYN rq
s.send(b"Hello Server i need sth")

with open('received_file','wb') as f:
    print('FILE OPEN>>TO WR NOW')
    while True:
        data  = s.recv(1024) #receive some data from the server
        print('data=%s'%(data))
        if not data:
            break
        f.write(data) #write data to file
f.close()
print("File successfully received")
s.close()
print("Connection off")