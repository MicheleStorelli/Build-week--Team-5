import socket

target = "192.168.20.20" #target ip
#range di porte da scannerizzare 
lowport = 1
hightport = 500

#andiamo a creare un dizionario che includa le porte aperte, e che ci dica a grandi linee quanto sia sicuro che la porta sia aperta
porte_note = {
    21: ("FTP", "Non Sicura"),
    22: ("SSH", "Sicura"),
    23: ("Telnet", "Non Sicura"),
    25: ("SMTP", "Rischiosa"),
    53: ("DNS", "Sicura se configurata"),
    80: ("HTTP", "Non Sicura"),
    111: ("RPCBind", "Rischiosa"),
    139: ("NetBios", "Rischisa"),
    445: ("SMB", "Rischiosa"),
}

#inizio scansione porte
print(f"\n🔍 Scannerizzando {target} dalla porta {lowport} alla porta {hightport}...\n")

#ciclo che scansiona ogni porta nel range definito
for port in range(lowport, hightport + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status = s.connect_ex((target, port))
    #se la porta è aperta
    if status == 0:
        #cerca il nome del servizio e il livello di sicurezza, se è tra quelli noti
        servizio, sicurezza = porte_note.get(port)
        print(f"Porta {port} APERTA - Servizio: {servizio} - Sicurezza: {sicurezza}")
    s.close()