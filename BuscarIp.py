import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print("El nombre del ordenado es : " + hostname)
print("La dirección ip del ordenador es : " + ip)
