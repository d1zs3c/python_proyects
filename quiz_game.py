print("welcome to my first game :)")

playing = input("Do you want yo play?(yes/no) ")

if playing.lower() != "yes":
        quit()

print("Okey! Let`s play")
score = 0
answer1 = input("What does CPU stand for? ")
if answer1.lower() == "central processing unit":
    score += 1
    print("Correct!")
else:
    print("Incorrect :(")

answer1 = input("What does GPU stand for? ")
if answer1.lower() == "graphics processing unit":
    score += 1
    print("Correct!")
else:
    print("Incorrect :(")

answer1 = input("What does RAM stand for? ")
if answer1.lower() == "random access memory":
    score += 1
    print("Correct!")
else:
    print("Incorrect :(")

print("Your total score is: " + str((score/3)*100) + "%")