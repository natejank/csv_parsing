list_of_teams=[] #list of teams
schedule_by_match={} #dict of schedule_by_match by match
schedule_by_team={} #dict of schedule_by_match by team
csv_file="Scouting_2019_Match_Schedule.csv"

file=open(csv_file,'r')
for line in file.readlines(): 
    line=line.replace('\n','')  
    line=line.split(",") 
 
    if line[0].isnumeric():
        lineKey=line[0]
        line.pop(0) 
        schedule_by_team.update({lineKey:line})
        for i in range(0,len(line)-1):
            if line[i] not in list_of_teams:
                list_of_teams.append(line[i])
file.close()

for i in range (0,len(list_of_teams)-1): 
    matches=[]
    for j in range (0,len(schedule_by_team.keys())-1):
        if list_of_teams[i] in schedule_by_team.get(list(schedule_by_team.keys())[j]):
            matches.append(list(schedule_by_team.keys())[j]) 
    schedule_by_match.update({list_of_teams[i]:matches})

for i in range (0,len(schedule_by_match.keys())-1):
    print(str(list(schedule_by_match.keys())[i])+": "+str(schedule_by_match.get(list(schedule_by_match.keys())[i])).replace('[','').replace(']','')) 