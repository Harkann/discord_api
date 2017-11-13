from config import BASE_URL, VERSION
import requests

class User():
    def __init__(self,token):
        self.token = token

    def generate_header(self):
        user_agent = {"User-Agent": "DiscordBot (%s, %d)" % (BASE_URL, VERSION)}
        auth_header = {"Authorization": "Bot %s" % self.token}
        return dict(user_agent, **auth_header)

    def get_user(self):
        url = "%s/v%d/users/@me" % (BASE_URL, VERSION)
        response = requests.get(url=url, headers=self.generate_header())
        if response.status_code == requests.codes.ok:
            return response.text
        else:
            return None

    def get_user_from_id(self,uid):
        url = "%s/v%d/users/%s" % (BASE_URL, VERSION, uid)
        response = requests.get(url=url, headers=self.generate_header())
        if response.status_code == requests.codes.ok:
            return response.text
        else:
            return None

    def patch_user(self,username=None,avatar=None):
        url = "%s/v%d/users/@me" % (BASE_URL, VERSION)
        payload = dict()
        if username is not None:
            payload = dict(payload, **{"username": username})
        if avatar is not None:
            pass
            # payload = dict(payload, **{})
        response = requests.patch(url=url,headers=self.generate_header(),json=payload)
        if response.status_code == requests.codes.ok:
            return response.text
        else:
            return None

    def get_servers(self):
        url = "%s/v%d/users/@me/guilds" % (BASE_URL, VERSION)
        response = requests.get(url=url, headers=self.generate_header())
        if response.status_code == requests.codes.ok:
            return response.text
        else:
            return None

    # def get_channels(self):
    #     url = "%s/v%d/users/@me/channels" % (BASE_URL, VERSION)
    #     response = requests.get(url=url, headers=self.generate_header())
    #     if response.status_code == requests.codes.ok:
    #         return response.text
    #     else:
    #         return None

    def get_connections(self):
        url = "%s/v%d/users/@me/connections" % (BASE_URL, VERSION)
        response = requests.get(url=url, headers=self.generate_header())
        if response.status_code == requests.codes.ok:
            return response.text
        else:
            return None

    def get_gateway(self):
        url = "%s/v%d/gateway/bot" % (BASE_URL, VERSION)
        response = requests.get(url=url, headers=self.generate_header())
        if response.status_code == requests.codes.ok:
            return response.text
        else:
            return None
