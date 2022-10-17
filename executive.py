'''
Author: Ansh Rajput
Date: Monday, January 24, 2022
Last modified: Sunday, Janurary 30
Purpose: The purpose of the executive class is to print the menu and handle all the
         user interactions. It uses the boardgame class to format and print all of
         the games based on what the user chooses.
'''

from boardgame import Boardgame

class Executive():

    def printMenu(): #prints the menu when called
        print("\nMake a selection")
        print("1) Print all games")
        print("2) Print all games from a year")
        print("3) Print a ranking range")
        print("4) The People VS Dr. Gibbons")
        print("5) Print based on play time")
        print("6) Exit the program\n")


    gameFile = open("gamedata.txt", "r")
    gameList = []
    for line in gameFile:
        line = line.strip()
        line = line.split()
        gameList.append(line)
    gameFile.close()

    while True:
        printMenu()
        userInput = int(input("Enter a number: "))

        if userInput == 1:
            print("Print all games:\n")
            for game in gameList:
                game = Boardgame(game[0], game[1], game[2], game[3], game[4], game[5])
                print(game.__str__())
                
        if userInput == 2:
            userYear = input("Enter a year: ")
            print("Print all games from " + userYear + ":\n")
            for game in gameList:
                if userYear == game[1]:
                    game = Boardgame(game[0], game[1], game[2], game[3], game[4], game[5])
                    print(game.__str__())

        if userInput == 3:
            userLowRating = float(input("Enter a minimum rating: "))
            userHighRating = float(input("Enter a maximum rating: "))
            print("Print all games between the rating of " + str(userLowRating) + " - " + str(userHighRating) + ":\n")
            for game in gameList:
                GRating = float(game[2])
                if userLowRating < GRating and userHighRating > GRating:
                    game = Boardgame(game[0], game[1], game[2], game[3], game[4], game[5])
                    print(game.__str__())

        if userInput == 4:
            userNum = float(input("Enter a number to compare the people's rating and Gibbon's rating: "))
            print("Print all games where people's rating and Dr. Gibbons rating are separated by " + str(userNum) + ":\n")
            for game in gameList:
                ratingDifference = float(game[3]) - float(game[2])
                if ratingDifference < 0:
                    ratingDifference = ratingDifference * -1
                if userNum <= ratingDifference:
                    game = Boardgame(game[0], game[1], game[2], game[3], game[4], game[5])
                    print(game.__str__())

        if userInput == 5:
            userPlaytime = int(input("Enter a play time: "))
            print("Print all games with a play time less than or equal to " + str(userPlaytime) + ":\n")
            for game in gameList:
                playtime = int(game[5])
                if userPlaytime >= playtime:
                    game = Boardgame(game[0], game[1], game[2], game[3], game[4], game[5])
                    print(game.__str__())
            
        if userInput == 6:
            print("Exiting...")
            break

