# -*- coding: utf-8 -*-

# Nastavení
# Počet dní (1-15)
days = 15

# Počet dní zpětně (0-7)
days_back = 7

# Výběr zdroje kanálů
# 1 = povolit
# 0 = zakázat
TV_SMS_CZ = 1
T_MOBILE_TV_GO = 0
O2_TV_SPORT = 0
MUJ_TV_PROGRAM_CZ = 1

# Seznam vlastních kanálů pro tv.sms.cz a T-Mobile TV Go
# Seznam číselných id kanálů oddělené čárkou (např.: "2,3,32,94")
# Pro všechny kanály ponechte prázdné
TV_SMS_CZ_IDS = ""
T_MOBILE_TV_GO_IDS = ""

#Časový posun (+/-hodina)
time_shift = +2

#Nahrát EPG na ftp server
#Ano = 1
#Ne = 0
ftp_upload = 0
ftp_server = "server.cz"
ftp_port = 21
ftp_login = "login"
ftp_password = "heslo"
ftp_folder = "/"


import sys
import os
import xmltv
import requests
import xml.etree.ElementTree as ET
import unicodedata
import time
from urllib.parse import quote
from datetime import datetime, timedelta, date
from ftplib import FTP


dn = os.path.dirname(os.path.realpath(__file__))
fn = os.path.join(dn,"../EPG.xml")
custom_names_path = os.path.join(dn,"custom_names.txt")
t_s = "%+d" % time_shift
TS = " " +t_s[0] + "0" + t_s[1] + "00"


def encode(string):
    string = str(unicodedata.normalize('NFKD', string).encode('ascii', 'ignore'), "utf-8")
    return string


custom_names = []
try:
    f = open(custom_names_path, "r", encoding="utf-8").read().splitlines()
    for x in f:
        x = x.split("=")
        custom_names.append((x[0], x[1]))
except:
    pass


def replace_names(value):
    for v in custom_names:
        if v[0] == value:
            value = v[1]
    return value


def get_muj_tv_programmes(ids, d, d_b):
    if d_b > 1:
        d_b = 1
    if d > 10:
        d = 10
    channels = []
    programmes = []
    ids_ = {"723": "723-skylink-7", "233": "233-stingray-classica", "234": "234-stingray-iconcerts", "110": "110-stingray-cmusic"}
    if "723" in ids:
        channels.append({'display-name': [(replace_names('Skylink 7'), u'cs')], 'id': '723-skylink-7','icon': [{'src': 'https://services.mujtvprogram.cz/tvprogram2services/services/logoImageDownloader.php?p1=ac6c69625699eaecc9b39f7ea4d69b8c&amp;p2=80'}]})
    if "233" in ids:
        channels.append({'display-name': [(replace_names('Stingray Classica'), u'cs')], 'id': '233-stingray-classica','icon': [{'src': 'https://services.mujtvprogram.cz/tvprogram2services/services/logoImageDownloader.php?p1=661af53f8f3b997611c29f844c7006fd&amp;p2=80'}]})
    if "234" in ids:
        channels.append({'display-name': [(replace_names('Stingray iConcerts'), u'cs')], 'id': '234-stingray-iconcerts','icon': [{'src': 'https://services.mujtvprogram.cz/tvprogram2services/services/logoImageDownloader.php?p1=99c87946872c81f46190c77af7cd1d89&amp;p2=80'}]})
    if "110" in ids:
        channels.append({'display-name': [(replace_names('Stingray CMusic'), u'cs')], 'id': '110-stingray-cmusic','icon': [{'src': 'https://services.mujtvprogram.cz/tvprogram2services/services/logoImageDownloader.php?p1=b323f2ad3200cb938b43bed58dd8fbf9&amp;p2=80'}]})
    now = datetime.now()
    for x in range(d_b*-1, d):
        next_day = now + timedelta(days = x)
        date_ = next_day.strftime("%d.%m.%Y")
        for y in ids:
            html = requests.post("https://services.mujtvprogram.cz/tvprogram2services/services/tvprogrammelist_mobile.php", data = {"channel_cid": y, "day": str(x)}).content
            root = ET.fromstring(html)
            for i in root.iter("programme"):
                programmes.append({"channel": ids_[y],  "start": time.strftime('%Y%m%d%H%M%S', time.localtime(int(i.find("startDateTimeInSec").text))) + TS, "stop": time.strftime('%Y%m%d%H%M%S', time.localtime(int(i.find("endDateTimeInSec").text))) + TS, "title": [(i.find("name").text, "")], "desc": [(i.find("shortDescription").text, "")]})
    return channels, programmes


