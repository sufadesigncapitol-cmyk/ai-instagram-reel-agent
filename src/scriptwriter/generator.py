"""
Script Generator - Creates engaging scripts for Instagram Reels
"""

import asyncio
import logging
from typing import Dict, List
import openai
from src.utils.logger import setup_logger

logger = setup_logger(__name__)


class ScriptGenerator:
    """Generates engaging scripts for reels"""
    
    def __init__(self, config):
        self.config = config
        openai.api_key = config.openai.api_key if hasattr(config, 'openai') else ""
        self.model = config.openai.model if hasattr(config, 'openai') else "gpt-4"
        
    async def generate(self, research_data: List[Dict]) -> Dict:
        """Generate a script based on research data"""
        try:
            logger.info("Generating script from research data...")
            
            # Select best topic
            topic = research_data[0]['topic'] if research_data else "trending topic"
            
            prompt = f"""Create an engaging Instagram Reel script (60 seconds max) about: {topic}
            
            Requirements:
            - Hook the viewer in first 3 seconds
            - Maintain high energy and engagement
            - Include call-to-action at the end
            - Make it entertaining and informative
            - Add visual cues for video editing
            - Keep it under 150 words
            
            Format the script as:
            [OPENING HOOK]
            [MAIN CONTENT]
            [VISUAL CUES]
            [CALL TO ACTION]
            """
            
            # For now, return a demo script
            script_content = f"""[OPENING HOOK]
"Did you know this trending topic is blowing up? Let me show you why!"

[MAIN CONTENT]
This {topic} is fascinating because... [engaging facts]

[VISUAL CUES]
- Quick cuts
- Text overlays
- B-roll transitions

[CALL TO ACTION]
Comment your thoughts below! Don't forget to like and follow!"""
            
            script = {
                'content': script_content,
                'topic': topic,
                'word_count': len(script_content.split()),
                'tone': 'engaging'
            }
            
            logger.info(f"Script generated: {script['word_count']} words")
            return script
            
        except Exception as e:
            logger.error(f"Error generating script: {str(e)}")
            raise
