# GLM Integration Summary

## What Was Created

This repository has been enhanced with GLM-4.7 support from Z.ai. The integration allows you to analyze Google Ads data using GLM's advanced reasoning capabilities instead of being limited to Claude or other AI assistants.

## New Files

### 1. `glm_google_ads_client.py`
**Main GLM client that bridges GLM-4.7 with Google Ads MCP server**

Features:
- ✅ Full tool calling support for all Google Ads functions
- ✅ Interactive chat mode for natural conversation
- ✅ Batch processing for automation
- ✅ Configurable model selection (glm-4.7, 4.6, 4.5, 4.6v)
- ✅ Environment variable configuration
- ✅ Error handling and graceful fallbacks

### 2. `example_usage.py`
**Simple getting started script showing basic usage**

Purpose:
- Verify Z.ai API key is configured
- Demonstrate basic chat with GLM
- Show tool calling example
- Quick connectivity test

### 3. `.env.example.glm`
**Environment configuration template for GLM integration**

Includes:
- Z.ai API key configuration
- Google Ads credentials setup
- Model selection options
- Documentation of available models

### 4. `README_GLM.md`
**Comprehensive documentation for GLM integration**

Contents:
- Feature comparison with other models
- Architecture diagram
- Usage examples (20+ scenarios)
- Advanced features (streaming, batch, etc.)
- Configuration options
- Troubleshooting guide
- FAQ

### 5. `QUICKSTART.md`
**5-minute quick start guide**

Includes:
- Step-by-step setup instructions
- Example conversations
- Common use cases
- Troubleshooting tips

### 6. Updated `requirements.txt`
**Added zai-sdk dependency**

New dependency:
```
zai-sdk>=0.2.0
```

## Architecture

```
User
  ↓
GLM-4.7 (zai-sdk)
  ↓
Tool Calls
  ↓
GLMMCPClient
  ↓
JSON-RPC (stdio)
  ↓
google_ads_server.py (MCP Server)
  ↓
Google Ads API
```

## How It Works

1. **User asks GLM a question** (e.g., "Show me my top campaigns")
2. **GLM analyzes the request** and decides which tool to call
3. **GLMMCPClient forwards tool call** to MCP server
4. **MCP server executes GAQL query** against Google Ads API
5. **Results return to GLM** for analysis and insights
6. **GLM presents results** with actionable recommendations

## Key Advantages Over Original

| Aspect | Original (Claude-only) | GLM Enhanced |
|---------|------------------------|---------------|
| AI Model | Limited to Claude | Any GLM model (4.5, 4.6, 4.7) |
| Deployment | Requires Claude Desktop | Standalone Python script |
| Interface | CLI through Claude | Interactive chat or API |
| Automation | Manual only | Batch processing available |
| Cost Control | N/A | Choose model based on needs |
| Model Selection | None | Flexible (glm-4.7, 4.6, 4.5) |
| Context Window | Claude's limit | Up to 200K tokens |
| Open Source | No | Yes (GLM models are open source) |

## Getting Started

### Quick Test (2 minutes)

```bash
# 1. Install zai-sdk
pip install zai-sdk

# 2. Set API key
export ZAI_API_KEY="your_key_here"

# 3. Test connection
python example_usage.py

# 4. Start chatting
python glm_google_ads_client.py
```

### Full Setup (5 minutes)

See [QUICKSTART.md](QUICKSTART.md) for complete guide.

## Usage Examples

### Interactive Mode
```bash
python glm_google_ads_client.py
```

Then chat:
```
You: Analyze my campaign performance
GLM: I'll retrieve your campaign data... [provides analysis]

You: Which ads have best CTR?
GLM: Let me check your ad performance... [shows top performers]

You: Run a query to find top converting keywords
GLM: I'll execute a GAQL query... [runs and presents results]
```

### Single Query Mode
```bash
python glm_google_ads_client.py -m "Show my top 10 campaigns by cost"
```

### Programmatic Usage
```python
from glm_google_ads_client import GLMMCPClient
import asyncio

async def main():
    client = GLMMCPClient(api_key="your_key")
    
    # Analyze multiple accounts
    accounts = ["1234567890", "0987654321"]
    
    for account in accounts:
        response = await client.chat(
            f"What are the top campaigns for account {account}?"
        )
        print(response)

asyncio.run(main())
```

## Available GLM Models

