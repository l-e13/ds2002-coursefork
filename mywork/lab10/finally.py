def write_data_to_file(data, filename):
  try:
    with open(filename, 'w', encoding='utf-8') as file:
      file.write(data)
  except FileNotFoundError as e:
    print(f"Error: File {filename} not found.")
  except PermissionError as e:
    print(f"Error: Permission denied to write to {filename}.")
  finally:
    if 'file' in locals():  # Check if 'file' variable exists (was opened)
      file.close()  # Close the file if it was opened

# Example usage
data = "This is some data to write to the file."
filename = "my_data.txt"
write_data_to_file(data, filename)

# The finally block checks if the file exists and closes it even if an exception occurred.