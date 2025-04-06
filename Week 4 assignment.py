def read_and_modify_file():
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' was not found.")
        return
    except IOError:
        print(f"❌ Error: Cannot read the file '{filename}'.")
        return

    # Modify the content (example: convert to uppercase)
    modified_content = content.upper()

    # Create new filename
    new_filename = f"modified_{filename}"

    try:
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
        print(f"✅ Success: Modified content written to '{new_filename}'")
    except IOError:
        print(f"❌ Error: Cannot write to the file '{new_filename}'.")

# Run the function
read_and_modify_file()
