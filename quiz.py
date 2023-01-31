from random import randint
import pygame
from pygame.locals import *

pygame.init()

questions = [
    "Who is the Scrum Master?",
    "Who is the smartest person in the room?",
    "What is the first index value in a list?",
    "What color is RGB value: 0, 0, 0?",
    "What is a common keyword/phrase you see when looping things?",
    "How many radians are in a full circle?",
    "How many degrees are in a circle?",
    "What is the value in parenthesis in a function called?",
    "How many pairs of chromosomes are in the average human?",
    "What is a gamete cell?"
]

answers = [
    ["Daniyal", "Eleaf", "Thomas", "Ryan"],
    ["Daniyal", "Eleaf", "Thomas", "Julian Fernando Casablancas"],
    ["1", "0", "2", "10"],
    ["Black", "Blue", "White", "Pink"],
    ["For", "Interlock Setup", "Interlock Result"],
    ["π", "9π", "0", "2π"],
    ["360", "180", "100", "90"],
    ["Definition", "Argument", "Number", "Variable"],
    ["23", "46", "48", "24"],
    ["sex cell", "the white stripes", "diploid cell", "somatic cell"]
]

randomOrder = []
score = 0

randomNumber = randint(0, len(questions)-1)

while len(randomOrder) < len(questions):
    if randomNumber not in randomOrder:
        randomOrder.append(randomNumber)
        randomNumber = randint(0, len(questions)-1)
    elif randomNumber in randomOrder:
        randomNumber = randint(0, len(questions)-1)

print(randomOrder)

for i in range(len(randomOrder)):
    randomNumber = randomOrder[i]
    print(i+1, ": ", questions[randomNumber])
    for j in range(len(answers[randomNumber])):
        print("    ", j+1, ": ", answers[randomNumber][j])
    userNum = int(input("Enter a number: "))

    if randomNumber == 0:
        if userNum == 1:
            score += 5
    if randomNumber == 1:
        if userNum == 1:
            score += 5
    if randomNumber == 2:
        if userNum == 2:
            score += 5
    if randomNumber == 3:
        if userNum == 1:
            score += 5
    if randomNumber == 4:
        if userNum == 1:
            score += 5
    if randomNumber == 5:
        if userNum == 4:
            score += 5
    if randomNumber == 6:
        if userNum == 1:
            score += 5
    if randomNumber == 7:
        if userNum == 2:
            score += 5
    if randomNumber == 8:
        if userNum == 1:
            score += 5
    if randomNumber == 9:
        if userNum == 1:
            score += 5
    print()

print("Score: ", score)

if score > 30:
    backgroundColor = (0, 255, 0)
else:
    backgroundColor = (255, 0, 0)

WIDTH = 500
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quiz Results")

screen.fill(backgroundColor)
pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