def get_o2_programmes(o2, d, d_b):
    channelKeys = o2.split(",")
    params = ""
    for channelKey in channelKeys:
        params = params + ("&channelKey=" + quote(channelKey))
    programmes = []
    for i in range(int(d_b)*-1, int(d)):
        next_day = datetime.combine(date.today(), datetime.min.time()) + timedelta(days = i)
        date_ = next_day.strftime("%d.%m.%Y")
        to_day = next_day  + timedelta(minutes = 1439)
        dt_from = int(time.mktime(next_day.timetuple()))
        dt_to = int(time.mktime(to_day.timetuple()))
        url = "https://api.o2tv.cz/unity/api/v1/epg/depr/?forceLimit=true&limit=500" + params + "&from=" + str(dt_from*1000) + "&to=" + str(dt_to*1000)
        req = requests.get(url).json()
        for it in req["epg"]["items"]:
            ch_name= it["channel"]["name"].replace(" HD", "").replace(" ", "-").lower()
            for e in it["programs"]:
                name = e["name"]
                start = datetime.fromtimestamp(int(e["start"])/1000).strftime('%Y%m%d%H%M%S')
                stop = datetime.fromtimestamp(int(e["end"])/1000).strftime('%Y%m%d%H%M%S')
                if e["npvr"] == True:
                    req = requests.get("https://api.o2tv.cz/unity/api/v1/programs/" + str(e["epgId"]) + "/").json()
                    programmes.append({"channel": ch_name, "start": start + TS, "stop": stop + TS, "title": [(name, "")], "desc": [(req["shortDescription"], u'')]})
                else:
                    programmes.append({"channel": ch_name, "start": start + TS, "stop": stop + TS, "title": [(name, "")]})
    return programmes


def get_tm_programmes(tm_ids, d, d_b):
    if d > 10:
        d = 10
    tm_ids_list = tm_ids.split(",")
    programmes2 = []
    params={"dsid": "c75536831e9bdc93", "deviceName": "Redmi Note 7", "deviceType": "OTT_ANDROID", "osVersion": "10", "appVersion": "3.7.0", "language": "CZ"}
    headers={"Host": "czgo.magio.tv", "authorization": "Bearer", "User-Agent": "okhttp/3.12.12", "content-type":  "application/json", "Connection": "Keep-Alive"}
    req = requests.post("https://czgo.magio.tv/v2/auth/init", params=params, headers=headers, verify=True).json()
    token = req["token"]["accessToken"]
    headers2={"Host": "czgo.magio.tv", "authorization": "Bearer " + token, "User-Agent": "okhttp/3.12.12", "content-type":  "application/json"}
    req1 = requests.get("https://czgo.magio.tv/v2/television/channels?list=LIVE&queryScope=LIVE", headers=headers2).json()["items"]
    channels2 = []
    ids = ""
    tvch = {}
    for y in req1:
        id = str(y["channel"]["channelId"])
        if tm_ids_list == [""]:
            name = y["channel"]["name"]
            logo = str(y["channel"]["logoUrl"])
            ids = ids + "," + id
            tm = str(ids[1:])
            tvch[name] = "tm-" + id + "-" + encode(name).replace(" HD", "").lower().replace(" ", "-")
            channels2.append(({"display-name": [(replace_names(name.replace(" HD", "")), u"cs")], "id": "tm-" + id + "-" + encode(name).replace(" HD", "").lower().replace(" ", "-"), "icon": [{"src": logo}]}))
        else:
            if id in tm_ids_list:
                name = y["channel"]["name"]
                logo = str(y["channel"]["logoUrl"])
                ids = ids + "," + id
                tm = str(ids[1:])
                tvch[name] = "tm-" + id + "-" + encode(name).replace(" HD", "").lower().replace(" ", "-")
                channels2.append(({"display-name": [(name.replace(" HD", ""), u"cs")], "id": "tm-" + id + "-" + encode(name).replace(" HD", "").lower().replace(" ", "-"), "icon": [{"src": logo}]}))
    now = datetime.now()
    for i in range(d_b*-1, d):
        next_day = now + timedelta(days = i)
        back_day = (now + timedelta(days = i)) - timedelta(days = 1)
        date_to = next_day.strftime("%Y-%m-%d")
        date_from = back_day.strftime("%Y-%m-%d")
        date_ = next_day.strftime("%d.%m.%Y")
        req = requests.get("https://czgo.magio.tv/v2/television/epg?filter=channel.id=in=(" + tm + ");endTime=ge=" + date_from + "T23:00:00.000Z;startTime=le=" + date_to + "T23:59:59.999Z&limit=" + str(len(channels2)) + "&offset=0&lang=CZ", headers=headers2).json()["items"]
        for x in range(0, len(req)):
            for y in req[x]["programs"]:
                channel = y["channel"]["name"]
                start_time = y["startTime"].replace("-", "").replace("T", "").replace(":", "")
                stop_time = y["endTime"].replace("-", "").replace("T", "").replace(":", "")
                title = y["program"]["title"]
                desc = y["program"]["description"]
                epi = y["program"]["programValue"]["episodeId"]
                if epi != None:
                    title = title + " (" + epi + ")"
                programm = {'channel': tvch[channel], 'start': start_time + TS, 'stop': stop_time + TS, 'title': [(title, u'')], 'desc': [(desc, u'')]}
                if programm not in programmes2:
                    programmes2.append(programm)
    return channels2, programmes2


