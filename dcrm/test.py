with open("mydb.py", "rb") as file:
    content = file.read()
    print(content[:10])  # Print the first 10 bytes to check for non-UTF-8 characters
