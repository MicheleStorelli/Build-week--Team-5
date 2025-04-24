import socket

SRV_ADDR = "192.168.10.10" #IP locale della macchina server
SRV_PORT = 44444 #porta su cui il server ascolterà

#creiamo il socket in ascolto
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
#colleghiamo il socket all'IP e alla porta in ascolto
s.bind((SRV_ADDR, SRV_PORT))
#mettiamo il server in ascolto
s.listen(1)
print("Server avviato")
#accettiamo la connessione con il client che tenterà di connetersi
connection, address = s.accept() 
print('Connessio avviata da:', address)

#ciclo per ricevere dati finché non riceve il messaggio 'end\n'
while True:
    data = connection.recv(1024)
    if not data : break
    message = data.decode('utf-8')
    print("Messaggio ricevuto:", message.strip())
    if message.strip() == "end":
        print("Messaggio di chiusura ricevuto. Fine connessione.")
        break
    connection.sendall(b"Messaggio ricevuto \n")
connection.close()

    
    