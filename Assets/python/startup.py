import os


if os.path.exists("Assets/Dev/Startup.txt"):
    with open('Assets/Dev/Startup.txt', 'r') as f:
        read = f.read()

    if read == "True":
       startup = True
    elif read == "False":
       startup = False
    else:
       startup = False
else:
   startup = False