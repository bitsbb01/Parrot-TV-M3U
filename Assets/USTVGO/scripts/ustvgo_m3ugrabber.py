import os
import sys


windows = False
python = 'python3'
if 'win' in sys.platform:
    windows = True
    python = 'python'

def done():
    sys.exit()
    
print('[*] Checking dependencies...')
while True:
    try:
        import requests
        from tqdm import tqdm
        break
    except ModuleNotFoundError as e:
        module = str(e)[17:-1]
        print(f'[*] Installing {module} module for python')
        #os.system(f'{python} -m pip install --upgrade pip')
        try:
            if os.system(f'{python} -m pip install {module}') != 0:
                raise 
        except:
            print(f'[!] Error installing "{module}" module. Do you have pip installed?')
            input(f'[!] Playlist generation failed. Press Ctrl+C to exit...')
            done()

def grab(name, code, logo):
    data = {'stream': code}
    m3u = s.post('https://ustvgo.tv/data.php', data=data).text
    playlist.write(f'\n#EXTINF:-1 tvg-id="{code}" group-title="ustvgo" tvg-logo="{logo}", {name}')
    playlist.write(f'\n{m3u}')

total = 0
with open('../ustvgo_channel_info.txt') as file:
    for line in file:
        line = line.strip()
        if not line or line.startswith('~~'):
            continue
        total += 1

s = requests.Session()
with open('../ustvgo_channel_info.txt') as file:
    with open('../../Channels/ustvgo.m3u', 'w') as playlist:
        print('[*] Generating your playlist, please wait...\n')
        playlist.write('x-tvg-url="https://raw.githubusercontent.com/nomoney4me/ustvgo/main/output/ustvgo_epg.xml"')
        pbar = tqdm(total=total)
        for line in file:
            line = line.strip()
            if not line or line.startswith('~~'):
                continue
            line = line.split('|')
            name = line[0].strip()
            code = line[1].strip()
            logo = line[2].strip()
            pbar.update(1)
            grab(name, code, logo)
        pbar.close()
        print('\n[SUCCESS] Playlist is generated!\n')
        done()