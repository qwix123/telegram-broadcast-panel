from telethon import TelegramClient
from telethon.sessions import StringSession
from app.core.config import settings
from typing import Optional
import os

class TelegramClientManager:
    def __init__(self):
        self.client: Optional[TelegramClient] = None
        self.session_string: Optional[str] = None
    
    async def initialize(self, phone_number: str, session_string: Optional[str] = None):
        """Initialize Telegram client with proxy support"""
        
        proxy = None
        if settings.proxy_enabled and settings.proxy_server:
            proxy = {
                'proxy_type': settings.proxy_type,
                'addr': settings.proxy_server,
                'port': settings.proxy_port,
                'username': settings.proxy_username,
                'password': settings.proxy_password,
            }
        
        session = StringSession(session_string) if session_string else StringSession()
        
        self.client = TelegramClient(
            session,
            settings.api_id,
            settings.api_hash,
            proxy=proxy,
        )
        
        await self.client.connect()
        return self.client
    
    async def send_code_request(self, phone_number: str):
        """Request code for login"""
        return await self.client.send_code_request(phone_number)
    
    async def sign_in(self, phone_number: str, code: str):
        """Sign in with phone and code"""
        await self.client.sign_in(phone_number, code)
        self.session_string = self.client.session.save()
        return self.session_string
    
    async def get_me(self):
        """Get current user info"""
        return await self.client.get_me()
    
    async def disconnect(self):
        """Disconnect from Telegram"""
        if self.client:
            await self.client.disconnect()
            self.client = None

telegram_manager = TelegramClientManager()