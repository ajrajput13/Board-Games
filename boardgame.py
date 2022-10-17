'''
Author: Ansh Rajput
Date: Monday, January 24, 2022
Last modified: Saturday, Janurary 29
Purpose: The purpose of the boardgame class is to create the variables that
         the Executive class will use. It also creates a format that will be
         used.
            
'''

class Boardgame():

    def __init__(self, name, year, G_rating, P_rating, min_players, playtime):
        self.name = name
        self.year = year
        self.G_rating = G_rating
        self.P_rating = P_rating
        self.min_players = min_players
        self.playtime = playtime

    def get_year(self):
        return(self.year)
    
    def set_year(self, yearNum):
        self.year = yearNum
      
    def __str__(self):
        return(f"{self.name} ({self.year}) [GR={self.G_rating}, PR={self.P_rating}, MP={self.min_players},MT={self.playtime}]")
