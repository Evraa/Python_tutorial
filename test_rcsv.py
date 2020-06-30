import zmq
import random,uu
from utils import serialize,deserialize
def consumer():
    context = zmq.Context()
    # recieve work
    consumer_receiver = context.socket(zmq.PULL)
    consumer_receiver.connect("tcp://127.0.0.1:5557")

    print ("recv is created")
    
    f = open("videos/vid.txt","w+")
    work = ((consumer_receiver.recv_string()))
    f.write(work)
    f.close()
    uu.decode('videos/vid.txt', 'videos/video-copy.mp4')
    print ("Receiver is done")

consumer()
