'''
Author: Ansh Rajput
Date: Monday, January 24, 2022
Last modified: Saturday, Janurary 29
Purpose: The purpose of the driver is to conatin main() which
         asks the user to input a file and then calls the
         Executive class if that file exists.
'''

def main(): #Asks user for a file and if the file matches, gives control to Executive class
    file_name = input("Enter the name of the input file: ")
    if file_name == "gamedata.txt":
        from executive import Executive
    else:
        print("File not found.")

if __name__ == "__main__":
    main()


