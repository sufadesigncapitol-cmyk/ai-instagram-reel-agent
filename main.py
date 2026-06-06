"""
AI Instagram Reel Agent - Main Entry Point
Orchestrates the entire workflow for autonomous reel creation and publishing
"""

import asyncio
import logging
from typing import Optional
from src.agent.orchestrator import ReelAgent
from src.config.settings import Config
from src.utils.logger import setup_logger

logger = setup_logger(__name__)


async def main():
    """Main entry point for the AI agent"""
    try:
        logger.info("Starting AI Instagram Reel Agent")
        
        # Load configuration
        config = Config.load()
        logger.info(f"Configuration loaded: {config.agent_name}")
        
        # Initialize agent
        agent = ReelAgent(config)
        
        # Run the complete workflow
        logger.info("Starting autonomous reel creation workflow")
        result = await agent.run()
        
        logger.info(f"Workflow completed successfully")
        logger.info(f"Result: {result}")
        
    except Exception as e:
        logger.error(f"Fatal error in main workflow: {str(e)}", exc_info=True)
        raise


if __name__ == "__main__":
    asyncio.run(main())
