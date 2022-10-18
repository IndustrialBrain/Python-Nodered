import socket
import time

def connect_NODERED():
    #Cria conexão com Nodered. Python é o Cliente e Nodered o servidor.
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print('Falha ao conectar no Nodered')

    print('Conexão com Nodered OK')

    IP= "192.168.0.202"
    PORT = 8888

    #Conect no Nodered
    client.connect((IP,PORT))

    #Recebe resposta do Nodered
    msg = client.recv(1024).decode('ascii')
    data_envia="Msg Recebida= "+msg

    #Recebe resposta do Nodered
    client.send(data_envia.encode())

    #Fecha conexão
    client.close()
    return msg

while True:

    recebeMsg=connect_NODERED()
    print(recebeMsg)
    #Vai executar a cada 100ms
    time.sleep(0.1)

       
        
