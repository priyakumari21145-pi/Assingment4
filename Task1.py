try:
    
    with open("sample.txt", "r") as file:
        print("Reading file content:\n")
        lines = file.readlines()
        
        
        for i, line in enumerate(lines, start=1):
            print(f"Line {i}: {line.strip()}")


except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
