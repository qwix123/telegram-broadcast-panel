from typing import Dict, Optional
from app.core.config import settings

class ProxyHandler:
    @staticmethod
    def get_proxy_config() -> Optional[Dict]:
        """Get current proxy configuration"""
        if not settings.proxy_enabled or not settings.proxy_server:
            return None
        
        return {
            'type': settings.proxy_type,
            'server': settings.proxy_server,
            'port': settings.proxy_port,
            'username': settings.proxy_username or '',
            'password': settings.proxy_password or '',
        }
    
    @staticmethod
    def validate_proxy_config(config: Dict) -> bool:
        """Validate proxy configuration"""
        required_fields = ['type', 'server', 'port']
        return all(field in config for field in required_fields)
    
    @staticmethod
    def format_proxy_url(config: Dict) -> str:
        """Format proxy as URL"""
        proto = config.get('type', 'http')
        server = config.get('server')
        port = config.get('port')
        username = config.get('username', '')
        password = config.get('password', '')
        
        if username and password:
            return f"{proto}://{username}:{password}@{server}:{port}"
        elif username:
            return f"{proto}://{username}@{server}:{port}"
        else:
            return f"{proto}://{server}:{port}"

proxy_handler = ProxyHandler()