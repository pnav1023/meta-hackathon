import os
import pandas as pd

# Define the directory containing the 10,000 CSV files
input_directory = "/Users/pranavnarahari/Downloads/HAM10000_images_vectors"
output_file = "combined_output.csv"

# Initialize a list to hold the data for the output CSV
combined_data = []

# Loop through each file in the directory
for idx, file_name in enumerate(os.listdir(input_directory), start=1):
    if file_name.endswith(".csv"):
        file_path = os.path.join(input_directory, file_name)
        
        try:
            # Read the CSV file
            data = pd.read_csv(file_path, header=None)
            
            # Flatten the vector and convert it to a comma-separated string without enclosing quotes
            vector = data.values.flatten()
            embeddings = "[" + ", ".join(map(str, vector)) + "]"
            
            # Append the id and embeddings to the combined data
            combined_data.append({"id": idx, "embeddings": embeddings})
        except Exception as e:
            print(f"Error reading file {file_name}: {e}")

# Convert the combined data into a DataFrame
output_df = pd.DataFrame(combined_data)

# Save the combined data to a single CSV file without quoting the embeddings
output_df.to_csv(output_file, index=False)  
print(f"Combined data saved to {output_file}")
