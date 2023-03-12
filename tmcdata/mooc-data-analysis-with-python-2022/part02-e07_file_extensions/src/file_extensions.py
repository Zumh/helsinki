#!/usr/bin/env python3

def file_extensions(filename):
    file_with_extensions = {}
    file_no_extension = []
    with open(filename, 'r') as files:
        for name in files:
            name = name.strip()
            if '.' in name:
                extension = name.split('.')[-1]
                
                if extension not in file_with_extensions:
                    file_with_extensions[extension] = [name]
                else:
                    file_with_extensions[extension].append(name) 
            else: 
                file_no_extension.append(name)


    return(file_no_extension, file_with_extensions)

def main():
    filename = "filenames.txt"
    no_extensions, with_extensions = file_extensions(filename)
    result = f"{len(no_extensions)} files with no extension\n"
  
    for name, extensions in sorted(with_extensions.items()):
        result += f"{name} {len(extensions)}\n"
    print(result)
if __name__ == "__main__":
    main()
