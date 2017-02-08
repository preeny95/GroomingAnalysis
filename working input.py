with open('chat.txt') as f:
    found = False
    for line in f:
        line = line.lower()
        if w in line:
            print(line)
            found = True
    if not found:
        print("not here")
