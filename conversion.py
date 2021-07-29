# Made only for Educational Purpose
# New-dev0 (2021)
# https://gist.github.com/New-dev0/c3b515d34cdd3470408a065ff48fc480


import struct, base64
from telethon.sessions.string import StringSession
from telethon.sync import TelegramClient
from pyrogram.storage.storage import Storage


def telethon_to_unpack(string):
  ST = StringSession(string)
  return ST


def start_session(string, api_id, api_hash):
  with TelegramClient(StringSession(string), api_id, api_hash) as ses:
    ml = ses.get_me()
  return ml


def pack_to_pyro(data, ses):
  Dt = Storage.SESSION_STRING_FORMAT
  return base64.urlsafe_b64encode(
            struct.pack(
                Dt,
                data.dc_id,
                None,
                data.auth_key.key,
                ses.id,
                ses.bot
        )).decode().rstrip("=")


def tele_to_pyro(string, api_id=6, api_hash="eb06d4abfb49dc3eeb1aeb98ae0f581e"):
    DL = telethon_to_unpack(string)
    MK = start_session(string, api_id, api_hash)
    return pack_to_pyro(DL, MK)
