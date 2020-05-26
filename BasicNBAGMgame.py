import random
import time

playerDict = {
    'LeBron James': 97, 'Giannis Antetokounmpo': 97, 'James Harden': 97, 'Kevin Durant': 96, 'Kawhi Leonard': 96,
    'Luka Doncic': 96, 'Anthony Davis': 96, 'Stephen Curry': 95, 'Damian Lillard': 94, 'Nikola Jokic': 91, 'Joel Embiid': 91,
    'Kyrie Irving': 91, 'Trae Young': 90, 'Karl-Anthony Towns': 90, 'Paul George': 90, 'Russell Westbrook': 89, 'Pascal Siakam': 89,
    'Bradley Beal': 89, 'Klay Thompson': 89, 'Ben Simmons': 88, 'Jayson Tatum': 88, 'Jimmy Butler': 88, 'Donovan Mitchell': 87,
    'Chris Paul': 87, 'Rudy Gobert': 87, 'Kemba Walker': 87, 'Khris Middleton': 87, 'Zion Williamson': 86, 'Kristaps Porzingis': 86,
    'Devin Booker': 86, 'Brandon Ingram': 86, 'DeMar DeRozan': 86, 'John Wall': 86, 'Bam Adebayo': 86, 'John Collins': 86,
    'Clint Capela': 86, 'DeAndre Ayton': 85, 'Andre Drummond': 85, 'DeAaron Fox': 85, 'CJ McCollum': 85, 'Zach LaVine': 85,
    'Nikola Vucevic': 85, 'Kyle Lowry': 85, 'Tobias Harris': 85, 'Jaylen Brown': 85, 'Montrezl Harrell': 85, 'Domantas Sabonis': 85,
    'Ja Morant': 84, 'Shai Gilgeous-Alexander': 84, 'LaMarcus Aldridge': 84, 'DAngelo Russell': 84, 'Jamal Murray': 84,
    'Derrick Rose': 84, 'Steven Adams': 84, 'Danilo Gallinari': 84, 'Mitchell Robinson': 83, 'Malcolm Brogdon': 83,
    'Victor Oladipo': 83, 'Jrue Holiday': 83, 'Eric Bledsoe': 83
}

''' This is the full dictionary consisting of 60 players to be spread amongst 6 NBA Teams through a draft.
Each player has a corresponding rating, based off of how good they are in real life. '''

# This establishes lists for when wins need to be universally stored to calculate the records at the end of the season.
userTeamWins = []
LakersWins = []
WarriorsWins = []
BullsWins = []
KnicksWins = []
CelticsWins = []

# This creates a list of players to be shown to the user, which is derived from playerDict, which as both the player and the rating.
# The rating is not included in this list to increase the diffculty for the user.
playerlist = []
for x, y in playerDict.items():
    playerlist.append(x)

# 6 Classes are established for storing all of the players and the ratings for each team

class userTeamClass():
    ratings = []
    players = []
    def __init__(self, player):
        self.name = player
    def add_rating(self, rating):
        self.ratings.append(rating)
    def add_player(self, player):
        self.players.append(player)

class Lakers():
    ratings = []
    players = []
    def __init__(self, player):
        self.name = player
    def add_rating(self, rating):
        self.ratings.append(rating)
    def add_player(self, player):
        self.players.append(player)

class Warriors():
    ratings = []
    players = []
    def __init__(self, player):
        self.name = player
    def add_rating(self, rating):
        self.ratings.append(rating)
    def add_player(self, player):
        self.players.append(player)

class Bulls():
    ratings = []
    players = []
    def __init__(self, player):
        self.name = player
    def add_rating(self, rating):
        self.ratings.append(rating)
    def add_player(self, player):
        self.players.append(player)

class Knicks():
    ratings = []
    players = []
    def __init__(self, player):
        self.name = player
    def add_rating(self, rating):
        self.ratings.append(rating)
    def add_player(self, player):
        self.players.append(player)

class Celtics():
    ratings = []
    players = []
    def __init__(self, player):
        self.name = player
    def add_rating(self, rating):
        self.ratings.append(rating)
    def add_player(self, player):
        self.players.append(player)

