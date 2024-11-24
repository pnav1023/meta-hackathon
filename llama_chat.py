import json
from llamaapi import LlamaAPI
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize the SDK
llama = LlamaAPI(os.environ["LLAMA_API_KEY"])

# Build the API request
api_request_json = {
    "model": "llama3.1-70b",
    "messages": [
        {"role": "user", "content": f"What skin ailments, if any, can you identify from this image: {image}"},
    ],
    "functions": [
        {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    },
                    "days": {
                        "type": "number",
                        "description": "for how many days ahead you wants the forecast",
                    },
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                },
            },
            "required": ["location", "days"],
        }
    ],
    "stream": False,
    "function_call": "get_current_weather",
}

# Execute the Request
response = llama.run(api_request_json)
print(json.dumps(response.json(), indent=2))
