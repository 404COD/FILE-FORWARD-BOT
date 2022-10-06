#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) inbliz

from config import Config
from config import LOGGER
from pyrogram import Client, __version__


class User(Client):
    def __init__(self):
        super().__init__(
            Config.SESSION,
            api_hash=Config.API_HASH,
            api_id=Config.API_ID,
            workers=4
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        return (self, usr_bot_me.id)

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")
