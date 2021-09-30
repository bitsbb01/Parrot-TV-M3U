def replaceSTT():
    findlines = open('Assets/Service/f.txt').read().split('\n')
    replacelines = open('Assets/Service/r.txt').read().split('\n')
    find_replace = dict(zip(findlines, replacelines))

    with open('Assets/Service/tt.txt') as data:
        with open('Assets/Service/timeou.txt', 'w') as new_data:
            for line in data:
                for key in find_replace:
                    if key in line:
                        line = line.replace(key, find_replace[key])
                new_data.write(line)