class Get_channels_sms:

    def __init__(self):
        self.channels = []
        headers = {"user-agent": "SMSTVP/1.7.3 (242;cs_CZ) ID/ef284441-c1cd-4f9e-8e30-f5d8b1ac170c HW/Redmi Note 7 Android/10 (QKQ1.190910.002)"}
        self.html = requests.get("http://programandroid.365dni.cz/android/v6-tv.php?locale=cs_CZ", headers = headers).text
        self.ch = {}

    def all_channels(self):
        try:
            root = ET.fromstring(self.html)
            for i in root.iter("a"):
                self.ch[i.attrib["id"]] = encode((i.attrib["id"] + "-" + i.find("n").text).replace(" ", "-").lower())
                try:
                    icon = "http://sms.cz/kategorie/televize/bmp/loga/velka/" + i.find("o").text
                except:
                    icon = ""
                self.channels.append({"display-name": [(replace_names(i.find("n").text), u"cs")], "id": encode((i.attrib["id"] + "-" + i.find("n").text).replace(" ", "-").lower()), "icon": [{"src": icon}]})
            self.f.close()
        except:
            pass
        return self.ch, self.channels

    def cz_sk_channels(self):
        try:
            root = ET.fromstring(self.html)
            for i in root.iter("a"):
                if i.find("p").text == "České" or i.find("p").text == "Slovenské":
                    self.ch[i.attrib["id"]] = encode((i.attrib["id"] + "-" + i.find("n").text).replace(" ", "-").lower())
                    try:
                        icon = "http://sms.cz/kategorie/televize/bmp/loga/velka/" + i.find("o").text
                    except:
                        icon = ""
                    self.channels.append({"display-name": [(replace_names(i.find("n").text), u"cs")], "id": encode((i.attrib["id"] + "-" + i.find("n").text).replace(" ", "-").lower()), "icon": [{"src": icon}]})
        except:
            pass
        return self.ch, self.channels

    def own_channels(self, cchc):
        try:
            root = ET.fromstring(self.html)
            for i in root.iter("a"):
                if i.attrib["id"] in cchc:
                    self.ch[i.attrib["id"]] = encode((i.attrib["id"] + "-" + i.find("n").text).replace(" ", "-").lower())
                    try:
                        icon = "http://sms.cz/kategorie/televize/bmp/loga/velka/" + i.find("o").text
                    except:
                        icon = ""
                    self.channels.append({"display-name": [(replace_names(i.find("n").text), u"cs")], "id": encode((i.attrib["id"] + "-" + i.find("n").text).replace(" ", "-").lower()), "icon": [{"src": icon}]})
        except:
            pass
        return self.ch, self.channels


