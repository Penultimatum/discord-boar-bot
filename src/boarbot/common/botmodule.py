import discord
from abc import ABCMeta, abstractmethod

from boarbot.common.events import EventType

class BotModule(metaclass=ABCMeta):
    def __init__(self, client: discord.Client):
        self.client = client

    @abstractmethod
    async def handle_event(self, event_type: EventType, args):
        ...
