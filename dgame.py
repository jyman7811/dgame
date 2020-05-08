import discord
import asyncio

class Dgame:
    def __init__(self, ca, meg, sleeps):
        self.ca = ca
        self.meg = meg
        self.sleeps = sleeps
        
    async def start(self):
        print(f"{self.ca}   {self.meg}   {self.sleeps}")
        messages = self.meg
        while True:
           await self.ca.change_presence(status=discord.Status.online, activity=discord.Game(name=messages[0]))
           messages.append(messages.pop(0))
           await asyncio.sleep(self.sleeps)

