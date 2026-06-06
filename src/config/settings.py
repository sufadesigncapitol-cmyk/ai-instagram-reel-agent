"""
Settings and configuration management for AI Instagram Reel Agent
"""

from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional, List
import yaml
from pathlib import Path


class DatabaseSettings(BaseSettings):
    url: str = Field(default="postgresql://localhost/ai_reel_agent")
    echo: bool = False


class OpenAISettings(BaseSettings):
    api_key: str = Field(default="")
    model: str = "gpt-4"


class ResearchSettings(BaseSettings):
    enabled: bool = True
    sources: List[str] = ["google_trends", "reddit", "twitter"]


class VoiceoverSettings(BaseSettings):
    provider: str = "elevenlabs"
    language: str = "en-US"
    speed: float = 1.0


class VideoSettings(BaseSettings):
    resolution: str = "1080x1920"
    fps: int = 30
    duration: int = 60


class Config(BaseSettings):
    agent_name: str = "InstagramReelAgent"
    openai: OpenAISettings = OpenAISettings()
    research: ResearchSettings = ResearchSettings()
    voiceover: VoiceoverSettings = VoiceoverSettings()
    video: VideoSettings = VideoSettings()
    
    class Config:
        env_file = ".env"
        case_sensitive = False
    
    @classmethod
    def load(cls) -> "Config":
        """Load configuration from config.yaml and .env"""
        config_path = Path("config.yaml")
        if config_path.exists():
            with open(config_path, 'r') as f:
                yaml_config = yaml.safe_load(f)
                return cls(**yaml_config)
        return cls()
