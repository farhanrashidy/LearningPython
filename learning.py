import random

def get_choice():
    player_choice = input("Enter your choice (Rock, Paper, Scissors): ")
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice,
               "computer": computer_choice}
    return choices

def check_win(player, computer):
    return [player, computer]



