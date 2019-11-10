#!/usr/bin/env python3
""" GUI Client for chat application"""

from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter


def receive():
    """Handles receiving of messages."""
    while True:
        try:
            msg = client_socket.recv(BUFFER_SIZE).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        except OSError:  # Can Happen when client has left the chat
            break


def send(event=None):  # even passed using binders.
    msg = my_msg.get()
    my_msg.set("")  # clear the input field.
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()
        top.quit()


def on_closing(event=None):
    """This function is called when the window is closed."""
    my_msg.set("{quit}")
    send()


top = tkinter.Tk()
top.title("Cipher_Chat")

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()
my_msg.set("Type Your messages Here:")
scrollbar = tkinter.Scrollbar(messages_frame)  # To enable to see past messages.
msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack()

top.protocol("WM_DELETE_WINDOW", on_closing)

HOST = input('Enter Host: ')
PORT = input('Enter port: ')
if not PORT:
    PORT = 42069
else:
    PORT = int(PORT)

BUFFER_SIZE = 1024
ADDRESS = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDRESS)
receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()
