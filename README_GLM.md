# Google Ads with GLM-4.7

This is a fork of the original [mcp-google-ads](https://github.com/cohnen/mcp-google-ads) project, enhanced to work with **Z.ai's GLM-4.7** models instead of being limited to Claude AI.

## What This Does

This project provides a powerful AI assistant that uses **GLM-4.7** (Z.ai's latest flagship model) to analyze your Google Ads data through natural language conversations. It combines:

- **Google Ads API Integration** - Access to all your Google Ads data
- **MCP Protocol** - Standardized tool interface for AI models
- **GLM-4.7 Model** - Z.ai's 355B parameter Mixture-of-Experts model with advanced reasoning capabilities

## Key Features

### What GLM-4.7 Brings

GLM-4.7 offers several advantages over other models:

- **355B Parameters** - Massive scale for better understanding
- **Mixture-of-Experts (MoE)** Architecture - More efficient and specialized reasoning
- **200K Context Window** - Handle complex multi-step analysis
- **Advanced Agentic Capabilities** - Built for tool-using agents
- **Hybrid Reasoning Mode** - Can switch between instant responses and deep thinking

### Available Tools

The GLM assistant can use these Google Ads tools:

| Tool | Description |
|-------|-------------|
| `list_accounts` | List all accessible Google Ads accounts |
| `get_account_currency` | Get account's default currency code |
| `get_campaign_performance` | Analyze campaign metrics over time period |
| `get_ad_performance` | Analyze ad creative performance |
| `run_gaql` | Run custom GAQL queries |
| `get_ad_creatives` | Review ad copy and creative elements |
| `get_image_assets` | List all image assets with URLs |
| `analyze_image_assets` | Analyze image performance across campaigns |

## Quick Start

### 1. Set Up Z.ai API Key

Get your API key from [Z.ai Open Platform](https://docs.z.ai/):

```bash
export ZAI_API_KEY="your_api_key_here"
```

### 2. Configure Google Ads Credentials

Copy the GLM-specific env file:

```bash
cp .env.example.glm .env
```

Edit `.env` with your Google Ads credentials:

```env
# Google Ads Configuration
GOOGLE_ADS_CREDENTIALS_PATH=/path/to/your/credentials.json
GOOGLE_ADS_DEVELOPER_TOKEN=your_developer_token
GOOGLE_ADS_LOGIN_CUSTOMER_ID=your_manager_account_id
GOOGLE_ADS_AUTH_TYPE=oauth

# Z.ai Configuration
ZAI_API_KEY=your_zai_api_key
GLM_MODEL=glm-4.7
```

### 3. Install Dependencies

```bash
# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

### 4. Run GLM Assistant

**Interactive Mode:**
```bash
python glm_google_ads_client.py
```

**Single Query Mode:**
```bash
python glm_google_ads_client.py -m "Show me my top performing campaigns from the last 30 days"
```

## Usage Examples

### Example 1: Analyze Campaign Performance

```
You: Show me my top 5 campaigns by spend in the last 30 days

GLM: I'll retrieve your campaign performance data...
[Retrieves data via MCP]
Here are your top 5 campaigns by cost:

1. Brand Search - $15,234.56
   - 234,567 impressions
   - 12,345 clicks
   - 2.1% CTR
   - 1,234 conversions

[Continues with analysis...]
```

### Example 2: Ad Creative Analysis

```
You: Which ad headlines are performing best in my search campaigns?

GLM: Let me analyze your ad performance data...
[Queries Google Ads API]
Based on the last 30 days:

Top Performing Headlines:
1. "Limited Time Offer - 50% Off" - 4.5% CTR
2. "Free Shipping Today" - 3.8% CTR
3. "Best Prices Guaranteed" - 3.2% CTR

Recommendations:
- The discount-focused headline performs best, consider testing more urgency triggers
- "Free Shipping" has strong performance, expand to more ad groups
```

### Example 3: Custom GAQL Query

```
You: Run a query to show keywords with >1000 impressions but CTR < 2%

GLM: I'll run a custom GAQL query for you...
[Executes GAQL query]
Found 12 keywords meeting your criteria:

Keyword          | Impressions | Clicks | CTR    | Cost
-----------------+-------------+---------+---------+--------
discount shoes    | 45,678      | 432     | 0.95%   | $234.56
sale footwear     | 34,234      | 298     | 0.87%   | $189.23
...

These keywords need optimization. Consider:
- Improving ad relevance for better CTR
- Lowering bids on underperforming keywords
- Adding negative keywords if traffic is irrelevant
```

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                 User Input                      │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│           GLM-4.7 Model                      │
│         (z-ai-sdk-python)                    │
│                                              │
│  - Advanced reasoning (355B params)            │
│  - Tool calling capabilities                   │
│  - 200K context window                       │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼ (Tool Calls)
┌─────────────────────────────────────────────────────────┐
│      MCP Protocol Layer                         │
│    (glm_google_ads_client.py)                  │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼ (JSON-RPC)
┌─────────────────────────────────────────────────────────┐
│    Google Ads MCP Server                       │
│    (google_ads_server.py)                      │
│                                              │
│  - Authentication (OAuth/Service Account)        │
│  - GAQL Query Execution                     │
│  - Data Formatting                           │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│      Google Ads API (v19)                     │
└─────────────────────────────────────────────────────────┘
```

## GLM-4.7 vs Other Models

| Feature | GLM-4.7 | Claude 3.5 | GPT-4o |
|----------|-------------|--------------|----------|
| Parameters | 355B MoE | ~200B | ~1.8T |
| Context Window | 200K tokens | 200K tokens | 128K tokens |
| Tool Calling | Native | Native | Native |
| Hybrid Reasoning | ✓ | - | - |
| Open Source | ✓ | - | - |
| Chinese Support | Excellent | Good | Good |

## Advanced Features

### Hybrid Reasoning Mode

GLM-4.7 offers two inference modes:

1. **Thinking Mode** - Deep reasoning for complex analysis
   - Great for: Strategic campaign optimization
   - Cost: Higher latency, better quality

2. **Non-Thinking Mode** - Fast, direct responses  
   - Great for: Quick data lookups
   - Cost: Lower latency, faster responses

The client automatically selects the appropriate mode based on query complexity.

### Streaming Responses

Enable streaming for real-time responses:

```bash
python glm_google_ads_client.py --stream
```

### Batch Analysis

Process multiple accounts in sequence:

```python
from glm_google_ads_client import GLMMCPClient

client = GLMMCPClient(api_key="your_key")
accounts = ["1234567890", "0987654321"]

for account in accounts:
    result = client.chat(f"Analyze top campaigns for account {account}")
    print(f"Account {account}: {result}")
```

## Configuration Options

### Environment Variables

| Variable | Description | Default |
|-----------|-------------|----------|
| `ZAI_API_KEY` | Your Z.ai API key | Required |
| `GLM_MODEL` | Model to use | `glm-4.7` |
| `ZAI_BASE_URL` | API base URL | `https://api.z.ai/api/paas/v4/` |
| `GOOGLE_ADS_CREDENTIALS_PATH` | Path to credentials file | Required |
| `GOOGLE_ADS_DEVELOPER_TOKEN` | Google Ads dev token | Required |
| `GOOGLE_ADS_LOGIN_CUSTOMER_ID` | Manager account ID | Optional |

### Available GLM Models

- `glm-4.7` - Flagship (355B MoE, recommended)
- `glm-4.6` - Extended context (200K tokens)
- `glm-4.5` - Efficient (106B parameters)
- `glm-4.6v` - Vision model for image analysis

## Troubleshooting

### Common Issues

**"zai-sdk not installed"**
```bash
pip install zai-sdk
```

**"MCP server not found"**
Ensure `google_ads_server.py` is in the same directory as `glm_google_ads_client.py`

**"Google Ads API rate limit"**
The MCP server includes built-in rate limiting. If you hit limits:
- Reduce query frequency
- Use more specific GAQL queries
- Consider upgrading your Google Ads API access level

**"Tool call failed"**
Check that:
1. Google Ads credentials are valid
2. Your account has access to the requested customer ID
3. Developer token is approved (not test token)

### Debug Mode

Enable verbose logging:

```bash
python glm_google_ads_client.py --debug
```

## Contributing

This project is open source! Contributions welcome:

1. Fork this repository
2. Create your feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - see [LICENSE](LICENSE) file for details

## Acknowledgments

- Original [mcp-google-ads](https://github.com/cohnen/mcp-google-ads) by [cohnen](https://github.com/cohnen)
- [z-ai-sdk-python](https://github.com/zai-org/z-ai-sdk-python) by Z.ai
- [MCP Protocol](https://modelcontextprotocol.io/) by Anthropic

## Contact & Support

- **Issues**: Report bugs or feature requests on GitHub Issues
- **Email**: user_feedback@z.ai (for Z.ai SDK issues)
- **Documentation**: [Z.ai Docs](https://docs.z.ai/)

## What's Different from Original?

The original mcp-google-ads project was designed specifically for Claude Desktop/Cursor. This GLM-enhanced version:

✅ **Model Agnostic** - Works with any GLM model (4.5, 4.6, 4.7)
✅ **Standalone Client** - No need for Claude/Cursor installation
✅ **Interactive Chat** - Full conversational interface
✅ **Batch Processing** - Programmatic access for automation
✅ **Hybrid Reasoning** - Automatic mode selection based on query complexity
✅ **Flexible Deployment** - Can run as script, service, or API

You get all the Google Ads analysis capabilities with the power of GLM-4.7!
