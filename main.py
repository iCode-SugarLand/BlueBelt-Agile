import pygame
import sys
from pygame.locals import *
pygame.init()
from random import randint


questions = ["Who is the Scrum Master?",
             "What is the first index value in a list",
             "What color is 0,0,0",
             "What is a common key word/phrase you see when looping",
             "How many radians are in a full circle",
             "How many degrees are in a circle?",
             "What is the value in parenthesis in a function called",
             "How many pairs of chromosomes are in the average human?",
             "What is a gamete cell",
             "Who is the biggest mistake in the room",
             "What is Trisomy 21 also referred as",
             "Where did python get its name?",
             "What does 'soh' in SOHCAHTOA stand for?",
             "What does a resistor resist?",
             "What disease/infection is Daniel Larson currently spreading all over SoCal?",
             "How many keys does a computer keyboard have?",
             "What is the end of a shoelace called?",
             "What is the loudest animal on Earth?"
             ]

answers = [
    ["Daniyal","Eleaf", "Thomas", "Ryan"],
    ["1", "0", "2", "10"],
    ["Black", "Blue", "White", "Pink"],
    ["For", "Interlock Setup", "Interlock Result"],
    ["π", "9π", "0", "2π"],
    ["360", "180", "100", "90"],
    ["Definition", "Argument", "Number", "variable"],
    ["23", "46", "48", "24"],
    ["sex cell", "the white stripes", "diploid cell", "somatic cell"],
    ["Elif","Elif","Elif","Daniyal"],
    ["Down bad syndrome", "Elif syndrome", "Jermaphobia", "Down syndrome"],
    ["An icecream company that gave them icecream","The owner got bit by a python","They just thought of a random name","It was named after the comedy troupe Monty Python"],
    ["Cos Opp Adj", "Tan Opp Hyp", "Sin Opp Hyp", "Sin Adj Hyp"],
    ["Resists food", "Resists further action", "Resists electricity", "Resists needs"],
    ["Scabies", "COVID", "Smallpox", "MRSA"],
    ["69", "66", "88", "32"],
    ["String", "Aglet", "Tip", "Juxtaposition"],
    ["Sperm Whale", "Lion", "Blue whale", "African Elephant"]
]

correct = [0, 1, 0, 0, 2, 0, 1, 0, 0, 2, 3, 3, 2, 2, 0, 1, 1, 0]

randomOrder = []
score = 0

randomNumber = randint(0, len(questions)-1)

while len(randomOrder) < len(questions):
    if randomNumber not in randomOrder:
        randomOrder.append(randomNumber)
        randomNumber = randint(0, len(questions)-1)
    elif randomNumber in randomOrder:
        randomNumber = randint(0, len(questions)-1)

print("size of questions list: ", len(questions))
print("size of answers list: ", len(answers))
print("size of correct list: ", len(correct))


for i in range(len(questions)):
    print(questions[randomOrder[i]])
    print(answers[randomOrder[i]])
    userSelection = int(input("Please pick one [0, 1, 2, 3] "))

    if correct[randomOrder[i]] == userSelection:
        score += 5
    print(score)


if score >= 70:
    print(score)
    MySurf = pygame.display.set_mode((500,400))
    pygame.display.set_caption("Results")
    MySurf.fill((0, 255, 0))
    print("You Passed!")
else:
    print(score)
    MySurf = pygame.display.set_mode((500, 400))
    pygame.display.set_caption("Results")
    MySurf.fill((255, 0, 0))
    print("You failed l bozo")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