# This is a tiny function that is simply for calculating the average for the ratings list for each team after the draft.
def avg(ratings):
    return sum(ratings) / len(ratings)

# This function takes in the userTeam's name, the number for which round of the draft it is, and which draft order the round is using. 
# It either prompts the user to select a player or has the computer randomly choose a one of the best remaining players from the dictionary.
# It stores the players and ratings in the corresponding team's Class, along with removing the player that was selected from the playerDict and playerlist.
# At the end of the function (every round), it prints the remaining players in the draft pool.
def rounds(team, round, draftorder):
    roundnum = str(round)
    for i in range(0,6):
        if draftorder[i] == team:
            selection1 = input('It is your turn to choose! Select your player here:  ')
            if selection1 not in playerDict:
                selection1 = input('That player is not available. Try again here:  ')
            print('The ' + team + ' selected ' + selection1 + ' with their round ' + roundnum + ' pick.')
            userTeam1 = userTeamClass(selection1)
            ratingofplayer = playerDict[selection1]
            playerDict.pop(selection1)
            playerlist.remove(selection1)
            userTeam1.add_rating(ratingofplayer)
            userTeam1.add_player(selection1)
        elif draftorder[i] == 'Warriors':
            x = random.randint(0,4)
            selection1 = playerlist[x]
            print('The Warriors selected ' + selection1 + ' with their round ' + roundnum + ' pick.')
            Warriors1 = Warriors(selection1)
            ratingofplayer = playerDict[selection1]
            playerDict.pop(selection1)
            playerlist.remove(selection1)
            Warriors1.add_rating(ratingofplayer)
            Warriors1.add_player(selection1)
        elif draftorder[i] == 'Lakers':
            x = random.randint(0,4)
            selection1 = playerlist[x]
            print('The Lakers selected ' + selection1 + ' with their round ' + roundnum + ' pick.')
            Lakers1 = Lakers(selection1)
            ratingofplayer = playerDict[selection1]
            playerDict.pop(selection1) 
            playerlist.remove(selection1)
            Lakers1.add_rating(ratingofplayer)
            Lakers1.add_player(selection1)
        elif draftorder[i] == 'Bulls':
            x = random.randint(0,4)
            selection1 = playerlist[x]
            print('The Bulls selected ' + selection1 + ' with their round ' + roundnum + ' pick.')
            Bulls1 = Bulls(selection1)
            ratingofplayer = playerDict[selection1]
            playerDict.pop(selection1)
            playerlist.remove(selection1)
            Bulls1.add_rating(ratingofplayer)
            Bulls1.add_player(selection1)
        elif draftorder[i] == 'Knicks':
            x = random.randint(0,4)
            selection1 = playerlist[x]
            print('The Knicks selected ' + selection1 + ' with their round ' + roundnum + ' pick.')
            Knicks1 = Knicks(selection1)
            ratingofplayer = playerDict[selection1]
            playerDict.pop(selection1)
            playerlist.remove(selection1)
            Knicks1.add_rating(ratingofplayer)
            Knicks1.add_player(selection1)
        elif draftorder[i] == 'Celtics':
            x = random.randint(0,4)
            selection1 = playerlist[x]
            print('The Celtics selected ' + selection1 + ' with their round ' + roundnum + ' pick.')
            Celtics1 = Celtics(selection1)
            ratingofplayer = playerDict[selection1]
            playerDict.pop(selection1)
            playerlist.remove(selection1)
            Celtics1.add_rating(ratingofplayer)
            Celtics1.add_player(selection1)
    time.sleep(1)
    print('')
    print('Here are the players remaining after Round #' + roundnum + '!')
    print(playerlist)

