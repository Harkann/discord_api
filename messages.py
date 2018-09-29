from user import User

class Message():
    def __init__(self,json_message):
        self.id = None
        self.channel_id = None
        self.guild_id = None
        self.author = None
        self.member = None
        self.content = None
        self.timestamp = None
        self.edited_timestamp = None
        self.tts = None
        self.mention_everyone = None
        self.mentions = None
        self.mention_roles = None
        self.attachements = None
        self.embeds = None
        self.reactions = None
        self.nonce = None
        self.pinned = None
        self.type = None
        self.activity = None
        self.application = None

        self.update(json_message)



    def update(self, json_message):
        for key in json_message.keys():
            if key == "author":
                self.author = User(json_message[key])
            else:
                setattr(self, key, json_message[key])
