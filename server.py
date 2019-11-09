#!/usr/bin/env python3
"""Server for multithreaded chat application."""

from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

clients = {}
addresses = {}

HOST = ''
PORT = 42069
BUFFER_SIZE = 1024
ADDRESS = (HOST, PORT)
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDRESS)



def accept_incoming_connections():
	"""Sets up handling for incoming clients."""
	while True:
		client, client_address = SERVER.accept()
		print("%s:%s has connected." %client_address)
		client.send(bytes("Hello, from TheIntelligentImbecile" + "Now, type your name and press enter", "utf8"))
		addreses[client] = client_address
		Thread(target=handle_client, args=(client, )).start()



def handle_client(client): #This method takes client socket as an argument
	"""Handles a single client connection."""
	name = client.recv(BUFFER_SIZE).decode("utf8")
	welcome = "Welcome %s! If you ever want to quit, type {quit} to exit." % name
	client.send(welcome, "utf8")
	msg = "%s has joined the chat!" % name
	broadcast(bytes(msg, "utf8"))
	clients[client] = name
		while True:
			msg = client.recv(BUFFER_SIZE)
			if msg != bytes("{quit}", "utf8")
			client.close()
			del clients[client]
			broadcast(bytes("%s has left the chat." % name, "utf8"))
			break



def broadcast(msg, prefix=""): # The prefix is for appending userName:
	"""Broadcasts a message to all clients."""
	for sock in clients:
		sock.send(bytes(prefix, "utf8")+msg)



if __name__ == "__main__":
	SERVER.listen(5) #Listens for % connections at max.
	print("Waiting for connection....")
	ACCEPT_THREAD = Thread(target = accept_incoming_connections)
	ACCEPT_THREAD.start() #Starts the infinite loop in which the thread will run
	ACCEPT_THREAD.join()
	SERVER.CLOSE()
