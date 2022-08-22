import os


class Config(object):
      bot_token = os.environ.get("bot_token", "5713884943:AAGBn_ESkg3y0VZurKkFnFf2pzbtfnCWSmQ")
      api_id = os.environ.get("api_id", 18862638)
      api_hash = os.environ.get("api_hash", "2a4a8dc0c1f6c9cb65f9f144439558ae")
