def replaceUStVicons():
    findlines = open('Assets/USTVGOreplace/find.txt').read().split('\n')
    replacelines = open('Assets/USTVGOreplace/replace.txt').read().split('\n')
    find_replace = dict(zip(findlines, replacelines))

    with open('Assets/USTVGOreplace/data.txt') as data:
        with open('Assets/Channels/US/ustvgo.m3u', 'w') as new_data:
            for line in data:
                for key in find_replace:
                    if key in line:
                        line = line.replace(key, find_replace[key])
                new_data.write(line)