class Get_programmes_sms:

    def __init__(self, days_back, days):
        self.programmes_sms = []
        self.days_back = days_back
        self.days = days

    def data_programmes(self, ch):
        if ch != {}:
            chl = ",".join(ch.keys())
            now = datetime.now()
            for i in range(self.days_back*-1, self.days):
                next_day = now + timedelta(days = i)
                date = next_day.strftime("%Y-%m-%d")
                date_ = next_day.strftime("%d.%m.%Y")
                headers = {"user-agent": "SMSTVP/1.7.3 (242;cs_CZ) ID/ef284441-c1cd-4f9e-8e30-f5d8b1ac170c HW/Redmi Note 7 Android/10 (QKQ1.190910.002)"}
                html = requests.get("http://programandroid.365dni.cz/android/v6-program.php?datum=" + date + "&id_tv=" + chl, headers = headers).text
                root = ET.fromstring(html)
                root[:] = sorted(root, key=lambda child: (child.tag,child.get("o")))
                for i in root.iter("p"):
                    n = i.find("n").text
                    try:
                        k = i.find("k").text
                    except:
                        k = ""
                    if i.attrib["id_tv"] in ch:
                        self.programmes_sms.append({"channel": ch[i.attrib["id_tv"]].replace("804-ct-art", "805-ct-:d"), "start": i.attrib["o"].replace("-", "").replace(":", "").replace(" ", "") + TS, "stop": i.attrib["d"].replace("-", "").replace(":", "").replace(" ", "") + TS, "title": [(n, "")], "desc": [(k, "")]})
        return self.programmes_sms


