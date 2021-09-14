findlines = open('../Replace/find.txt').read().split('\n')
replacelines = open('../Replace/replace.txt').read().split('\n')
find_replace = dict(zip(findlines, replacelines))

with open('../Replace/data.txt') as data:
    with open('../Replace/out.txt', 'w') as new_data:
        for line in data:
            for key in find_replace:
                if key in line:
                    line = line.replace(key, find_replace[key])
            new_data.write(line)