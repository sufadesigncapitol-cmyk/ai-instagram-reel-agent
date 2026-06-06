"""
Main Agent Orchestrator - Coordinates all components of the reel creation workflow
"""

import asyncio
import logging
from typing import Dict, Optional, List
from datetime import datetime
from src.research.engine import ResearchEngine
from src.scriptwriter.generator import ScriptGenerator
from src.voiceover.generator import VoiceoverGenerator
from src.video_editor.creator import VideoCreator
from src.caption_generator.generator import CaptionGenerator
from src.social_media.uploader import SocialMediaUploader
from src.vector_db.manager import VectorDBManager
from src.utils.logger import setup_logger

logger = setup_logger(__name__)


class ReelAgent:
    """Main orchestrator for autonomous reel creation"""
    
    def __init__(self, config):
        self.config = config
        self.research_engine = ResearchEngine(config)
        self.script_generator = ScriptGenerator(config)
        self.voiceover_generator = VoiceoverGenerator(config)
        self.video_creator = VideoCreator(config)
        self.caption_generator = CaptionGenerator(config)
        self.social_uploader = SocialMediaUploader(config)
        self.vector_db = VectorDBManager(config)
        
    async def run(self) -> Dict:
        """Execute the complete reel creation workflow"""
        try:
            logger.info("=" * 50)
            logger.info("Starting Reel Creation Workflow")
            logger.info("=" * 50)
            
            # Phase 1: Research
            logger.info("\n[Phase 1] Starting Research...")
            research_data = await self.research_engine.find_trending_topics()
            logger.info(f"Found {len(research_data)} trending topics")
            
            # Phase 2: Script Generation
            logger.info("\n[Phase 2] Generating Script...")
            script = await self.script_generator.generate(research_data)
            logger.info(f"Script generated: {len(script['content'])} characters")
            
            # Phase 3: Voiceover
            logger.info("\n[Phase 3] Generating Voiceover...")
            audio_path = await self.voiceover_generator.generate(script['content'])
            logger.info(f"Voiceover generated: {audio_path}")
            
            # Phase 4: Video Creation
            logger.info("\n[Phase 4] Creating Video...")
            video_path = await self.video_creator.create(audio_path, script)
            logger.info(f"Video created: {video_path}")
            
            # Phase 5: Captions & Hashtags
            logger.info("\n[Phase 5] Generating Captions and Hashtags...")
            captions = await self.caption_generator.generate(script, research_data)
            logger.info(f"Captions generated with {len(captions['hashtags'])} hashtags")
            
            # Phase 6: Vector DB Learning
            logger.info("\n[Phase 6] Storing in Vector Database...")
            await self.vector_db.store_content(script, research_data, captions)
            logger.info("Content stored and indexed")
            
            # Phase 7: Publishing
            logger.info("\n[Phase 7] Publishing to Social Media...")
            publish_result = await self.social_uploader.upload(
                video_path,
                captions['caption'],
                captions['hashtags']
            )
            logger.info(f"Published to: {', '.join(publish_result['published_to'])}")
            
            result = {
                'status': 'success',
                'timestamp': datetime.now().isoformat(),
                'video_path': video_path,
                'research_topics': len(research_data),
                'platforms_published': publish_result['published_to'],
                'captions': captions,
                'script': script
            }
            
            logger.info("\n" + "=" * 50)
            logger.info("Workflow Completed Successfully!")
            logger.info("=" * 50)
            
            return result
            
        except Exception as e:
            logger.error(f"Workflow failed: {str(e)}", exc_info=True)
            raise
