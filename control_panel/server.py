import requests
import time

class Server():
    
    def __init__(self):
        self.url = "http://127.0.0.1:5000/"

    #             cmd ---->
    # (control panel) <-> (command center) <-> (client)
    #                                     <---- response
    # client response format: (client_id):(msg)
    
    def send(self, msg : str):
        req = requests.post(self.url, data={"msg":msg, "u":0})
    
    def recv(self):
        req = requests.get(self.url, params={"u":0})
        return req.text
    
    def send_and_recv(self, msg : str):
        self.send(msg)
        return self.recv()
