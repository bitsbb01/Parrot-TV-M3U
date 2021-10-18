def config(replit, email, repo, token, name):
    global origin
    global config_mail
    global config_name
    origin = ""
    config_name = ""
    config_mail = ""
    if replit == True:
        origin = "git remote set-url origin https://github:" + str(token) + str(repo) # Gets token and repo from Auth/auth.py
        config_mail = "git config --global user.email " + email
        config_name = "git config --global user.name " + name
    elif replit == False:
        origin = "sudo git remote set-url origin https://github:" + str(token) + str(repo) # Gets token and repo from Auth/auth.py
        config_mail = "sudo git config --global user.email " + email
        config_name = "sudo git config --global user.name " + name
