#COMUNICAÇÃO VIA SOCKET
import socket
0
mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#ESTABELCE A PORTA AO QUAL VAMOS NOS CONECTAR
mysocket.connect(('data.pr4e.org',80))
#PROTOCOLO DE CONEXAO E  NO FINAL UMA LINHA EM BRANCO APOS O HEADER
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()

mysocket.send(cmd)
while True:
    #RECEBE A INFORMAÇÃO PAGINADO POR 250 CARACTERES POR VEZ ATÉ FINALIZAR
    data = mysocket.recv(250)
    if len(data) < 1:
        break
    
    print(data.decode(),end='')
    
mysocket.close()