| Model | Parameters | Context | Best For |
|--------|-------------|----------|-----------|
| glm-4.7 | 355B MoE | 128K tokens | Complex analysis, reasoning |
| glm-4.6 | - | 200K tokens | Long context, document analysis |
| glm-4.5 | 106B MoE | 128K tokens | Fast responses, cost-efficient |
| glm-4.6v | - | - | Image analysis |

## Tool Coverage

All Google Ads MCP tools are available:

- ✅ `list_accounts` - List all accounts
- ✅ `get_account_currency` - Get currency code
- ✅ `get_campaign_performance` - Campaign metrics
- ✅ `get_ad_performance` - Ad metrics
- ✅ `run_gaql` - Custom GAQL queries
- ✅ `get_ad_creatives` - Review ad copy
- ✅ `get_image_assets` - List image assets
- ✅ `analyze_image_assets` - Image performance
- ✅ `download_image_asset` - Download images
- ✅ `get_asset_usage` - Where assets are used

## Configuration

### Required Environment Variables

```env
ZAI_API_KEY=your_zai_api_key
GOOGLE_ADS_CREDENTIALS_PATH=/path/to/credentials.json
GOOGLE_ADS_DEVELOPER_TOKEN=your_dev_token
```

### Optional Environment Variables

```env
GLM_MODEL=glm-4.7  # Default: glm-4.7
GOOGLE_ADS_AUTH_TYPE=oauth  # Default: oauth (or service_account)
GOOGLE_ADS_LOGIN_CUSTOMER_ID=1234567890  # Manager account ID
```

## Use Cases

### 1. Performance Analysis
- "What are my top performing campaigns?"
- "Which ads have the best CTR?"
- "Analyze my keyword performance"

### 2. Budget Optimization
- "Which campaigns should I increase budget for?"
- "Am I spending efficiently?"
- "Identify campaigns with poor ROAS"

### 3. Creative Review
- "Review my ad headlines and suggest improvements"
- "Which images are performing best?"
- "Analyze my ad copy effectiveness"

### 4. Custom Queries
- "Run a GAQL query for [custom requirements]"
- "Find keywords with [specific criteria]"
- "Export campaign data as CSV"

### 5. Automation
- Batch process multiple accounts
- Schedule regular reports
- Generate weekly summaries

## Next Steps

1. **Configure API keys**: Set up Z.ai and Google Ads credentials
2. **Test connection**: Run `python example_usage.py`
3. **Start analyzing**: Use `python glm_google_ads_client.py`
4. **Customize**: Modify client for your specific needs
5. **Automate**: Create batch scripts for regular tasks

## Documentation

- **[QUICKSTART.md](QUICKSTART.md)** - 5-minute setup guide with examples
- **[README_GLM.md](README_GLM.md)** - Full documentation with all features
- **[README.md](README.md)** - Original mcp-google-ads documentation (Claude-focused)

## Benefits of GLM Integration

### For Users
- 🔓 **More Model Options** - Choose from GLM-4.5, 4.6, 4.7 based on needs
- 💰 **Cost Control** - Select efficient models for simple queries
- 🌐 **Open Source** - GLM models are open source and auditable
- 🚀 **Advanced Reasoning** - 355B MoE architecture for complex analysis
- 📊 **200K Context** - Handle complex multi-step analysis
- 🤖 **Native Tools** - Built for agentic tool usage

### For Developers
- 🔧 **Flexible Deployment** - Run as script, service, or API
- 🔄 **Batch Processing** - Automate multi-account analysis
- 📝 **Customizable** - Extend client for specific workflows
- 🧪 **Standalone** - No dependency on Claude Desktop/Cursor

## Acknowledgments

- **[mcp-google-ads](https://github.com/cohnen/mcp-google-ads)** - Original project by cohnen
- **[z-ai-sdk-python](https://github.com/zai-org/z-ai-sdk-python)** - Official Z.ai Python SDK
- **[GLM Models](https://github.com/zai-org/GLM-4.5)** - Open source models from Zhipu AI
- **[MCP Protocol](https://modelcontextprotocol.io/)** - Anthropic's open standard

## Support

For issues or questions:
- Check [QUICKSTART.md](QUICKSTART.md) troubleshooting section
- Review [README_GLM.md](README_GLM.md) for detailed docs
- Open GitHub issue with error details and steps to reproduce

## License

MIT License - Same as original mcp-google-ads project
