# Google Ads + GLM Integration Quick Start

This guide will get you up and running with GLM-4.7 and Google Ads in 5 minutes.

## 🚀 Quick Setup (5 minutes)

### Step 1: Get Z.ai API Key (1 minute)

1. Go to [Z.ai Open Platform](https://docs.z.ai/)
2. Sign up or log in
3. Navigate to API Keys section
4. Create a new API key
5. Copy it somewhere safe

### Step 2: Get Google Ads Credentials (2-3 minutes)

**Option A: Service Account (Recommended for automation)**

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a project or select existing one
3. Enable Google Ads API
4. Go to Credentials → Create Credentials → Service Account
5. Download the JSON key file
6. Grant the service account access to your Google Ads accounts
7. Apply for [Developer Token](https://ads.google.com/aw/apicenter)

**Option B: OAuth 2.0 (Good for personal use)**

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Enable Google Ads API
3. Create OAuth Client ID (Desktop Application type)
4. Download client configuration
5. Apply for [Developer Token](https://ads.google.com/aw/apicenter)

### Step 3: Configure Environment (1 minute)

```bash
# Copy the GLM template
cp .env.example.glm .env

# Edit with your favorite editor
nano .env  # or: notepad .env (Windows)
```

Add your credentials to `.env`:

```env
# Z.ai (required)
ZAI_API_KEY=zai_your_api_key_here

# Google Ads (required)
GOOGLE_ADS_CREDENTIALS_PATH=/full/path/to/your/credentials.json
GOOGLE_ADS_DEVELOPER_TOKEN=your_google_ads_developer_token
GOOGLE_ADS_AUTH_TYPE=service_account
GOOGLE_ADS_LOGIN_CUSTOMER_ID=your_manager_account_id_if_applicable

# Optional: Choose GLM model
GLM_MODEL=glm-4.7
```

### Step 4: Install Dependencies (1 minute)

```bash
# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install requirements
pip install -r requirements.txt
```

### Step 5: Test Connection (1 minute)

```bash
# Run example to verify API key
python example_usage.py
```

You should see:
```
🚀 Initializing GLM-4.7 Google Ads Assistant
============================================================

Example 1: Basic Chat
------------------------------------------------------------
GLM: Hello! I'd be happy to help you with Google Ads analysis...

✅ Examples completed!
```

### Step 6: Start Analyzing! (30 seconds)

```bash
# Interactive mode - chat with GLM
python glm_google_ads_client.py

# Or ask a single question
python glm_google_ads_client.py -m "What are my top performing campaigns?"
```

## 💬 Example Conversations

### Conversation 1: Campaign Performance

```
You: Show me my top 5 campaigns by spend this month

GLM: I'll retrieve your campaign performance data...
[GLM calls list_accounts tool]
[GLM calls get_campaign_performance tool]

Here are your top 5 campaigns by cost over the last 30 days:

📊 Campaign Performance Analysis
────────────────────────────────────

1. Brand Search - $15,234.56
   Impressions: 234,567
   Clicks: 12,345
   CTR: 5.27%
   Conversions: 1,234
   ROAS: 2.34x

   💡 Insight: Strong performance with healthy ROAS. Consider
      increasing budget by 15-20% to capture more demand.

2. Product Discovery - $12,890.45
   Impressions: 456,789
   Clicks: 8,765
   CTR: 1.92%
   Conversions: 456
   ROAS: 1.87x

   💡 Insight: Lower CTR suggests ad creative optimization
      needed. Test different headlines or images.

[Continues with analysis and recommendations...]
```

### Conversation 2: Ad Creative Review

```
You: Analyze my ad headlines and tell me which are performing best

GLM: Let me analyze your ad creative performance...
[Retrieves ad data]

🎯 Ad Headline Performance
────────────────────────────

Top Performing Headlines:
────────────────────────────────

1. "Limited Time: 50% Off Today Only" - 4.8% CTR
   Used in: 12 ad groups
   Total impressions: 89,234
   Total clicks: 4,276
   Conversions: 445

2. "Free Shipping - No Minimum Order" - 4.2% CTR
   Used in: 8 ad groups
   Total impressions: 56,789
   Total clicks: 2,385
   Conversions: 298

Lowest Performing Headlines:
────────────────────────────────

1. "Learn More" - 1.2% CTR
   Used in: 15 ad groups
   Total impressions: 123,456
   Total clicks: 1,481
   Conversions: 67

💡 Recommendations:
──────────────────

• Test urgency language: Top performers use time-limited offers
• Expand "Free Shipping" to more ad groups (high CTR)
• Pause or improve "Learn More" (low performance)
• A/B test: "50% Off" vs "40% Off" to find optimal discount
```

### Conversation 3: Custom GAQL Query

```
You: Find keywords with more than 5000 impressions but CTR under 1%

GLM: I'll run a custom GAQL query to find underperforming keywords...
[Executes GAQL query]

🔍 Underperforming Keywords
────────────────────────────

Found 8 keywords with high impressions but low CTR:

Keyword              | Impressions | Clicks | CTR    | Cost     | Conv
─────────────────────|──────────────|─────────|──────────|──────────|──────
shoes cheap         | 12,456      | 89      | 0.71%   | $45.67  | 2
discount footwear   | 9,876       | 78      | 0.79%   | $34.23  | 1
buy shoes online     | 8,234       | 65      | 0.79%   | $28.91  | 1
...

📈 Action Plan:
────────────────

1. **Improve Ad Relevance** (CTR < 1% despite high impressions)
   - Review search terms triggering these keywords
   - Add negative keywords for irrelevant queries
   - Improve landing page experience

2. **Bid Optimization**
   - Lower bids on underperforming keywords
   - Redirect budget to high-performing terms

3. **Keyword Expansion**
   - Consider more specific match types
   - Test long-tail variations

Total wasted spend on these keywords: $234.56
Potential savings with optimization: ~$150-200/month
```

## 🎯 Common Use Cases

### Use Case 1: Weekly Performance Review

```
You: Give me a comprehensive report of last week's performance

GLM will:
1. Get all accounts
2. Retrieve campaign data
3. Analyze ad performance
4. Check creative metrics
5. Summarize with insights and recommendations
```

### Use Case 2: Budget Optimization

```
You: Which campaigns should I increase/decrease budget for?

GLM will:
1. Analyze ROAS across campaigns
2. Identify high-performing but budget-limited campaigns
3. Find campaigns with poor ROAS
4. Recommend budget allocations
```

### Use Case 3: Creative A/B Testing

```
You: Help me design a test for new ad headlines

GLM will:
1. Review current top performers
2. Suggest new headline variations
3. Set up test structure
4. Define success metrics
```

### Use Case 4: Seasonal Planning

```
You: How should I prepare for the holiday season?

GLM will:
1. Analyze last year's holiday performance
2. Identify seasonal trends
3. Recommend budget increases
4. Suggest holiday-specific creative
```

## 🔧 Advanced Features

### Feature 1: Batch Analysis

Create a script to analyze multiple accounts:

```python
# batch_analysis.py
import asyncio
from glm_google_ads_client import GLMMCPClient

accounts = ["1234567890", "0987654321"]
client = GLMMCPClient()

for account in accounts:
    result = await client.chat(
        f"Analyze top campaigns for account {account}"
    )
    print(f"\n=== Account {account} ===\n{result}")
```

Run it:
```bash
python batch_analysis.py > monthly_report.txt
```

### Feature 2: Automated Reports

Schedule daily/weekly reports:

```python
# Use cron (Linux/Mac) or Task Scheduler (Windows)

# Run every Monday at 9 AM
0 9 * * 1 /path/to/weekly_report.sh

# weekly_report.sh
#!/bin/bash
cd /path/to/Google-ADS-GLM
source .venv/bin/activate
python glm_google_ads_client.py -m "Generate weekly performance report" > reports/week_$(date +%Y%m%d).txt
```

### Feature 3: Integration with Other Tools

Export data for further analysis:

```python
# Export to CSV
result = await client.chat(
    "Get campaign performance as CSV for account 1234567890"
)

# GLM can call run_gaql with format="csv"
# The output can be imported to Excel, Google Sheets, etc.
```

## ❓ FAQ

**Q: Do I need Claude Desktop or Cursor?**
A: No! This is a standalone client. Just run the Python script.

**Q: Can I use this with my existing mcp-google-ads setup?**
A: Yes! If you already have mcp-google-ads working with Claude, you can just add the GLM client on top. Share the same `.env` file.

**Q: What's the cost?**
A: Z.ai charges per token. A typical conversation with tool calls costs ~$0.01-0.05. See [Z.ai Pricing](https://docs.z.ai/) for details.

**Q: Is my data safe?**
A: Your Google Ads data goes directly from Google to the MCP server. GLM only sees the results you ask for. Nothing is stored or sent to Z.ai beyond your current request.

**Q: Can I use other GLM models?**
A: Yes! Set `GLM_MODEL=glm-4.6` or `glm-4.5` in your `.env` file.

**Q: What if I hit rate limits?**
A: The MCP server handles Google Ads rate limiting. If you see errors:
- Wait a few minutes and retry
- Use more specific queries (less data to fetch)
- Consider upgrading your Google Ads API access tier

## 🆘 Troubleshooting

**Problem**: `ModuleNotFoundError: No module named 'zai'`
```bash
pip install zai-sdk
```

**Problem**: `FileNotFoundError: MCP server not found`
```bash
# Ensure you're in the correct directory
ls -la google_ads_server.py

# Should see the file
```

**Problem**: `Error: Invalid credentials`
```bash
# Check your .env file
cat .env

# Verify paths are absolute (not relative)
GOOGLE_ADS_CREDENTIALS_PATH=/home/user/Google-ADS-GLM/credentials.json  # ✓
GOOGLE_ADS_CREDENTIALS_PATH=credentials.json  # ✗ Use full path
```

**Problem**: `Error: Developer token required`
```
# Apply for a developer token at:
https://ads.google.com/aw/apicenter

# Note: Test tokens have limitations
```

## 📚 Next Steps

Now that you're set up:

1. **Explore**: Try different questions about your Google Ads data
2. **Automate**: Create batch scripts for regular reporting
3. **Integrate**: Combine with your existing workflows
4. **Customize**: Modify the client for your specific needs

For more advanced usage, see [README_GLM.md](README_GLM.md)

## 🎉 Success!

You're now ready to analyze your Google Ads data with GLM-4.7!

Start the conversation:
```bash
python glm_google_ads_client.py
```

Ask GLM anything:
- "How are my campaigns performing?"
- "Which ads have the best CTR?"
- "Run a query to find top converting keywords"
- "Analyze my image asset performance"
- "What would you recommend to improve my ROAS?"

Happy analyzing! 📊
