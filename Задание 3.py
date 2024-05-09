import os

files = ["1.txt", "2.txt", "3.txt"]

file_counts = {}

for file in files:
    with open(file, "r") as f:
        file_counts[file] = len(f.readlines())

sorted_files = sorted(files, key=lambda x: file_counts[x])

with open("combined.txt", "w") as output:
    for file in sorted_files:
        output.write(f"{file}\n{file_counts[file]}\n")

        with open(file, "r") as f:
            output.write(f.read())