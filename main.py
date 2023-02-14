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
             "How many bones does a shark have?",
             "What is Trisomy 21 also referred as",
             "Where did python get its name?",
             "What does 'soh' in SOHCAHTOA stand for?",
             "What does a resistor resist?",
             "Who is the patron saint of Ireland?",
             "How many keys does a computer keyboard have?",
             "What is the end of a shoelace called?",
             "What is the loudest animal on Earth?",
             "How many time zones are in Russia?",
             "Who Painted the Mona Lisa"
             ]

answers = [
    ["Daniyal", "Eleaf", "Thomas", "Ryan"],
    ["1", "0", "2", "10"],
    ["Black", "Blue", "White", "Pink"],
    ["For", "Interlock Setup", "Interlock Result", "After"],
    ["π", "9π", "0", "2π"],
    ["360", "180", "100", "90"],
    ["Definition", "Argument", "Number", "variable"],
    ["23", "46", "48", "24"],
    ["sex cell", "the white stripes", "diploid cell", "somatic cell"],
    ["147", "256", "0", "468"],
    ["salamander disease", "Marinara-syndrome", "Jermaphobia", "Down syndrome"],
    ["An icecream company that gave them icecream", "The owner got bit by a python", "They just thought of a random name", "It was named after the comedy troupe Monty Python"],
    ["Cos Opp Adj", "Tan Opp Hyp", "Sin Opp Hyp", "Sin Adj Hyp"],
    ["Resists food", "Resists further action", "Resists electricity", "Resists needs"],
    ["St Patrick", "St Ajora", "St Bernard", "St Anthony"],
    ["69", "66", "88", "32"],
    ["String", "Aglet", "Tip", "Juxtaposition"],
    ["Sperm Whale", "Lion", "Blue whale", "African Elephant"],
    ["14", "1", "11", "18"],
    ["Leonardo DiCaprio", "Rafael Lopez", "Leonardo DaVinci", "Michelangelo"]
]

correct = [0, 1, 0, 0, 2, 0, 1, 0, 0, 2, 3, 3, 2, 2, 0, 1, 1, 0, 2, 2]

randomOrder = []
score = 0

randomNumber = randint(0, len(questions)-1)

while len(randomOrder) < len(questions):
    if randomNumber not in randomOrder:
        randomOrder.append(randomNumber)
        randomNumber = randint(0, len(questions)-1)
    elif randomNumber in randomOrder:
        randomNumber = randint(0, len(questions)-1)

# print("random order list: ", randomOrder)
# print("size of questions list: ", len(questions))
# print("size of answers list: ", len(answers))
# print("size of correct list: ", len(correct))
# print()


for i in range(len(questions)):
    print(i + 1, ". ", questions[randomOrder[i]])
    for j in range(len(answers[randomOrder[i]])):
        print("  ", j+1, ". ", answers[randomOrder[i]][j])
    userSelection = int(input("Please pick one: "))
    if userSelection < 1 or userSelection > 4:
        while userSelection < 1 or userSelection > 4:
            userSelection = int(input("Please make a valid selection between 1 - 4: "))
    userSelection = userSelection - 1
    if correct[randomOrder[i]] == userSelection:
        score += 5
    print("\nCurrent Score: ", score,"\n")


# if score >= 70:
#     print(score)
#     MySurf = pygame.display.set_mode((500, 400))
#     pygame.display.set_caption("Results")
#     MySurf.fill((0, 255, 0))
#     print("You Passed!")
# else:
#     print(score)
#     MySurf = pygame.display.set_mode((500, 400))
#     pygame.display.set_caption("Results")
#     MySurf.fill((255, 0, 0))
#     print("You failed")

MySurf = pygame.display.set_mode((500, 400))
pygame.display.set_caption("result")
font = pygame.font.Font('freesansbold.ttf', 32)
white = (255, 255, 255)
scoreStr = (str(score))
scoreText = ('Your score was: ' + scoreStr + '/100')

if score >= 70:
    background = (34, 139, 34)
    text = font.render('Congratulations. You won!!', True, white, background)
else:
    background = (210, 20, 4)
    text = font.render('Sorry, try again...', True, white, background)

textRect = text.get_rect()
textRect.center = (500 // 2, 400//3)

scoreDisp = font.render(scoreText, True, white, background)
scoreDispRect = scoreDisp.get_rect()
scoreDispRect.center = (500//2, 400//2)

while True:
    MySurf.fill(background)
    MySurf.blit(text, textRect)
    MySurf.blit(scoreDisp, scoreDispRect)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
