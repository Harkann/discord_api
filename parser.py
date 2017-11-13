import json as js
from termcolor import cprint

def parse_dispatch(d_type, payload):
    cprint("| t:{} with".format(d_type), "green")
    if d_type == "READY":
        pass
    elif d_type == "GUILD_CREATE":
        pass
    elif d_type == "PRESENCE_UPDATE":
        pass
        
def parse_response(response):
    response = js.loads(response)

    op = response["op"]
    if op == 0:
        t = response["t"]
        s = response["s"]
        d = response["d"]
        cprint("Dispatch with s:{}".format(s), "green")
        parse_dispatch(t,d)
        return s
    elif op == 1:
        cprint("Heartbeat with", "red")
    elif op == 2:
        cprint("Identify with", "red")
    elif op == 3:
        cprint("Status Update with", "red")
    elif op == 4:
        cprint("Voice Status Update with", "red")
    elif op == 5:
        cprint("Voice Server Ping with", "red")
    elif op == 6:
        cprint("Resume with", "red")
    elif op == 7:
        cprint("Reconnect with", "red")
    elif op == 8:
        cprint("Request Guild Members with", "red")
    elif op == 9:
        cprint("Invalid Session with", "red")
    elif op == 10:
        t = response["t"]
        s = response["s"]
        d = response["d"]
        heartbeat_interval = d["heartbeat_interval"]
        cprint("Hello with", "yellow")
        cprint("| t:{}, s:{}".format(t,s), "yellow")
        cprint("| heartbeat_interval:{}".format(heartbeat_interval), "yellow")
        return {"s": s, "heartbeat_interval": heartbeat_interval}
    elif op == 11:
        t = response["t"]
        s = response["s"]
        d = response["d"]
        cprint("Heartbeat ACK with", "red")
        cprint("| t:{}, s:{}, d:{}".format(t,s,d), "red")
        return s
    else:
        print("OP code not supported")
        pass
