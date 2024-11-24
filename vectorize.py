from PIL import Image
from transformers import CLIPProcessor, CLIPModel
import torch
import os

def vectorize_image(image_dir):
    model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
    processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

    for filename in os.listdir(image_dir):
        print(filename)
        if filename.lower().endswith(('.jpg')):  # Check for image files
            image_path = os.path.join(image_dir, filename)
            image = Image.open(image_path).convert("RGB")
            # Size of the images are all consistent at 600x450
            # Process the image (e.g., print its size or extract embeddings)
            print(f"Processing {filename}, Size: {image.size}")
            inputs = processor(images=image, return_tensors="pt")
            embeddings = model.get_image_features(**inputs)
            vector = embeddings.detach().numpy()
            with open("/Users/shreyasbyndoor/Documents/dataverse_files/HAM10000_images_vectors/"+filename[:-4]+".csv", "w") as f:
                for value in vector.flatten():
                    f.write(str(value) + ",")
            f.close()
            

if __name__ == "__main__":
    image_dir = "/Users/shreyasbyndoor/Documents/dataverse_files/HAM10000_images/"
    vectorize_image(image_dir)
    