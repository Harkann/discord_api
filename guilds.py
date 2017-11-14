from user import User

class Guild():
    def __init__(self,json_guild):
        self.id = None
        self.name = None
        self.icon = None
        self.splash = None
        self.owner_id = None
        self.region = None
        self.afk_channel_id = None
        self.afk_timeout = None
        self.embed_enabled = None
        self.embed_channel_id = None
        self.verification_level = None
        self.default_message_notifications = None
        self.explicit_content_filter = None
        self.roles = None
        self.emojis = None
        self.features = None
        self.mfa_level = None
        self.application_id = None
        self.widget_enabled = None
        self.widget_channel_id = None
        self.joined_at = None
        self.large = None
        self.unavailable = None
        self.member_count = None
        self.voice_states = None
        self.members = []
        self.channels = None
        self.presences = None

        self.update(json_guild)



    def update(self, json_guild):
        for key in json_guild.keys():
            if key == "members":
                for m in json_guild[key]:
                    self.members.append(User(json_user=m))
            else:
                setattr(self, key, json_guild[key])
