# AI Instagram Reel Agent

An autonomous AI agent that automatically creates, manages, and uploads Instagram Reels with minimal human intervention. The agent handles research, trending topic discovery, scriptwriting, voiceover generation, video creation, caption generation, and social media uploads.

## Features

- 🔍 **Autonomous Research**: Finds trending topics and gathers relevant information
- 📝 **Script Generation**: Writes engaging scripts for short-form content
- 🎤 **Voiceover Creation**: Generates natural-sounding audio narration
- 🎬 **Video Creation & Editing**: Assembles videos with effects and transitions
- 📱 **Caption & Hashtag Generation**: Creates optimized captions and hashtags
- 🚀 **Automated Upload**: Posts to Instagram and other social platforms
- 🧠 **Vector Database Learning**: Stores and learns from previous research
- 📊 **Analytics & Tracking**: Monitors performance and engagement
- ⚙️ **Workflow Orchestration**: Manages entire process without human intervention

## Project Structure

```
ai-instagram-reel-agent/
├── src/
│   ├── agent/                 # Main agent orchestration
│   ├── research/              # Research and trending topics
│   ├── scriptwriter/          # Script generation
│   ├── voiceover/             # Text-to-speech
│   ├── video_editor/          # Video creation and editing
│   ├── caption_generator/     # Captions and hashtags
│   ├── social_media/          # Platform integrations
│   ├── vector_db/             # Vector database management
│   ├── utils/                 # Helper utilities
│   └── config/                # Configuration management
├── tests/                     # Unit and integration tests
├── data/                      # Data storage
├── logs/                      # Application logs
├── requirements.txt           # Python dependencies
├── .env.example               # Environment variables template
├── config.yaml                # Application configuration
└── main.py                    # Entry point
```

## Installation

### Prerequisites

- Python 3.10+
- FFmpeg (for video processing)
- Git

### Setup

1. Clone the repository
```bash
git clone https://github.com/sufadesigncapitol-cmyk/ai-instagram-reel-agent.git
cd ai-instagram-reel-agent
```

2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure environment variables
```bash
cp .env.example .env
# Edit .env with your API keys and credentials
```

5. Initialize vector database
```bash
python src/vector_db/init_db.py
```

## Configuration

Edit `config.yaml` to customize:

- Research sources and keywords
- Content preferences and themes
- Video parameters (resolution, duration, effects)
- Social media platforms and schedules
- Vector database settings
- API credentials

See `.env.example` for required environment variables:

- OpenAI API Key
- Anthropic API Key (Claude)
- Instagram Meta API Token
- Twitter API Keys
- Pinecone/Weaviate API Keys
- Google Trends API
- News APIs

## Usage

### Run the agent

```bash
python main.py
```

### Run specific tasks

```bash
# Research only
python -m src.research.engine

# Generate script
python -m src.scriptwriter.generator

# Create video
python -m src.video_editor.creator

# Upload to social media
python -m src.social_media.uploader
```

### Schedule automated runs

```bash
# Run agent every 6 hours
python src/scheduler/run.py --interval 6h
```

## Architecture

### Agent Flow

1. **Research Phase**: Discovers trending topics, gathers data
2. **Planning Phase**: Selects best topic, plans content strategy
3. **Creation Phase**: Generates script, voiceover, video, captions
4. **Optimization Phase**: Queries vector DB for performance insights
5. **Publishing Phase**: Uploads to social platforms
6. **Learning Phase**: Stores results and metrics for future improvement

### Technology Stack

- **LLM**: OpenAI GPT-4 / Claude 3
- **Voice**: ElevenLabs / Google TTS / Azure Speech
- **Video**: FFmpeg, MoviePy, OpenCV
- **Vector DB**: Pinecone, Weaviate, or Milvus
- **Task Orchestration**: CrewAI / LangChain / Celery
- **APIs**: Meta Graph API, Twitter API, YouTube API
- **Web Scraping**: BeautifulSoup, Scrapy
- **Database**: PostgreSQL (metadata), Vector DB (embeddings)

## API Integrations

### Social Media
- **Instagram**: Meta Graph API
- **TikTok**: TikTok Open Platform
- **YouTube Shorts**: YouTube Data API
- **Twitter/X**: X API v2

### AI Services
- **LLMs**: OpenAI, Anthropic, Google Gemini
- **Voice**: ElevenLabs, Google Cloud TTS
- **Vision**: OpenAI Vision, Claude Vision

### Data Sources
- **Trends**: Google Trends, Trending US, Reddit API
- **News**: NewsAPI, Guardian API, New York Times API
- **Social**: Twitter Trending, TikTok Trends API

## Vector Database

Stores:
- Research findings and summaries
- Script performance metrics
- Audience engagement data
- Visual preferences
- Hashtag effectiveness
- Audio characteristics

Query examples:
- Find scripts similar to high-performing content
- Retrieve hashtags for trending topics
- Find visual styles that resonate with audience
- Identify optimal posting times

## Performance Monitoring

The agent tracks:
- Engagement rates (likes, comments, shares)
- View duration and completion rates
- Audience demographics
- Trending performance
- Cost per engagement
- Processing time

Metrics stored in vector DB for optimization.

## Error Handling & Logging

- Comprehensive logging at each stage
- Automatic retry logic for API calls
- Graceful degradation for missing components
- Detailed error reports
- Monitoring dashboard

## Security

- API keys stored in environment variables
- Secure credential management
- Rate limiting for API calls
- Content moderation checks
- Compliance with platform policies

## Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## License

MIT License - see LICENSE file

## Roadmap

- [ ] Multi-language support
- [ ] Advanced video effects library
- [ ] Real-time trend tracking
- [ ] A/B testing framework
- [ ] Advanced analytics dashboard
- [ ] Mobile app for monitoring
- [ ] Integration with more platforms
- [ ] Custom AI model fine-tuning
- [ ] Community content sharing

## Support

For issues, questions, or suggestions, please open an GitHub issue.

## Disclaimer

This agent is for educational purposes. Ensure compliance with:
- Instagram/Meta Terms of Service
- Copyright and intellectual property laws
- Platform automation policies
- Content authenticity requirements
- Local regulations

Use responsibly and ethically.
