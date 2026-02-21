from email import parser
import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_functions import available_functions, call_function



load_dotenv()
api_key=os.environ.get("GEMINI_API_KEY")
if api_key is None:
    raise ValueError("GEMINI_API_KEY not found in environment variables.")
client = genai.Client(api_key=api_key)
def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
# Now we can access `args.user_prompt`
    response =client.models.generate_content(
        model="gemini-2.5-flash",
        contents= messages,
        config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt),

    )
    if response.usage_metadata is None:
        raise RuntimeError("Unable to process response.")
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    if response.function_calls is not None:
        function_results=[]
        for fc in response.function_calls:
            print(f"Calling function: {fc.name}({fc.args})")
            function_response = call_function(fc, verbose=args.verbose)
            if not function_response.parts:
                raise Exception("tool result had no parts")
            
            fr = function_response.parts[0].function_response
            if fr is None:
                raise Exception("missing function_response")
            resp = fr.response
            if resp is None:
                raise Exception("missing function_response.response")
            
            function_results.append(function_response.parts[0])

            if args.verbose:
                print(f"-> {resp}")

    else:
        print(response.text)


if __name__ == "__main__":
    main()