def main():
    os.system("clear")
    channels = []
    programmes = []
    cchc = ""
    tm_id = ""
    o2_id = ""
    if TV_SMS_CZ == 1:
        try:
            print("TV.SMS.cz kanály")
            print("Stahuji data...")
            g = Get_channels_sms()
            if TV_SMS_CZ_IDS == "":
                ch, channels_sms = g.all_channels()
            else:
                ch, channels_sms = g.own_channels(TV_SMS_CZ_IDS)
            channels.extend(channels_sms)
            gg = Get_programmes_sms(days_back, days)
            programmes_sms = gg.data_programmes(ch)
            programmes.extend(programmes_sms)
            sys.stdout.write('\x1b[1A')
            sys.stdout.write('\x1b[2K')
            print("Hotovo\n")
        except Exception as ex:
            sys.stdout.write('\x1b[1A')
            sys.stdout.write('\x1b[2K')
            print("Chyba: " + str(ex) + "\n")
    if T_MOBILE_TV_GO == 1:
        try:
            print("T-Mobile TV Go kanály")
            print("Stahuji data...")
            if T_MOBILE_TV_GO_IDS == "":
                tm_id = ""
            else:
                tm_id = T_MOBILE_TV_GO_IDS
            channels_tm, programmes_tm = get_tm_programmes(tm_id, days, days_back)
            channels.extend(channels_tm)
            programmes.extend(programmes_tm)
            sys.stdout.write('\x1b[1A')
            sys.stdout.write('\x1b[2K')
            print("Hotovo\n")
        except Exception as ex:
            sys.stdout.write('\x1b[1A')
            sys.stdout.write('\x1b[2K')
            print("Chyba: " + str(ex) + "\n")
    if O2_TV_SPORT == 1:
        try:
            print("O2 TV Sport kanály")
            print("Stahuji data...")
            o2_id = "O2 Sport1 HD,O2 Sport2 HD,O2 Sport3 HD,O2 Sport4 HD,O2 Sport5 HD,O2 Sport6 HD,O2 Sport7 HD,O2 Sport8 HD"
            channels.extend(({"display-name": [(replace_names("O2 Sport1"), u"cs")], "id": "o2tv-sport1", "icon": [{"src": 'http://www.o2tv.cz/assets/images/tv-logos/original/o2-sport-hd.png'}]}, {"display-name": [(replace_names("O2 Sport2"), u"cs")], "id": "o2tv-sport2", "icon": [{"src": 'http://www.o2tv.cz/assets/images/tv-logos/original/o2-sport-hd.png'}]}, {"display-name": [(replace_names("O2 Sport3"), u"cs")], "id": "o2tv-sport3", "icon": [{"src": 'http://www.o2tv.cz/assets/images/tv-logos/original/o2-sport-hd.png'}]}, {"display-name": [(replace_names("O2 Sport4"), u"cs")], "id": "o2tv-sport4", "icon": [{"src": 'http://www.o2tv.cz/assets/images/tv-logos/original/o2-sport-hd.png'}]}, {"display-name": [(replace_names("O2 Sport5"), u"cs")], "id": "o2tv-sport5", "icon": [{"src": 'http://www.o2tv.cz/assets/images/tv-logos/original/o2-sport-hd.png'}]}, {"display-name": [(replace_names("O2 Sport6"), u"cs")], "id": "o2tv-sport6", "icon": [{"src": 'http://www.o2tv.cz/assets/images/tv-logos/original/o2-sport-hd.png'}]}, {"display-name": [(replace_names("O2 Sport7"), u"cs")], "id": "o2tv-sport7", "icon": [{"src": 'http://www.o2tv.cz/assets/images/tv-logos/original/o2-sport-hd.png'}]}, {"display-name": [(replace_names("O2 Sport8"), u"cs")], "id": "o2tv-sport8", "icon": [{"src": 'http://www.o2tv.cz/assets/images/tv-logos/original/o2-sport-hd.png'}]}))
            programmes_o2 = get_o2_programmes(o2_id, days, days_back)
            programmes.extend(programmes_o2)
            sys.stdout.write('\x1b[1A')
            sys.stdout.write('\x1b[2K')
            print("Hotovo\n")
        except Exception as ex:
            sys.stdout.write('\x1b[1A')
            sys.stdout.write('\x1b[2K')
            print("Chyba: " + str(ex) + "\n")
    if MUJ_TV_PROGRAM_CZ == 1:
        try:
            print("můjTVprogram.cz kanály")
            print("Stahuji data...")
            channels_mujtv, programmes_mujtv = get_muj_tv_programmes(["723", "233", "234", "110"], days, days_back)
            channels.extend(channels_mujtv)
            programmes.extend(programmes_mujtv)
            sys.stdout.write('\x1b[1A')
            sys.stdout.write('\x1b[2K')
            print("Hotovo\n")
        except Exception as ex:
            sys.stdout.write('\x1b[1A')
            sys.stdout.write('\x1b[2K')
            print("Chyba: " + str(ex) + "\n")
    if channels != []:
        print("\nCelkem kanálů: " + str(len(channels)))
        print("Generuji...")
        try:
            w = xmltv.Writer(encoding="utf-8", source_info_url="http://www.funktronics.ca/python-xmltv", source_info_name="Funktronics", generator_info_name="python-xmltv", generator_info_url="http://www.funktronics.ca/python-xmltv")
            for c in channels:
                w.addChannel(c)
            for p in programmes:
                w.addProgramme(p)
            w.write(fn, pretty_print=True)
            sys.stdout.write('\x1b[1A')
            sys.stdout.write('\x1b[2K')
            print("Hotovo\n\n")
        except Exception as ex:
            sys.stdout.write('\x1b[1A')
            sys.stdout.write('\x1b[2K')
            print("Chyba: " + str(ex) + "\n")
        if ftp_upload == 1:
            ftp = FTP()
            ftp.set_debuglevel(2)
            ftp.connect(ftp_server, ftp_port)
            ftp.login(ftp_login, ftp_password)
            ftp.cwd(ftp_folder)
            file = open(fn, "rb")
            ftp.storbinary('STOR ' + "epg.xml", file)
            file.close()
            ftp.quit()
    else:
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')
        print("Žádné kanály\n\n")


if __name__ == "__main__":
    main()