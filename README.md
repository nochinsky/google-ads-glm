# Google Ads with GLM-4.7

**Analyze your Google Ads campaigns, ads, and performance using GLM's 355B Mixture-of-Experts model through natural language conversations.**

**Repository**: https://github.com/nochinsky/google-ads-glm

---

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

Required packages:
- `httpx` - For Z.ai API calls
- `google-auth-oauthlib` - Google Ads authentication
- `google-auth` - Google API authentication
- `mcp` - MCP protocol support
- `python-dotenv` - Environment configuration

### 2. Configure Credentials

Copy the environment template:
```bash
cp .env.example .env
```

Edit `.env` with your values:
```env
# Required: Z.ai API Key
ZAI_API_KEY=your_zai_api_key_here

# Required: Google Ads Credentials
GOOGLE_ADS_CREDENTIALS_PATH=/path/to/your/google-ads-credentials.json
GOOGLE_ADS_DEVELOPER_TOKEN=your_google_ads_developer_token

# Optional: Authentication Type (default: oauth)
GOOGLE_ADS_AUTH_TYPE=oauth

# Optional: Manager Account ID
GOOGLE_ADS_LOGIN_CUSTOMER_ID=1234567890

# Optional: GLM Model (default: glm-4.7)
GLM_MODEL=glm-4.7
```

**Getting Credentials:**

1. **Z.ai API Key**: Get it from https://platform.z.ai/
2. **Google Ads Developer Token**: Apply at https://ads.google.com/aw/apicenter
3. **Google Ads Credentials**: 
   - OAuth: Create OAuth client in Google Cloud Console
   - Service Account: Create service account in Google Cloud Console

### 3. Run the Tool

```bash
# Interactive mode - chat with GLM
python3 glm_client.py

# Single question
python3 glm_client.py -m "Show my top 10 campaigns by spend"

# Use different GLM model
python3 glm_client.py --model glm-4.5 -m "Analyze my ad performance"
```

---

## 📋 What You Can Ask

GLM can help you analyze your Google Ads data with natural language:

### Campaigns
- "Show me my top 10 campaigns by cost"
- "Which campaigns have the best ROAS?"
- "Analyze my campaign performance trends over the last 90 days"

### Ads & Creatives
- "Which ad headlines are performing best?"
- "Review my ad copy and suggest improvements"
- "Compare image assets performance"

### Keywords
- "Find keywords with high spend but low conversions"
- "What are my top converting keywords?"
- "Identify underperforming keywords"

### Custom Queries
- "Run a GAQL query to find [specific requirement]"
- "Export campaign data as CSV"
- "Find campaigns spending more than $X per month"

### Automation
- "Create a weekly performance report"
- "Analyze all my accounts and identify optimization opportunities"

---

## 🛠️ Available Tools

| Tool | What It Does |
|-------|---------------|
| `list_accounts` | List all your Google Ads accounts |
| `get_account_currency` | Get account's currency code |
| `get_campaign_performance` | Get campaign metrics over time period |
| `get_ad_performance` | Get ad creative performance |
| `run_gaql` | Run custom GAQL queries |
| `get_ad_creatives` | Review ad copy and elements |
| `get_image_assets` | List all image assets |
| `analyze_image_assets` | Analyze image performance |
| `download_image_asset` | Download specific images |

---

## 💬 Example Conversations

### Example 1: Campaign Analysis
```
You: Show me my top 5 campaigns by spend from the last 30 days

GLM: I'll retrieve your campaign data...

Here are your top 5 campaigns:

1. Brand Search - $15,234.56
   Impressions: 234,567
   Clicks: 12,345
   CTR: 5.27%
   Conversions: 1,234
   ROAS: 2.34x

💡 Recommendation: Brand Search has excellent ROAS. Consider 
increasing budget by 15-20% to capture more demand.
```

### Example 2: Ad Creative Review
```
You: Which ad headlines are performing best?

GLM: Let me analyze your ad creative performance...

Top Performing Headlines:
1. "50% Off Today Only" - 4.8% CTR
2. "Free Shipping on Orders Over $50" - 4.2% CTR

Low Performers:
1. "Learn More" - 1.2% CTR

💡 Recommendations:
- Expand top performers to more ad groups
- Test urgency language (limited time offers)
- Consider pausing or improving "Learn More"
```

