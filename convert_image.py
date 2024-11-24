from wand.image import Image

def heic_to_png(input_path, output_path):
    with Image(filename=input_path) as img:
        img.format = 'png'
        img.save(filename=output_path)
        print(f"Converted {input_path} to {output_path}")

heic_to_png('uploaded_image.heic', 'converted_image.png')
