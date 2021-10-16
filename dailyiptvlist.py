# Dailyiptvlist scraper
# Made in python
# Scarper by HereIronman7746 / ParrotDevelopers
# Licensed under GPL V3

import requests
import datetime
import os
import shutil

if not os.path.exists('IPTV/'):
    os.system("mkdir IPTV/")
else:
    shutil.rmtree('IPTV/')
    os.system("mkdir IPTV/")

if not os.path.exists('Works/'):
    os.system("mkdir Works/")
else:
    shutil.rmtree('Works/')
    os.system("mkdir Works/")

def Main(state, check):
    def testurl(url, filename):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'
        }

        resp = requests.get(url, headers=headers)
        code = resp.status_code
        if str(code).startswith("2") or str(code).startswith("1") or str(code).startswith("3"): # Check for response status code
            os.system("clear")
        else:
            rm = "rm Works/" + filename
            os.system(rm)



    baseurl = "https://dailyiptvlist.com/dl/" + state + "-m3uplaylist"

    now = datetime.datetime.now()

    dat = now.strftime("-20%y-%m-%d-") # Enable if you want to use today's date
    #dat = now.strftime("-2021-10-15-") # Enable if you want to use custom date

    ur = baseurl + dat

    num = 0
    for l in range(15): # Loop 15 times to get all links
        url = ur + str(l) + ".m3u"
        wget = "wget -P IPTV/ " + url
        if not url.endswith('0.m3u'):
            os.system(wget)
            for filename in os.listdir('IPTV/'):
                if filename.endswith('.html'):
                    rm = "IPTV/" + filename
                    os.remove(rm)
                elif filename.endswith('.m3u'):
                    mv = "mv IPTV/* Works/"
                    os.system(mv)
        if check == True:
            for filename in os.listdir('Works/'):
                fn = "Works/" + filename
                file = open(fn)
                content = file.readlines()
                url_test = content[2]
                testurl(url_test, filename)

    for filename in os.listdir('Works/'): # Counts every file in Works/ folder
        num += 1
        return

    os.system("clear")
    print(str(num) + "worked!")
        



if __name__ == "__main__":
    Main("us", True) 
    # Edit us to any state
    # Edit True to False if you want to disable checking of links in m3u