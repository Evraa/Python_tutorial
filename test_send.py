import time
import zmq
import os
import speech_recognition as sr
from utils import serialize,deserialize
import uu
def producer():
    context = zmq.Context()
    zmq_socket = context.socket(zmq.PUSH)
    zmq_socket.bind("tcp://127.0.0.1:5557")
    print ("Sender is created")
    fileName = 'videos/Bolna.txt'
    uu.encode('videos/Bolna.mp4', fileName)
    f = open(fileName,"r")
    content = f.read()
    #content = str(content)
    #content =  content.decode()
    zmq_socket.send_string(content)
    print("sender is done")
producer()