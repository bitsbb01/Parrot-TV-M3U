def config(replit, email, repo, token, name):
    if replit == True:
        global origin
        global config_mail
        global config_name
        origin = "git remote set-url origin https://github:" + str(token) + str(repo) # Gets token and repo from Auth/auth.py
        config_mail = "git config --global user.email " + email
        config_name = "git config --global user.name " + name
    elif replit == False:
        global origin
        global config_mail
        global config_name
        origin = "sudo git remote set-url origin https://github:" + str(token) + str(repo) # Gets token and repo from Auth/auth.py
        config_mail = "sudo git config --global user.email " + email
        config_name = "sudo git config --global user.name " + name
