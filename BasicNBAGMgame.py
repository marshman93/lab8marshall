import random

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

playerlist = []
for x, y in playerDict.items():
    playerlist.append(x)

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

def avg(ratings):
    return sum(ratings) / len(ratings)

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
    print('Here are the players remaining after Round #' + roundnum + '!')
    for x, y in playerDict.items():
        print(x,y)

def draft(team):
    print('Welcome to the Fantasy Draft! You are controlling the ' + team + '.')
    draftorder = ['Lakers', 'Warriors', 'Bulls', 'Knicks', 'Celtics', team]
    random.shuffle(draftorder)
    print('Before the draft begins, it will be important to know who is available. Here is a list of the 60 players you can draft!')
    for x, y in playerDict.items():
        print(x,y)
    print('The draft order has been randomized. It is ' + str(draftorder) + '.')
    print('You will select 10 players, and therefore there will be 10 rounds in this draft.')
    print('The draft is a snake draft, so the team with the 6th pick will get the 7th pick, 5th with 8th, and so on.')
    print('Let the Fantasy Draft begin! Good luck!')
    reversedraftorder = draftorder[::-1]

    rounds(team, 1, draftorder)
    rounds(team, 2, reversedraftorder)
    rounds(team, 3, draftorder)
    rounds(team, 4, reversedraftorder)
    rounds(team, 5, draftorder)
    rounds(team, 6, reversedraftorder)
    rounds(team, 7, draftorder)
    rounds(team, 8, reversedraftorder)
    rounds(team, 9, draftorder)

    # The 10th round does not include choosing players by chance for the other teams because there are only 6 players left, so it exists as its own separate function.
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
    print('Congratulations! The Fantasy Draft is complete and all teams are filled!')
    print('Here is what the ' + team + ' look like. First, there is your roster of players, and after is each players corresponding rating.')
    print(userTeam1.players)
    print(userTeam1.ratings)
    print('In addition, here are the other teams rosters.')
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

    global teamratingslist
    teamratingslist = [averageUserTeam, averageWarriors, averageLakers, averageBulls, averageKnicks, averageCeltics]
    return teamratingslist

def score(rating):

    x = random.randint(-10,30)
    finalscore = int(rating + x)
    return finalscore

def game(team1, rating1, team2, rating2):

    a = score(rating1)
    b = score(rating2)
    score1 = str(a)
    score2 = str(b)

    print('Final Score: ' + team1 + ' ' + score1 + ' ' + team2 + ' ' + score2)


if __name__ == "__main__":
    print('Welcome to NBA Manager Version 1.0! You will be tasked with managing your own NBA team!')
    print('You must guide your team from the Fantasy Draft up until the end of the regular season, and hopefully the playoffs!')
    print('You can choose your own team name and will compete against 5 other existing other NBA teams.')
    print('These teams are the Los Angeles Lakers, Golden State Warriors, Chicago Bulls, New York Knicks, and Boston Celtics. These are 5 of the most storied franchises in NBA history.')
    print('The regular seasons consists of 12 games, and the 4 best records make the playoffs.')
    print('The playoffs are a best of 5 series for the Semifinals and a best of 7 series for the crown of NBA Champion!')
    print('It is time to choose your team! Please only enter the mascot name of the team you wish to choose.')
    userTeam = input('Enter your team name in here:  ')
    draft(userTeam)
    print(teamratingslist)
    userTeamAvg = teamratingslist[0]
    WarriorsAvg = teamratingslist[1]
    LakersAvg = teamratingslist[2]
    BullsAvg = teamratingslist[3]
    KnicksAvg = teamratingslist[4]
    CelticsAvg = teamratingslist[5]
    game(userTeam, userTeamAvg, 'Warriors', WarriorsAvg)
