import os

def create_directories_with_files():
    for day in range(1, 26):
        directory_name = f"day_{day}"
        os.makedirs(directory_name, exist_ok=True)
        print(f"Directory '{directory_name}' created.")
        
        file_path = os.path.join(directory_name, "puzzle_input.txt")
        with open(file_path, 'w') as file:
            file.write("")
        print(f"File 'puzzle_input.txt' added to '{directory_name}'.")

if __name__ == "__main__":
    create_directories_with_files()