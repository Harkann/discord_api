import json as js
from guilds import Guild
from messages import Message
from termcolor import cprint

def parse_dispatch(d_type, payload, bot):
    cprint("| t:{} with".format(d_type), "green")
    if d_type == "READY":
        # useless for now
        version = payload["v"]
        user = payload["user"]
        guilds = payload["guilds"]
        pv_chans = payload["private_channels"]
        bot.session_id = payload["session_id"]
        _trace = payload["_trace"]

        # update bot attributes
        bot.user.update(user)
        for g in guilds:
            bot.guilds.append(Guild(g))

        # printing for debug purposes
        if bot.debug is True:
            cprint("| User", "green")
            for key in user:
                cprint("|| {}:{}".format(key, user[key]), "green")
            cprint("|| --", "green")
            cprint("| Guilds", "green")
            for g in guilds:
                for key in g:
                    cprint("|| {}:{}".format(key, g[key]), "green")
                cprint("|| --", "green")

    elif d_type == "GUILD_CREATE":
        found = False  # if the guild is in the guilds already registred

        # update bot attributes
        for g in bot.guilds:
            if payload["id"] == g.id:
                g.update(payload)
                found = True
        if not found:
            bot.guilds.append(Guild(payload))

        # printing for debug purposes
        for key in payload:
            cprint("| {}:{}".format(key, payload[key]), "green")

    elif d_type == "PRESENCE_UPDATE":
        pass

    elif d_type == "MESSAGE_CREATE":
        found = False

        for g in bot.guilds:
            if payload["guild_id"] == g.id:
                g.insert_message(payload)
                found = True
        if not found:
            print("UNKNOWN_GUILD")
        # printing for debug purposes
        for key in payload:
            cprint("| {}:{}".format(key, payload[key]), "green")
        bot.on_message_create(Message(payload))



    elif d_type == "MESSAGE_UPDATE":
        pass

def parse_response(response, bot):
    response = js.loads(response)
    op = response["op"]
    if op == 0:
        # RECEIVE only
        t = response["t"]
        s = response["s"]
        d = response["d"]
        cprint("Dispatch with s:{}".format(s), "green")
        parse_dispatch(t,d, bot)
        return s
    elif op == 1:
        # SEND / RECEIVE
        cprint("Heartbeat with", "red")
    elif op == 2:
        # SEND only
        cprint("Identify with", "red")
    elif op == 3:
        # SEND only
        cprint("Status Update with", "red")
    elif op == 4:
        # SEND only
        cprint("Voice Status Update with", "red")
    elif op == 5:
        # SEND only
        cprint("Voice Server Ping with", "red")
    elif op == 6:
        # SEND only
        cprint("Resume with", "red")
    elif op == 7:
        # RECEIVE only
        cprint("Reconnect with", "red")
    elif op == 8:
        # SEND only
        cprint("Request Guild Members with", "red")
    elif op == 9:
        # RECEIVE only
        cprint("Invalid Session with", "red")
    elif op == 10:
        # RECEIVE only
        t = response["t"]
        s = response["s"]
        d = response["d"]
        heartbeat_interval = d["heartbeat_interval"]
        _trace = d["_trace"]
        cprint("Hello with", "yellow")
        cprint("| t: {}, s: {}".format(t,s), "yellow")
        cprint("| heartbeat_interval: {}".format(heartbeat_interval), "yellow")
        cprint("| _trace: {}".format(_trace), "yellow")
        bot.sequence = s
        bot.heartbeat_interval = heartbeat_interval
    elif op == 11:
        # RECEIVE only
        cprint("Heartbeat ACK with", "red")
    else:
        print("OP code not supported")
        pass
