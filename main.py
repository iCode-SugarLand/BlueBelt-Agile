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
             "What is Trisomy 21 also referred as"
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
    ["Down bad syndrome", "Elif syndrome", "Jermaphobia", "Down syndrome"]
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

for i in range(len(questions)):
    print(questions[randomOrder[i]])
    print(answers[randomOrder[i]])
    userSelection = input("Please make a selection: ")
