try:
    #read file
    with open("EPLTeams.csv","r") as file:
        data=file.readlines()
    
    #initialize
    highestPercentage=-1
    best_team=""
    
    #except the first
    for row in data[1:]:
        #delete " " near by text
        row = row.strip()
        #if row is empty then skip
        if row == "":
            continue 
        
        block = row.split()
        #skip for the not normal row
        if len(block) != 3:
            continue
        
        team_name = block[0].strip()
        
        try:
            played = int(block[1].strip())
            won = int(block[2].strip())
            
        except ValueError:
            continue
        #skip if /0
        
        if played == 0 :
            continue
        
        #calculate winning percentage
        win_percentage = won / played
        
        if win_percentage > highestPercentage:
            highestPercentage = win_percentage
            best_team = team_name
            
    print(f"{best_team},{highestPercentage:.3f}")

except IOError:
    print ("IO Error")
print("Analysis finished")
