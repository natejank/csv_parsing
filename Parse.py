teams = {}

for line in open('Scouting_2019_Match_Schedule.csv', 'r').readlines():
    line = line.rstrip('/n') # line[:-1] doesn't work because the file doesn't end with a newline
    line = line.split(',')

    match_number = line.pop(0)

    for index in line:
        if index.isnumeric():
            if index not in teams:
                teams[index] = []
            teams[index].append(match_number)

for team in teams:
    out = f'{team}: {teams[team].pop(0)}'

    for match in teams[team]:
        out += f', {match}'

    print(out)