### Example 3: Custom GAQL Query
```
You: Find keywords with more than 5000 impressions but CTR under 2%

GLM: I'll run a custom GAQL query for you...

Found 8 keywords matching your criteria:

Keyword              | Impressions | Clicks | CTR    | Cost
---------------------|-------------|---------|--------|-------
discount shoes        | 12,456      | 89      | 0.71%  | $45.67
sale footwear       | 9,876       | 78      | 0.79%  | $34.23
...

🎯 Action Plan:
1. Improve ad relevance for better CTR
2. Consider negative keywords if traffic is irrelevant
3. Test more specific match types
```

---

## ⚙️ Configuration Options

### Environment Variables

| Variable | Required? | Description | Default |
|-----------|------------|-------------|---------|
| `ZAI_API_KEY` | ✅ | Your Z.ai API key | - |
| `GOOGLE_ADS_CREDENTIALS_PATH` | ✅ | Path to Google Ads credentials | - |
| `GOOGLE_ADS_DEVELOPER_TOKEN` | ✅ | Google Ads developer token | - |
| `GOOGLE_ADS_AUTH_TYPE` | ❌ | OAuth or service_account | oauth |
| `GOOGLE_ADS_LOGIN_CUSTOMER_ID` | ❌ | Manager account ID | - |
| `GLM_MODEL` | ❌ | GLM model to use | glm-4.7 |
| `ZAI_BASE_URL` | ❌ | API base URL | https://api.z.ai/api/paas/v4/ |

### GLM Models Available

| Model | Parameters | Context | Best For |
|--------|-------------|----------|-----------|
| `glm-4.7` | 355B MoE | 128K tokens | Complex analysis, reasoning |
| `glm-4.6` | - | 200K tokens | Long documents, batch processing |
| `glm-4.5` | 106B MoE | 128K tokens | Fast responses, cost-efficient |
| `glm-4.6v` | - | - | Image analysis |

---

## 🔧 How It Works

1. **You** ask a question in natural language
2. **GLM** analyzes your request and decides which tool to use
3. **GLM Client** sends tool call via JSON-RPC to MCP server
4. **MCP Server** executes the tool against Google Ads API
5. **Results** return to GLM for analysis
6. **GLM** provides insights and recommendations

---

## ❓ Troubleshooting

### Common Issues

**Error: "ZAI_API_KEY not set"**
```bash
# Solution: Set your API key in .env file
echo "ZAI_API_KEY=your_key_here" >> .env
```

**Error: "Google Ads credentials not found"**
```bash
# Solution: Check path is absolute (not relative)
# Correct:
GOOGLE_ADS_CREDENTIALS_PATH=/home/user/credentials.json

# Incorrect:
GOOGLE_ADS_CREDENTIALS_PATH=credentials.json
```

**Error: "ModuleNotFoundError: No module named 'httpx'"**
```bash
# Solution: Install httpx
pip install httpx
```

---

## 🎯 Use Cases

### 1. Performance Analysis
- Weekly/monthly performance reports
- Campaign optimization
- Budget recommendations
- ROAS analysis

### 2. Creative Testing
- A/B test ad headlines
- Compare image assets
- Review ad copy effectiveness

### 3. Keyword Management
- Identify underperforming keywords
- Find new keyword opportunities
- Negative keyword recommendations

### 4. Automation
- Multi-account batch processing
- Scheduled reports
- Automated alerts

---

## 🔗 Links

- **Repository**: https://github.com/nochinsky/google-ads-glm
- **Z.ai Platform**: https://platform.z.ai/
- **Z.ai Documentation**: https://docs.z.ai/
- **GLM Models**: https://github.com/zai-org
- **Google Ads API**: https://developers.google.com/google-ads/api/docs/
- **MCP Protocol**: https://modelcontextprotocol.io/

---

## 📝 License

MIT License - See [LICENSE](LICENSE) file for details.
