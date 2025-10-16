#!/usr/bin/env python3
"""
Simple example showing how to use GLM with Google Ads MCP

This is a minimal example to get you started quickly.
"""

import os
import asyncio

# Make sure zai-sdk is installed
try:
    from zai import ZaiClient
except ImportError:
    print("Please install zai-sdk first:")
    print("  pip install zai-sdk")
    exit(1)


async def example_usage():
    """Example of how to use the GLM Google Ads client"""

    # Check for required API key
    api_key = os.environ.get("ZAI_API_KEY")
    if not api_key:
        print("\n" + "=" * 60)
        print("❌ Error: ZAI_API_KEY not set")
        print("=" * 60)
        print("\nPlease set your Z.ai API key:")
        print("  export ZAI_API_KEY='your_api_key_here'")
        print("\nOr get a key at: https://docs.z.ai/")
        return

    # Initialize GLM client
    print("\n" + "=" * 60)
    print("🚀 Initializing GLM-4.7 Google Ads Assistant")
    print("=" * 60 + "\n")

    # Simple example: Ask GLM to list accounts
    client = ZaiClient(api_key=api_key)

    # Example 1: Chat with GLM (without tools yet)
    print("Example 1: Basic Chat")
    print("-" * 60)

    response = client.chat.completions.create(
        model="glm-4.7",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful Google Ads assistant. Be concise and friendly.",
            },
            {
                "role": "user",
                "content": "Hello! Can you help me with Google Ads analysis?",
            },
        ],
        max_tokens=500,
    )

    print(f"GLM: {response.choices[0].message.content}\n")

    # Example 2: With tool definitions (schema)
    print("\nExample 2: With Google Ads Tools")
    print("-" * 60)

    tools = [
        {
            "type": "function",
            "function": {
                "name": "list_accounts",
                "description": "List all accessible Google Ads accounts",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }
    ]

    response = client.chat.completions.create(
        model="glm-4.7",
        messages=[
            {
                "role": "system",
                "content": "You are a Google Ads assistant with access to tools.",
            },
            {"role": "user", "content": "List my Google Ads accounts"},
        ],
        tools=tools,
        max_tokens=500,
    )

    print(f"GLM: {response.choices[0].message.content}")

    if response.choices[0].message.tool_calls:
        print("\nTool calls requested:")
        for tool_call in response.choices[0].message.tool_calls:
            print(f"  - {tool_call.function.name}")
            print(f"    Args: {tool_call.function.arguments}")

    print("\n" + "=" * 60)
    print("✅ Examples completed!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Set up your Google Ads credentials in .env file")
    print("2. Run the full client: python glm_google_ads_client.py")
    print("3. Ask questions about your campaigns, ads, or performance")
    print("\n" + "=" * 60)


if __name__ == "__main__":
    asyncio.run(example_usage())
