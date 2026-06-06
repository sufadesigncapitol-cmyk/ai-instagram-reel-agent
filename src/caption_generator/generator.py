"""
Caption Generator - Creates captions and hashtags for reels
"""

import asyncio
import logging
from typing import Dict, List
import openai
from src.utils.logger import setup_logger

logger = setup_logger(__name__)


class CaptionGenerator:
    """Generates captions and hashtags"""
    
    def __init__(self, config):
        self.config = config
        openai.api_key = config.openai.api_key if hasattr(config, 'openai') else ""
        self.model = config.openai.model if hasattr(config, 'openai') else "gpt-4"
        
    async def generate(self, script: Dict, research_data: List[Dict]) -> Dict:
        """Generate caption and hashtags"""
        try:
            logger.info("Generating captions and hashtags...")
            
            topic = script.get('topic', 'trending')
            
            # Generate demo caption and hashtags
            caption = f"""🔥 {topic} is TRENDING! 🔥

Did you know about this? Let's explore together! 🤔

Like & Follow for more trending content!

#InstagramReels #TrendingNow #{topic.replace(' ', '')}"""
            
            hashtags = [
                '#trending',
                '#viral',
                '#instagrams',
                '#reels',
                f'#{topic.replace(" ", "")}',
                '#explore',
                '#entertainment',
                '#content'
            ]
            
            result = {
                'caption': caption,
                'hashtags': hashtags,
                'hashtag_count': len(hashtags),
                'caption_length': len(caption)
            }
            
            logger.info(f"Caption generated: {result['caption_length']} characters, {result['hashtag_count']} hashtags")
            return result
            
        except Exception as e:
            logger.error(f"Error generating captions: {str(e)}")
            raise
