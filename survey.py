#science
#games
#instagram
print("SURVEY")
computer_science=input("Are you interested in computer science? (y/n):")
computer_science=computer_science.lower()=="y"
computer_games=input("Do you like playing computer games? (y/n):")
computer_games=computer_games.lower()=="y"
instagram=input("o you have an Instagram account? (y/n):")
instagram=instagram.lower()=="Y"

print("SURVEY RESULTS")

if computer_science:
    print("Interested in computer science: Yes")
else:
    print("Interested in computer science: No")

if computer_games:
    print("Playing computer games: Yes")
else:
    print("Playing computer games: No")

if instagram:
    print("Has an Instagram account: Yes")
else:
    print("Has an Instagram account: No")
