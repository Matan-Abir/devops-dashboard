import os
import socket

def show_sysinfo():
  print(f"Current Working Directory: {os.getcwd()}")
  print(f"Hostname: {socket.gethostname()}")
  print(f"Username: {os.getlogin()}")
