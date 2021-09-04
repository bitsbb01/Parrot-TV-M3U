import os
import shutil

def remPYC():
    if os.path.exists("Auth/__pycache__"):
        shutil.rmtree("Auth/__pycache__")

    if os.path.exists("Assets/python/__pycache__"):
        shutil.rmtree("Assets/python/__pycache__")

    if os.path.exists("Assets/USTVGO/scripts/__pycache__"):
        shutil.rmtree("Assets/USTVGO/scripts/__pycache__")

    if os.path.exists("__pycache__"):
        shutil.rmtree("__pycache__")
