#!/usr/bin/env python3
"""
GLM Client for Google Ads MCP Server - Direct HTTP API Version

This version bypasses the zai-sdk dependency issue by using
HTTP requests directly to Z.ai's API instead of their SDK.
"""

import os
import sys
import json
import asyncio
import subprocess
from typing import Any, Dict, List, Optional

try:
    import httpx
except ImportError:
    print("Error: httpx not installed. Install with:")
    print("  pip install httpx")
    sys.exit(1)


class DirectGLMClient:
    """GLM client using direct HTTP API calls (bypassing zai-sdk)"""

    def __init__(self, api_key: Optional[str] = None, model: str = "glm-4.7"):
        """
        Initialize GLM client with direct HTTP calls

        Args:
            api_key: Z.ai API key (if None, loads from environment)
            model: GLM model to use (default: glm-4.7)
        """
        self.api_key = api_key or os.environ.get("ZAI_API_KEY")
        if not self.api_key:
            raise ValueError(
                "ZAI_API_KEY not set. Set it as environment variable "
                "or pass it as parameter."
            )

        self.model = model
        self.base_url = os.environ.get("ZAI_BASE_URL", "https://api.z.ai/api/paas/v4")
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    def _get_tool_definitions(self) -> List[Dict[str, Any]]:
        """Get tool definitions for Google Ads MCP"""
        return [
            {
                "type": "function",
                "function": {
                    "name": "list_accounts",
                    "description": "List all accessible Google Ads accounts",
                    "parameters": {"type": "object", "properties": {}, "required": []},
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "get_account_currency",
                    "description": "Get the default currency code for a Google Ads account",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "customer_id": {
                                "type": "string",
                                "description": "Google Ads customer ID (10 digits, no dashes)",
                            }
                        },
                        "required": ["customer_id"],
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "get_campaign_performance",
                    "description": "Get campaign performance metrics for specified time period",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "customer_id": {
                                "type": "string",
                                "description": "Google Ads customer ID (10 digits, no dashes)",
                            },
                            "days": {
                                "type": "integer",
                                "description": "Number of days to look back",
                                "default": 30,
                            },
                        },
                        "required": ["customer_id"],
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "get_ad_performance",
                    "description": "Get ad performance metrics for specified time period",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "customer_id": {
                                "type": "string",
                                "description": "Google Ads customer ID (10 digits, no dashes)",
                            },
                            "days": {
                                "type": "integer",
                                "description": "Number of days to look back",
                                "default": 30,
                            },
                        },
                        "required": ["customer_id"],
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "run_gaql",
                    "description": "Execute any arbitrary GAQL query with custom formatting",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "customer_id": {
                                "type": "string",
                                "description": "Google Ads customer ID (10 digits, no dashes)",
                            },
                            "query": {
                                "type": "string",
                                "description": "Valid GAQL query string",
                            },
                            "format": {
                                "type": "string",
                                "description": "Output format: 'table', 'json', or 'csv'",
                                "default": "table",
                            },
                        },
                        "required": ["customer_id", "query"],
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "get_ad_creatives",
                    "description": "Get ad creative details including headlines, descriptions, and URLs",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "customer_id": {
                                "type": "string",
                                "description": "Google Ads customer ID (10 digits, no dashes)",
                            }
                        },
                        "required": ["customer_id"],
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "get_image_assets",
                    "description": "Retrieve all image assets in account including their full-size URLs",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "customer_id": {
                                "type": "string",
                                "description": "Google Ads customer ID (10 digits, no dashes)",
                            },
                            "limit": {
                                "type": "integer",
                                "description": "Maximum number of image assets to return",
                                "default": 50,
                            },
                        },
                        "required": ["customer_id"],
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "analyze_image_assets",
                    "description": "Analyze image assets with their performance metrics across campaigns",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "customer_id": {
                                "type": "string",
                                "description": "Google Ads customer ID (10 digits, no dashes)",
                            },
                            "days": {
                                "type": "integer",
                                "description": "Number of days to look back",
                                "default": 30,
                            },
                        },
                        "required": ["customer_id"],
                    },
                },
            },
        ]

    async def chat(
        self, user_message: str, conversation_history: Optional[List[Dict]] = None
    ) -> str:
        """
        Chat with GLM model about Google Ads data

        Args:
            user_message: The user's message/question
            conversation_history: Previous messages in the conversation

        Returns:
            GLM's response
        """
        messages = conversation_history or []
        messages.append(
            {
                "role": "system",
                "content": (
                    "You are a helpful AI assistant for Google Ads analysis. "
                    "You have access to tools that can retrieve Google Ads data. "
                    "When the user asks about their Google Ads campaigns, ads, or performance, "
                    "use the appropriate tools to get the data, then analyze and present it "
                    "in a clear, actionable way. Always explain what data you're retrieving "
                    "and provide insights about the results."
                ),
            }
        )
        messages.append({"role": "user", "content": user_message})

        try:
            # Make API call to Z.ai
            async with httpx.AsyncClient(timeout=60.0) as client:
                payload = {
                    "model": self.model,
                    "messages": messages,
                    "tools": self._get_tool_definitions(),
                    "temperature": 0.7,
                    "max_tokens": 2000,
                }

                response = await client.post(
                    f"{self.base_url}/chat/completions",
                    headers=self.headers,
                    json=payload,
                )

                if response.status_code != 200:
                    return f"Error from Z.ai API: HTTP {response.status_code}"

                result = response.json()

                # Handle tool calls if present
                if "choices" in result and len(result["choices"]) > 0:
                    message = result["choices"][0]["message"]

                    if "tool_calls" in message and message["tool_calls"]:
                        # Execute tools
                        tool_results = []
                        for tool_call in message["tool_calls"]:
                            tool_name = tool_call["function"]["name"]
                            tool_args = json.loads(tool_call["function"]["arguments"])

                            # Call the MCP server
                            result = await self.call_mcp_server(tool_name, tool_args)
                            tool_results.append(
                                {"tool_call_id": tool_call["id"], "result": result}
                            )

                        # Send tool results back to GLM
                        messages.append(message)
                        for tool_result in tool_results:
                            messages.append(
                                {
                                    "role": "tool",
                                    "tool_call_id": tool_result["tool_call_id"],
                                    "content": tool_result["result"],
                                }
                            )

                        # Get final response
                        final_response = await client.post(
                            f"{self.base_url}/chat/completions",
                            headers=self.headers,
                            json={
                                "model": self.model,
                                "messages": messages,
                                "temperature": 0.7,
                                "max_tokens": 2000,
                            },
                        )

                        if final_response.status_code == 200:
                            final_result = final_response.json()
                            if (
                                "choices" in final_result
                                and len(final_result["choices"]) > 0
                            ):
                                return final_result["choices"][0]["message"]["content"]
                            else:
                                return "No response from GLM after tool execution"
                        else:
                            return f"Error from Z.ai API: HTTP {final_response.status_code}"

                    elif "content" in message:
                        return message["content"]
                    else:
                        return "No content or tool calls in GLM response"

                else:
                    return "No choices in GLM response"

        except Exception as e:
            return f"Error communicating with GLM: {str(e)}"

    async def call_mcp_server(self, tool_name: str, arguments: Dict[str, Any]) -> str:
        """
        Call the MCP server with a specific tool and arguments

        Args:
            tool_name: Name of the MCP tool to call
            arguments: Dictionary of arguments to pass to the tool

        Returns:
            Result from the MCP server as string
        """
        server_path = os.path.join(os.path.dirname(__file__), "google_ads_server.py")

        if not os.path.exists(server_path):
            return f"Error: MCP server not found at {server_path}"

        # Create JSON-RPC request
        request = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "tools/call",
            "params": {"name": tool_name, "arguments": arguments},
        }

        try:
            # Set environment variables for Google Ads credentials
            env = os.environ.copy()

            # Run MCP server as subprocess and communicate via stdio
            process = await asyncio.create_subprocess_exec(
                sys.executable,
                [server_path],
                stdin=asyncio.subprocess.PIPE,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                env=env,
            )

            # Send request
            request_json = json.dumps(request) + "\n"
            process.stdin.write(request_json.encode())
            await process.stdin.drain()
            process.stdin.close()

            # Read response
            response_data = await process.stdout.read()

            # Wait for process to finish
            await process.wait()

            if not response_data:
                return "No response from MCP server"

            # Parse response
            response = json.loads(response_data.decode())

            if "result" in response:
                return response["result"]["content"][0]["text"]
            elif "error" in response:
                return f"MCP Server Error: {response['error']}"
            else:
                return "Unknown error from MCP server"

        except Exception as e:
            return f"Error calling MCP server: {str(e)}"

    async def interactive_mode(self):
        """Run in interactive chat mode"""
        print("\n" + "=" * 60)
        print("GLM-4.7 Google Ads Assistant (Direct API Version)")
        print("=" * 60)
        print("\nType 'quit' or 'exit' to end the session.")
        print("You can ask about your Google Ads campaigns, ads, or performance, etc.")
        print("-" * 60 + "\n")

        conversation_history = []

        while True:
            try:
                user_input = input("\nYou: ").strip()

                if user_input.lower() in ["quit", "exit", "q"]:
                    print("\nGoodbye! 👋\n")
                    break

                if not user_input:
                    continue

                print("\nGLM: ", end="", flush=True)
                response = await self.chat(user_input, conversation_history)
                print(response)

                # Add to conversation history (keep last 10 messages)
                conversation_history.append({"role": "user", "content": user_input})
                conversation_history.append({"role": "assistant", "content": response})
                if len(conversation_history) > 20:
                    conversation_history = conversation_history[-20:]

            except KeyboardInterrupt:
                print("\n\nSession interrupted. Type 'quit' to exit properly.\n")
            except Exception as e:
                print(f"\nError: {str(e)}\n")


def main():
    """Main entry point"""
    import argparse

    parser = argparse.ArgumentParser(
        description="GLM-4.7 Client for Google Ads MCP Server (Direct API Version)"
    )
    parser.add_argument(
        "--api-key", help="Z.ai API key (optional if ZAI_API_KEY env var is set)"
    )
    parser.add_argument(
        "--model", default="glm-4.7", help="GLM model to use (default: glm-4.7)"
    )
    parser.add_argument(
        "--message", "-m", help="Single message to send instead of interactive mode"
    )

    args = parser.parse_args()

    try:
        client = DirectGLMClient(api_key=args.api_key, model=args.model)

        if args.message:
            # Single message mode
            import asyncio

            response = asyncio.run(client.chat(args.message))
            print(response)
        else:
            # Interactive mode
            asyncio.run(client.interactive_mode())

    except ValueError as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