# This is the actual draft function, which first randomizes the draft order and also creates a corresponding reversed draft order.
# It then runs the rounds() function 9 times for the first 9 rounds. The 10th round is different, so it is typed out separately from the rounds() function.
# This is because The 10th round does not include choosing players by chance for the other teams because there are only 6 players left.
# The separate 10th round necessary to have so that the players and ratings stored in the Classes can be accessed directly afterwards.
# At the conlcusion of the draft, it prints each teams' players and calculates each teams' average rating using the avg() function.
# Finally, it stores each teams' average rating into a singular list and returns it, so this singular variable is now global.
def draft(team):
    print('Welcome to the Fantasy Draft! You are controlling the ' + team + '.')
    draftorder = ['Lakers', 'Warriors', 'Bulls', 'Knicks', 'Celtics', team]
    random.shuffle(draftorder)
    print('Before the draft begins, it will be important to know who is available. Here is a list of the 60 players you can draft!')
    time.sleep(5)
    print(playerlist)
    time.sleep(5)
    print('The draft order has been randomized. It is ' + str(draftorder) + '.')
    time.sleep(5)
    print('You will select 10 players, and therefore there will be 10 rounds in this draft.')
    print('The draft is a snake draft, so the team with the 6th pick will get the 7th pick, 5th with 8th, and so on.')
    print('Let the Fantasy Draft begin! Good luck!')
    time.sleep(3)
    reversedraftorder = draftorder[::-1]

    rounds(team, 1, draftorder)
    time.sleep(0.5)
    rounds(team, 2, reversedraftorder)
    time.sleep(0.5)
    rounds(team, 3, draftorder)
    time.sleep(0.5)
    rounds(team, 4, reversedraftorder)
    time.sleep(0.5)
    rounds(team, 5, draftorder)
    time.sleep(0.5)
    rounds(team, 6, reversedraftorder)
    time.sleep(0.5)
    rounds(team, 7, draftorder)
    time.sleep(0.5)
    rounds(team, 8, reversedraftorder)
    time.sleep(0.5)
    rounds(team, 9, draftorder)
    time.sleep(0.5)

    # 10th Round
    for i in range(0,6):
        if reversedraftorder[i] == team:
            selection1 = input('It is your turn to choose! Select your player here:  ')
            if selection1 not in playerDict:
                selection1 = input('That player is not available. Try again here:  ')
            print('The ' + team + ' selected ' + selection1 + ' with their round 10 pick.')
            userTeam1 = userTeamClass(selection1)
            ratingofplayer = playerDict[selection1]
            playerDict.pop(selection1)
            playerlist.remove(selection1)
            userTeam1.add_rating(ratingofplayer)
            userTeam1.add_player(selection1)
        elif reversedraftorder[i] == 'Warriors':
            selection1 = playerlist[0]
            print('The Warriors selected ' + selection1 + ' with their round 10 pick.')
            Warriors1 = Warriors(selection1)
            ratingofplayer = playerDict[selection1]
            playerDict.pop(selection1)
            playerlist.remove(selection1)
            Warriors1.add_rating(ratingofplayer)
            Warriors1.add_player(selection1)
        elif reversedraftorder[i] == 'Lakers':
            selection1 = playerlist[0]
            print('The Lakers selected ' + selection1 + ' with their round 10 pick.')
            Lakers1 = Lakers(selection1)
            ratingofplayer = playerDict[selection1]
            playerDict.pop(selection1)
            playerlist.remove(selection1)
            Lakers1.add_rating(ratingofplayer)
            Lakers1.add_player(selection1)
        elif reversedraftorder[i] == 'Bulls':
            selection1 = playerlist[0]
            print('The Bulls selected ' + selection1 + ' with their round 10 pick.')
            Bulls1 = Bulls(selection1)
            ratingofplayer = playerDict[selection1]
            playerDict.pop(selection1)
            playerlist.remove(selection1)
            Bulls1.add_rating(ratingofplayer)
            Bulls1.add_player(selection1)
        elif reversedraftorder[i] == 'Knicks':
            selection1 = playerlist[0]
            print('The Knicks selected ' + selection1 + ' with their round 10 pick.')
            Knicks1 = Knicks(selection1)
            ratingofplayer = playerDict[selection1]
            playerDict.pop(selection1)
            playerlist.remove(selection1)
            Knicks1.add_rating(ratingofplayer)
            Knicks1.add_player(selection1)
        elif reversedraftorder[i] == 'Celtics':
            selection1 = playerlist[0]
            print('The Celtics selected ' + selection1 + ' with their round 10 pick.')
            Celtics1 = Celtics(selection1)
            ratingofplayer = playerDict[selection1]
            playerDict.pop(selection1)
            playerlist.remove(selection1)
            Celtics1.add_rating(ratingofplayer)
            Celtics1.add_player(selection1)
    time.sleep(2)
    print('Congratulations! The Fantasy Draft is complete and all teams are filled!')
    print('')
    time.sleep(2)
    print('Here is what the ' + team + ' look like. First, there is your roster of players, and after is each players corresponding rating.')
    time.sleep(2)
    print(userTeam1.players)
    print(userTeam1.ratings)
    time.sleep(10)
    print('')
    print('In addition, here are the other teams rosters.')
    time.sleep(1)
    print('The Warriors roster is')
    print(Warriors1.players)
    print('The Lakers roster is')
    print(Lakers1.players)
    print('The Bulls roster is') 
    print(Bulls1.players)
    print('The Knicks roster is')
    print(Knicks1.players)
    print('The Celtics roster is')
    print(Celtics1.players)
    time.sleep(5)

    userTeamRatings = userTeam1.ratings
    WarriorsRatings = Warriors1.ratings
    LakersRatings = Lakers1.ratings
    BullsRatings = Bulls1.ratings
    KnicksRatings = Knicks1.ratings
    CelticsRatings = Celtics1.ratings

    averageUserTeam = avg(userTeamRatings)
    averageWarriors = avg(WarriorsRatings)
    averageLakers = avg(LakersRatings)
    averageBulls = avg(BullsRatings)
    averageKnicks = avg(KnicksRatings)
    averageCeltics = avg(CelticsRatings)

    # teamratingslist is used to calculate the score outside of the draft() function, which is why it needs to be global.
    global teamratingslist
    teamratingslist = [averageUserTeam, averageWarriors, averageLakers, averageBulls, averageKnicks, averageCeltics]
    return teamratingslist

