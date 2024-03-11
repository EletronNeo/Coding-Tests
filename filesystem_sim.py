user_input = input("Enter your name: ")

# Use the input
print("Hello, " + user_input + "!")

class File:
    def __init__(self, name):
        self.name = name

class Directory:
    def __init__(self, name):
        self.name = name
        self.subdirectories = []
        self.files = []

class FileSystem:
    def __init__(self):
        self.root = Directory('/')
        self.current_directory = self.root

    def ls(self):
        print("Directories:")
        for directory in self.current_directory.subdirectories:
            print(directory.name)
        print("Files:")
        for file in self.current_directory.files:
            print(file.name)

    def mkdir(self, directory_name):
        new_directory = Directory(directory_name)
        self.current_directory.subdirectories.append(new_directory)

    def cd(self, directory_name):
        if directory_name == '..':
            if self.current_directory != self.root:
                self.current_directory = self.get_parent_directory(self.current_directory)
        else:
            found = False
            for directory in self.current_directory.subdirectories:
                if directory.name == directory_name:
                    self.current_directory = directory
                    found = True
                    break
            if not found:
                print("Directory does not exist.")

        print("Usage: cd <directory_name>")
        elif command[0] == 'touch':
            if len(command) > 1:
                fs.touch(command[1])
            else:
                print("Usage: touch <file_name>")
        elif command[0] == 'rmdir':
            if len(command) > 1:
                fs.rmdir(command[1])
            else:
                print("Usage: rmdir <directory_name>")
        elif command[0] == 'temp':
            if len(command) > 1:
                fs.touch(command[1], temporary=True)
            else:
                print("Usage: temp <temporary_file_name>")

    def get_parent_directory(self, directory):
        current_dir = self.root
        path = []
        while current_dir != directory:
            path.append(current_dir)
            for subdirectory in current_dir.subdirectories:
                if directory in subdirectory.subdirectories or directory in subdirectory.files:
                    current_dir = subdirectory
                    break
        return path[-1]


if __name__ == "__main__":
    fs = FileSystem()

    while True:
        command = input("Enter command (ls, mkdir, cd, touch, exit): ").split()

        if command[0] == 'ls':
            fs.ls()
        elif command[0] == 'mkdir':
            if len(command) > 1:
                fs.mkdir(command[1])
            else:
                print("Usage: mkdir <directory_name>")
        elif command[0] == 'cd':
            if len(command) > 1:
                fs.cd(command[1])
            else:
                print("Usage: cd <directory_name>")
        elif command[0] == 'touch':
            if len(command) > 1:
                fs.touch(command[1])
            else:
                print("Usage: touch <file_name>")
        elif command[0] == 'exit':
            print("Exiting file system simulation.")
            break
        else:
            print("Invalid command. Supported commands are ls, mkdir, cd, touch, exit.")
