from socket  import *
from constCS import *
import pickle

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT)) # connect to server (block until accepted)

op = input("Operação a invocar (sum, sub, mul, div): ")
v1 = int(input("Entre com o 1º operando: "))
v2 = int(input("Entre com o 2º operando: "))

data = {"OP": op, "V1": v1, "V2": v2}
msg = pickle.dumps(data)
s.send(msg)  # send data packet

msg = s.recv(1024)     # receive the response
data = pickle.loads(msg)

if data["STATUS"] == "OK":
  print("Resultado: ", data["RES"])
else: # Se o STATUS for "NOK"
  print("Ocorreu um erro no servidor.")
  print("Motivo: ", data["RES"])

s.close()               # close the connection