# This function randomizes a score for every given game, and ensures that every score is a realistic basketball score.
# After trial and error, most teams' average rating fell between 86 and 88.
# To ensure that the better rated teams would have better records, the teams with slightly higher ratings have a better chance at having a higher score.
# A random integer is generated to be added to the the rating of the team itself, and this is actual score
# If the team's rating is higher, they have a range of random integers that can be generated that is more favorable.
def score(rating):
    if rating < 86:
        x = random.randint(-15, 10)
        finalscore = int(rating + x)
        return finalscore
    if rating >= 86 and rating < 87:
        x = random.randint(-12, 20)
        finalscore = int(rating + x)
        return finalscore
    if rating >= 87 and rating < 87.5:
        x = random.randint(-5, 30)
        finalscore = int(rating + x)
        return finalscore
    if rating >= 87.5 and rating < 88:
        x = random.randint(0, 35)
        finalscore = int(rating + x)
        return finalscore
    if rating >= 88:
        x = random.randint(8, 45)
        finalscore = int(rating + x)
        return finalscore
    
# This is a simple function to be used to add wins to the lists established at the beginning of the program.
# This makes it easier to generate the records at the end of the season.
def addwin(team):
    win = 'W'
    if team == userTeam:
        userTeamWins.append(win)
    elif team == 'Warriors':
        WarriorsWins.append(win)
    elif team == 'Lakers':
        LakersWins.append(win)
    elif team == 'Bulls':
        BullsWins.append(win)
    elif team == 'Knicks':
        KnicksWins.append(win)
    elif team == 'Celtics':
        CelticsWins.append(win)

# The game() function takes in two team names, and each team's corresponding rating.
# It uses the score() function to generate two scores, and whichever team has the higher score is awarded a win with the addwin() function.
def game(team1, rating1, team2, rating2):

    a = score(rating1)
    b = score(rating2)
    score1 = str(a)
    score2 = str(b)

    print('Final Score: ' + team1 + ' ' + score1 + ' ' + team2 + ' ' + score2)

    if a > b:
        addwin(team1)
    elif b > a:
        addwin(team2)

