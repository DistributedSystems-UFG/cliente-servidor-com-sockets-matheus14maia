from socket import *
from constCS import *
import pickle

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
(conn, addr) = s.accept()  # returns new socket and addr. client
while True:  # forever
    msg = conn.recv(1024)  # receive data from client
    if not msg: break  # stop if client stopped

    data = pickle.loads(msg)
    print("Requisição recebida:", data)

    op = data.get("OP")
    v1 = data.get("V1")
    v2 = data.get("V2")

    res = 0
    status = "OK"

    if op == "sum":
        res = v1 + v2
    elif op == "sub":
        res = v1 - v2
    elif op == "mul":
        res = v1 * v2
    elif op == "div":
        if v2 == 0:
            status = "NOK"
            res = "Erro: Divisão por zero não é permitida."
        else:
            res = v1 / v2
    else:
        status = "NOK"
        res = "Operação inválida ou não existente."

    # Monta a resposta
    data = {"STATUS": status, "RES": res}
    msg = pickle.dumps(data)
    conn.send(msg)

conn.close()  # close the connection
