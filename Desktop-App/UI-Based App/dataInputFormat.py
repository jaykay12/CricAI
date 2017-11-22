import sys
import datasetRead

if __name__ == '__main__':
    ReadDataSet()

d = datasetRead.Dataset()

class DataInput:
    def hashAll(self):
        self.hashingTeam1()
        self.hashingTeam2()
        self.hashingGrounds()
        self.hashingInnings()
        self.hashingVenue()
        self.hashingTargetWinners()

    def hashingTeam1(self):
        d.ReadDataSet()
        self.ourTeams_1 = {}
        for i,teams in enumerate(list(d.match_data.columns)):
            if i==23:
                break
            teamName = str(teams)
            teamName = teamName.split("Team 1_", 1)[-1]
            self.ourTeams_1[teamName] = i

    def hashingTeam2(self):
        d.ReadDataSet()
        self.ourTeams_2 = {}
        for i,teams in enumerate(list(d.match_data.columns)):
            if i<23:
                continue
            if i==46:
                break
            teamName = str(teams)
            teamName = teamName.split("Team 2_", 1)[-1]
            self.ourTeams_2[teamName] = i

    def hashingGrounds(self):
        d.ReadDataSet()
        self.ourGrounds = {}
        for i,grounds in enumerate(list(d.match_data.columns)):
            if i<46:
                continue
            if i==207:
                break
            groundName = str(grounds)
            groundName = groundName.split("Ground_", 1)[-1]
            self.ourGrounds[groundName] = i

    def hashingInnings(self):
        self.ourInnings = {'Team1_1Inning': 207, 'Team1_2Inning': 208, 'Team2_1Inning': 209, 'Team2_2Inning': 210}

    def hashingVenue(self):
        self.ourVenues = {'Team1_Away': 211, 'Team1_Home': 212, 'Team1_Neutral': 213, 'Team2_Away': 214, 'Team2_Home': 215, 'Team2_Neutral': 216}

    def hashingTargetWinners(self):
        d.ReadDataSet()
        self.winnerIndex = {}
        counter = 0
        for i,teams in enumerate(list(d.match_data.columns)):
            if i<217:
                continue
        
            teamName = str(teams)
            teamName = teamName.split("Winner_", 1)[-1]
            self.winnerIndex[teamName] = counter
            counter+=1