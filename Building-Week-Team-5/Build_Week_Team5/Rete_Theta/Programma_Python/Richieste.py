import http.client 

host = "192.168.20.20" #target ip
port = 80 #la macchina metasploitable espone un servizio sulla porta 80


try: #richiesta GET
    connection = http.client.HTTPConnection(host, port) #gestiamo la connessione verso l'host
    connection.request('GET', '/') #utiliziamo request per inviare una richiesta HTTP specificando il verbo
    response = connection.getresponse() #otteniamo la risposta dall'host
    print("GET:", response.status,) #stampa risposta
    connection.close() #chiudi la connessione
except Exception as e:
    print("Errore")

try: #richesta POST
    connection = http.client.HTTPConnection(host, port) 
    connection.request('POST', '/')
    response = connection.getresponse()
    print("POST:", response.status,)
    connection.close()
except Exception as e:
    print("Errore")

try: #richesta PUT
    connection = http.client.HTTPConnection(host, port)
    connection.request('PUT', '/')
    response = connection.getresponse()
    print("PUT:", response.status,)
    connection.close()
except Exception as e:
    print("Errore")

try: #richiesta DELETE
    connection = http.client.HTTPConnection(host, port)
    connection.request('DELETE', '/')
    response = connection.getresponse()
    print("DELETE:", response.status,)
    connection.close()
except Exception as e:
    print("Errore")