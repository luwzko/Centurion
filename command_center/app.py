from flask import *
from werkzeug.wrappers import response

app = Flask(__name__)

# index 0: control_panel
# index 1: client
msgs = ["", "Client"]
read_states = [False, False]

@app.route("/", methods=["GET"])
def index_get():
    global msgs
    global read_states
    u = request.args.get("u")
                    #protection from invalid indexes
    if u == None or (u := int(u)) not in [0,1]:
        return ""
    else:
        if read_states[1]:
            read_states = [False, False]
            msgs = [False, False]
        return Response(response=msgs[not u])

@app.route("/", methods=["POST"])
def index_post():
    global msgs
    global read_states
    try:
        msgs[int(request.form["u"])] = request.form["msg"]    
    except IndexError:
        pass
    return ""

if __name__ == "__main__":
    app.run()