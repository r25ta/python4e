import socket
import time

#DECLARAÇÃO DAS CONSTANTES DE CONEXAO
#HOST = "data.pr4e.org"
HOST = "f1-grandprix.com"
PORT = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST,PORT))

#A STRING DE CONEXAO DEVE SER EM BYTES POR ISSO NO FINAL DA LINHA TEM O METODO ENCODE() TRANSFORMA STRING EM BYTES
#cmd = "GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n".encode()
cmd = "GET http://www.f1-grandprix.com/wp-content/uploads/wppa/209.jpg?ver=6 HTTP/1.0\r\n\r\n".encode()
mysock.sendall(cmd)

count=0
picture =b""

while True:
    #CADA INTERACAO RETORNAR 1 MB DE INFORMAÇÕES
    data = mysock.recv(1048576)
    if len(data) < 1:
        break;
    #TIME SLEEP DE 1/4 DE SEGUNDO
    time.sleep(0.25)
    
    #CONTAGEM DE INTERAÇÕES(PAGINAÇÕES)
    count += 1
    #EXIBE A QTDE DE DADOS RETORNADOS POR INTERAÇÃO
    print(len(data),count)
    
    #ARMAZENANDO A INFORMAÇÃO EM MEMORIA
    picture = picture + data

#FINALIZOU A CAPTURA DE INFORMAÇÃO    
mysock.close()

#LOCALIZA O FINAL DO HEADER
pos = picture.find(b"\r\n\r\n")
#EXIBE O TAMANHO DO HEADER EM BYTES
print("\nHeader length",pos)
#EXIBE O CONTEUDO DO HEADER O METODO DECODE() TRANSFORMA BYTE EM STRING
#O CONTENT-TYPE DESSE HEADER É IMAGE/JPEG, SIGNIFICA QUE TEMOS UMA IMAGEM
print("\n",picture[:pos].decode())

#FORMATA O CONTEUDO DA IMAGEM
picture = picture[pos+4:]
#ABRE UM NOVO ARQUIVO COM OS ATRIBUTOS DE ESCRITA E LEITURA
#NAME_IMG = "stuff.jpg"
NAME_IMG = "brabhan.jpg"
fhand = open(NAME_IMG,"wb")
#GRAVA AS INFORMAÇÕES NO ARQUIVO
fhand.write(picture)
#FECHA O ARQUIVO
fhand.close()
     