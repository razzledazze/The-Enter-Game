import time
import csv

print(time.gmtime())

def playGame():
    input("\nWelcome to the Enter Game.\nWhen you are ready to play, press enter twice as fast as possible.\n\n>") #Introduces the game
    startTime = time.time() #After enter is pressed the first time, the time is recorded
    input() #press enter again
    finishTime = time.time() #record the finish time
    timeElapsed = finishTime - startTime #find the time difference
    return timeElapsed #return the time difference

def openCsv():
    read = open("highScores.csv") #open the csv file containing the high scores
    read = csv.reader(read) #read the csv file
    return read

def compileHighScores(read):
    highScores = [] #create a blank array for the high scores
    for row in read: #for every record in the csv file (stored as name,score)
        highScores.append([row[0],row[1]]) #make a new array within the highScores array in the form [name,score]
    return highScores

def determineHighScore(userTime,userName,highScores):
    newHighScores = [] #a new high scores array
    alreadyScored = False #so that once the score is put into the array, it doesn't also get put in for every lower score as well
    for score in highScores: #for every record
        if float(score[1]) < userTime: #if the user has done worse than the score
            newHighScores.append(score) #put the score back where it was from
        elif float(score[1]) > userTime and alreadyScored == False or float(score[1]) > userTime and alreadyScored == False: #if the user has done better than the score, and the user's score hasn't already been put in
            newHighScores.append([userName,userTime]) #put the user's score in
            newHighScores.append(score) #then put the old score afterwards
            alreadyScored = True #then make sure the user's score isn't put in again
        else:
            newHighScores.append(score) #if the user's score has already been added, just add the normal score
    if alreadyScored == False: #if the end of the highscores array has been reached and the user's still not added,
        newHighScores.append([userName,userTime]) #add it
    return newHighScores

def writeCsv(newHighScores): #this function re-writes the csv file, now including the new user's score
    write = open("highScores.csv","w")
    write = csv.writer(write)
    for record in newHighScores:
        write.writerow(record)

def printScores(newHighScores): #prints the top 3 after adding the user's new score
    print("The Current Top 3 Are:\n-------------------")
    for i in range(3):
        print(str(newHighScores[i][0])+" - "+str(newHighScores[i][1])+"ms")

def getUserName(highScores):
    runAgain = True
    while runAgain == True:
        userName = input("Enter your chosen player name: ") #gets the user's name choice
        runAgain = False
        for i in highScores: #for every high score record
            if i[0] == userName: #if the record already has the same name as the user's choice
                runAgain = True #reset runagain so that the user is asked again
        if userName in [""," "]: #if the user's choice is invalid
            runAgain = True #reset runagain
        if runAgain == True: #if at the end, the user's choice is taken or invalid, give error message
            print("Sorry, that name is already taken or is invalid")
    return userName #return name only after loop is ended, so the username must be unique and valid

read = openCsv()
highScores = compileHighScores(read)

userName = getUserName(highScores)
userTime = round(playGame() * 1000,2)
print("Your time was "+str(userTime)+"ms\n")
newHighScores = determineHighScore(userTime,userName,highScores)
printScores(newHighScores)
writeCsv(newHighScores)