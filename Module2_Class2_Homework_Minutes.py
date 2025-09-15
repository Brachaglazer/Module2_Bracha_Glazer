"""
Bracha Glazer
Convert the user's amount of minutes to hours and minutes.
"""


"""The function requests a number of minutes from the user and then calculates how many hours and minutes can be extracted from the user's amount of minutes."""
#I am defining and beginning my funcion.
def minutes_to_hours_and_minutes():
    minutes = float(input("How many minutes? ")) #I am asking the user how many minutes they would like to calculate. I am putting it into floating-point number so that in case the user inputs a decimal it will still work properly.
    #I am clarifying what this program will do with the information the user has inputted and displaying it on the screen for the user to see.
    print("The user wants to calculate how many hours and minutes can be extracted from", minutes, "minutes.")
    hours = minutes // 60 #I am creating the variable "hours", which is the amount of minutes the user has inputted divided by 60 through integer division so that only the minutes that go evenly into hours will be used.
    minutes_answer = minutes % 60 #I am creating the variable "minutes_answer", which is the remainder when the amount of minutes the user has inputted is divided by 60. This covers for the part that "hours" cuts out.
    #I am printing the answer for the user to see.
    print(hours, "Hours and", minutes_answer, "minutes can be extracted from your", minutes, "minutes.")
    #I am closing my definition.
minutes_to_hours_and_minutes()
