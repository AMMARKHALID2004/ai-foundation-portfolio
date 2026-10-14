def read_large_file(file):
    with open(file) as f:
        for line in f:
            print("[source reading line]")
            yield line


file_path="Projects/file.txt"

read_file=read_large_file(file_path)

print(next(read_file))
print(next(read_file))