# This function displays the records at the end of the 10 game season.
# This takes in the length of each team's win list.
# This length is subtracted from 10 to determine the amount of losses
# The team with the best record is the Champion, and if there is a tie, there are co-Champions.
def displayrecords(team):

    bos = len(CelticsWins)
    nyk = len(KnicksWins)
    chi = len(BullsWins)
    lal = len(LakersWins)
    gsw = len(WarriorsWins)
    user = len(userTeamWins)

    print('Here are the final records!')

    listofrecords = [bos, nyk, chi, lal, gsw, user]
    listofrecords.sort(reverse=True)
    print(team + ' ' + str(user) + '-' + str(10-user))
    print('Celtics ' + str(bos) + '-' + str(10-bos))
    print('Knicks ' + str(nyk) + '-' + str(10-nyk))
    print('Bulls ' + str(chi) + '-' + str(10-chi))
    print('Lakers ' + str(lal) + '-' + str(10-lal))
    print('Warriors ' + str(gsw) + '-' + str(10-gsw))
    time.sleep(0.5)

    maxwins = max(listofrecords)
    count = listofrecords.count(maxwins)

    if count == 1:
    
        if max(listofrecords) == bos:
            print('The Boston Celtics have won the NBA Championship! Thank you for playing!')
        if max(listofrecords) == nyk:
            print('The New York Knicks have won the NBA Championship! Thank you for playing!')
        if max(listofrecords) == chi:
            print('The Chicago Bulls have won the NBA Championship! Thank you for playing!')
        if max(listofrecords) == lal:
            print('The Los Angeles Lakers have won the NBA Championship! Thank you for playing!')
        if max(listofrecords) == gsw:
            print('The Golden State Warriors have won the NBA Championship! Thank you for playing!')
        if max(listofrecords) == user:
            print('Your ' + team + ' have won the NBA Championship!!! You built an incredible team. Thank you for playing! Great Job!')
    
    if count > 1:
        print('There are co-Champions! Congratulaitons to all teams who tied for the best record on great seasons! Thank you for playing!')

