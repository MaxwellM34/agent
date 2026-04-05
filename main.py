import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types



def main():
    print("Hello from agent!")

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key:
        print("API Key loaded successfully.")
    else:
        raise RuntimeError("API Key not found. Please set GEMINI_API_KEY in your .env file.")
        
    client = genai.Client(api_key=api_key)
    prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    # Now we can access `args.user_prompt`
    response = client.models.generate_content(
        model='gemini-2.5-flash', contents=messages
    )

    if response.usage_metadata:
        print(f"Response:\n{response.text}")
        if args.verbose == True:
            print(f"User prompt: {args.user_prompt}\n")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}\nResponse tokens: {response.usage_metadata.candidates_token_count}")
    else:
        raise RuntimeError("Response was not generated")
        
if __name__ == "__main__":
    main()
