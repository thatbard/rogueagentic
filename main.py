import os
from dotenv import load_dotenv
from google import genai

model = "gemini-2.5-flash"

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key == None:
        raise RuntimeError("failed to load GEMINI_API_KEY")
    
    client = genai.Client(api_key=api_key)
    request = "How much wood would a wood-chuck chuck if a wood-chuck could chuck wood?"
    response = client.models.generate_content(model=model, contents=request)

    if response.usage_metadata == None:
        raise RuntimeError("no usage_metadata found")
    
    print(f"User request: {request}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print(f"Model response: {response.text}")


if __name__ == "__main__":
    main()
