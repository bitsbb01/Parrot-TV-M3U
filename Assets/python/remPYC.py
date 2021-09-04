import os
import shutil

def remPYC():
    if os.path.exists("Auth/__pycache__"):
        shutil.rmtree("Auth/__pycache__")