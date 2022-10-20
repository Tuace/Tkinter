import requests
AMOUNT=10
DIFFICULTY= "hard"
TYPE="boolean"
CATEGORY=18
parameters = {
    "amount": AMOUNT,
    "difficulty": DIFFICULTY,
    "type": TYPE


}

questions = requests.get(url="https://opentdb.com/api.php", params= parameters)
questions.raise_for_status()
data = questions.json()
question_data=(data["results"])



#https://opentdb.com/api.php?amount=10&difficulty=hard&type=boolean


