import os

def remPYC():
    if os.path.exists("Auth/__pycache__"):
        os.remove("Auth/__pycache__")