import os
from groq import Groq
from dotenv import load_dotenv
import argparse
import base64

def assess_image(image, locationOnBody="leg", age="55"):
    load_dotenv()
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user", 
                "content": f"What skin ailments, if any, can you identify from this image: {image}. The user is {age} years old and the location of the image is {locationOnBody}"
            }
        ],
        model="llama-3.2-11b-vision-preview",
    )

    print(chat_completion.choices[0].message.content)

def main():
    parser = argparse.ArgumentParser(description="Assess an image for skin ailments.")
    parser.add_argument("image_path", type=str, help="Path to the image file")
    parser.add_argument("--location", type=str, default="leg", help="Location on the body")
    parser.add_argument("--age", type=str, default="55", help="Age of the user")
    
    args = parser.parse_args()

    with open(args.image_path, "rb") as image_file:
        assess_image(base64.b64encode(image_file.read()).decode('utf-8'), args.location, args.age)

if __name__ == "__main__":
    main()
