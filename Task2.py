import os
FILE_NAME = "output.txt"

def solve_file_io_task():
    
    
    print(f"--- Starting File Handling Process with {FILE_NAME} ---")

    initial_text = input("Enter text to write to the file: ") + "\n"
    
    try:
        with open(FILE_NAME, 'w') as file:
            file.write(initial_text)
        print(f"Data successfully written to {FILE_NAME}.")
    except IOError as e:
        print(f"An error occurred while writing: {e}")
        return 
        
    print("-" * 30)
    additional_text = input("Enter additional text to append: ")
    
    try:
        with open(FILE_NAME, 'a') as file:
            file.write(additional_text)
        print("Data successfully appended.")
    except IOError as e:
        print(f"An error occurred while appending: {e}")
        
    print("-" * 30)

    
    
    print(f"Final content of {FILE_NAME}:")
    try:
        with open(FILE_NAME, 'r') as file:
            final_content = file.read()
        
            print(final_content.strip()) 
    except FileNotFoundError:
        print(f"Error: The file {FILE_NAME} was not found.")
    except IOError as e:
        print(f"An error occurred while reading: {e}")
        
    print("-" * 30)
    
    
solve_file_io_task()