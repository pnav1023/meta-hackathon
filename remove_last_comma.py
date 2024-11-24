import os

def remove_trailing_commas(directory):
    iterate_count = 0
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):  # Process only CSV files
            print(iterate_count)
            file_path = os.path.join(directory, filename)
            with open(file_path, "r") as f:
                lines = f.readlines()
            
            # Remove trailing commas from each line
            cleaned_lines = [line.rstrip(",") + "\n" for line in lines]

            # Write the cleaned lines back to the file
            with open(file_path, "w") as f:
                f.writelines(cleaned_lines)
            iterate_count += 1

# Specify the directory containing the CSV files
csv_directory = "/Users/shreyasbyndoor/Documents/dataverse_files/HAM10000_images_vectors/"
remove_trailing_commas(csv_directory)

print("Trailing commas removed from all CSV files in the directory.")