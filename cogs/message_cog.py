"""
This cog provides a command to set reminders.
The command allows users to set a reminder that will be sent to them after a specified time.
"""

import discord
from discord import app_commands
from discord.ext import commands
import asyncio
import logging

# Get a logger instance for this module
logger = logging.getLogger(__name__)

class ReminderCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot  # Initialize the cog with the bot instance

    @app_commands.command(name='remindme', description='Set a reminder.')
    async def remind_me(self, interaction: discord.Interaction, time: int, *, message: str):
        """Sets a reminder. Time is in seconds."""
        try:
            await interaction.response.send_message(f"Reminder set! I will remind you in {time} seconds.")
            await asyncio.sleep(time)
            await interaction.user.send(f"Reminder: {message}")
            logger.info(f'Reminder set for {interaction.user} with message: {message}')
        except Exception as e:
            await interaction.response.send_message('An error occurred while setting the reminder.')
            logger.error(f'Failed to set reminder: {e}')

async def setup(bot):
    # Function to add the cog to the bot during setup
    await bot.add_cog(ReminderCog(bot))