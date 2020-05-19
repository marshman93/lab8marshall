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

class Lakers():
    ratings = []
    def __init__(self, player):
        self.name = player
    def add_rating(self, rating):
        self.ratings.append(rating)

class Warriors():
    ratings = []
    def __init__(self, player):
        self.name = player
    def add_rating(self, rating):
        self.ratings.append(rating)

class Spurs():
    ratings = []
    def __init__(self, player):
        self.name = player
    def add_rating(self, rating):
        self.ratings.append(rating)

class Bulls():
    ratings = []
    def __init__(self, player):
        self.name = player
    def add_rating(self, rating):
        self.ratings.append(rating)

class Knicks():
    ratings = []
    def __init__(self, player):
        self.name = player
    def add_rating(self, rating):
        self.ratings.append(rating)

class Celtics():
    ratings = []
    def __init__(self, player):
        self.name = player
    def add_rating(self, rating):
        self.ratings.append(rating)

if __name__ == "__main__":
    print('Welcome to NBA Manager Version 1.0! You will be tasked with managing one of the six NBA teams that are in this game!')
    print('You must guide your team from the Fantasy Draft up until the end of the regular season, and hopefully the playoffs!')
    print('There are six teams to choose from, which are the 6 most storied franchises in NBA history.')
    print('These teams are the LA Lakers, Golden State Warriors, San Antonio Spurs, Chicago Bulls, New York Knicks, and Boston Celtics.')
    print('There are two divisons: the East and the West.')
    print('The Lakers, Warriors, and Spurs are in the West, while the Bulls, Knicks, and Celtics are in the East.')
    print('The regular seasons consists of 12 games, and the two best records from each divsion make the playoffs.')
    print('The playoffs are a best of 5 series for the Division Championship and a best of 7 series for the crown of NBA Champion!')
    print('It is time to choose your team! Please only enter the mascot name of the team you wish to choose.')
    userTeam = input('The options are Lakers, Warriors, Spurs, Bulls, Knicks and Celtics. Enter your team name in here:  ')