# This is where the main program is run. Much of the print statements here are to enhance the presentation of the game.
if __name__ == "__main__":
    print('Welcome to NBA Manager Version 1.0! You will be tasked with managing your own NBA team!')
    print('You must guide your team from the Fantasy Draft up until the end of the regular season, and hopefully the playoffs!')
    print('You can choose your own team name and will compete against 5 other existing other NBA teams.')
    time.sleep(5)
    print('These teams are the Los Angeles Lakers, Golden State Warriors, Chicago Bulls, New York Knicks, and Boston Celtics. These are 5 of the most storied franchises in NBA history.')
    print('The regular seasons consists of 10 games, and the team with the best record wins the crown of NBA Champion!')
    time.sleep(5)
    print('It is time to choose your team! Please only enter the mascot name of the team you wish to choose.')
    userTeam = input('Enter your team name in here:  ')
    time.sleep(2)
    draft(userTeam) # This is where the draft() function is run.
    time.sleep(3)
    print('')
    print('Here is the list of each teams average rating, ordered from left to right being your team, Warriors, Lakers, Bulls, Knicks, and Celtics.')
    time.sleep(5)
    print(teamratingslist) # Here it prints the teamratingslist, with the corresponding order included in the print statement above.
    print('')
    time.sleep(10)

    # It uses teamratingslist to determine the individual average rating of each team.
    # This is possible because the order of teamratingslist is known and I used each index value of each corresponding team.
    # Each team's average rating is then used in the game() function to calculate the scores of each game.
    userTeamAvg = teamratingslist[0]
    WarriorsAvg = teamratingslist[1]
    LakersAvg = teamratingslist[2]
    BullsAvg = teamratingslist[3]
    KnicksAvg = teamratingslist[4]
    CelticsAvg = teamratingslist[5]

    # Week 1 (This program follows a fixed schedule of games. Each week consists of 3 games in which it calls the game() function.)
    print('Welcome to Week 1 of the Season. First, the ' + userTeam + ' play their first game, against the Warriors. The simulation begins!')
    time.sleep(2)
    game(userTeam, userTeamAvg, 'Warriors', WarriorsAvg)
    game('Lakers', LakersAvg, 'Bulls', BullsAvg)
    game('Celtics', CelticsAvg, 'Knicks', KnicksAvg)
    time.sleep(3)

    # Week 2
    print('Welcome to Week 2. You play the Lakers. Here are the simulations for this week.')
    time.sleep(2)
    game(userTeam, userTeamAvg, 'Lakers', LakersAvg)
    game('Warriors', WarriorsAvg, 'Celtics', CelticsAvg)
    game('Bulls', BullsAvg, 'Knicks', KnicksAvg)
    time.sleep(3)

    # Week 3
    print('Welcome to Week 3. You play the Celtics. Here are the simulations for this week.')
    time.sleep(2)
    game('Celtics', CelticsAvg, userTeam, userTeamAvg)
    game('Knicks', KnicksAvg, 'Lakers', LakersAvg)
    game('Warriors', WarriorsAvg, 'Bulls', BullsAvg)
    time.sleep(3)

    # Week 4
    print('Welcome to Week 4. You play the Bulls. Here are the simulations for this week.')
    time.sleep(2)
    game('Bulls', BullsAvg, userTeam, userTeamAvg)
    game('Celtics', CelticsAvg, 'Lakers', LakersAvg)
    game('Knicks', KnicksAvg, 'Warriors', WarriorsAvg)
    time.sleep(3)

    # Week 5
    print('Welcome to Week 5. You play the Knicks. Here are the simulations for this week.')
    time.sleep(2)
    game(userTeam, userTeamAvg, 'Knicks', KnicksAvg)
    game('Lakers', LakersAvg, 'Warriors', WarriorsAvg)
    game('Bulls', BullsAvg, 'Celtics', CelticsAvg)
    time.sleep(3)

    # Week 6
    print('Welcome to Week 6. You play the Lakers. Here are the simulations for this week.')
    time.sleep(2)
    game(userTeam, userTeamAvg, 'Lakers', LakersAvg)
    game('Warriors', WarriorsAvg, 'Celtics', CelticsAvg)
    game('Bulls', BullsAvg, 'Knicks', KnicksAvg)
    time.sleep(3)

    # Week 7
    print('Welcome to Week 7. You play the Celtics. Here are the simulations for this week.')
    time.sleep(2)
    game('Celtics', CelticsAvg, userTeam, userTeamAvg)
    game('Knicks', KnicksAvg, 'Lakers', LakersAvg)
    game('Warriors', WarriorsAvg, 'Bulls', BullsAvg)
    time.sleep(3)

    # Week 8
    print('Welcome to Week 8. You play the Warriors. Here are the simulations for this week.')
    time.sleep(2)
    game(userTeam, userTeamAvg, 'Warriors', WarriorsAvg)
    game('Lakers', LakersAvg, 'Bulls', BullsAvg)
    game('Celtics', CelticsAvg, 'Knicks', KnicksAvg)
    time.sleep(3)

    # Week 9
    print('Welcome to Week 9. You play the Knicks. Here are the simulations for this week.')
    time.sleep(2)
    game(userTeam, userTeamAvg, 'Knicks', KnicksAvg)
    game('Lakers', LakersAvg, 'Warriors', WarriorsAvg)
    game('Bulls', BullsAvg, 'Celtics', CelticsAvg)
    time.sleep(3)

    # Week 10
    print('Welcome to the final week of the season. It all comes down to this. You play the Bulls.')
    time.sleep(2)
    game('Bulls', BullsAvg, userTeam, userTeamAvg)
    game('Celtics', CelticsAvg, 'Lakers', LakersAvg)
    game('Knicks', KnicksAvg, 'Warriors', WarriorsAvg)
    time.sleep(3)

    # Display the Final Records and Declare a Champion
    print('')
    displayrecords(userTeam)
