import os


if os.path.exists("Assets/Dev/Replit.txt"):
    with open('Assets/Dev/Replit.txt', 'r') as f:
        read = f.read()

    if read == "True":
        replitMode = True
    elif read == "False":
        replitMode = False
    else:
        replitMode = False
else:
    replitMode = False