import discord
import asyncio

class dgame:
    def __init__(self, ca, meg, sleeps):
        self.ca = ca
        self.meg = meg
        self.sleeps = sleeps
        
    async def start(self):
        messages = self.meg
        while True:
           await self.ca.change_presence(status=discord.Status.online, activity=discord.Game(name=messages[0]))
           messages.append(messages.pop(0))
           await asyncio.sleep(self.sleeps)

