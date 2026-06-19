# ===== Write Mode =====
with open("notes.txt", "w") as f:
    f.write("Hello Yugandhar\n")
    f.write("Day 15 - File Handling")

with open("notes.txt", "r") as f:
    print(f.read())


# ===== Overwrite Danger =====
with open("notes.txt", "w") as f:
    f.write("New content")

with open("notes.txt", "r") as f:
    print(f.read())


# ===== Append Mode =====
with open("notes.txt", "a") as f:
    f.write("\nAdded this line without deleting old data")

with open("notes.txt", "r") as f:
    print(f.read())


# ===== Line by Line Reading =====
with open("notes.txt", "r") as f:
    for line in f:
        print(line.strip())