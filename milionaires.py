import requests
import json
import random
import apihidden

url = "https://api.openai.com/v1/chat/completions"
apiKey = apihidden.getApi()
subject_database = ["animals","geography","cars","boats","history","World War II","heroes","buildings","computer science","Python coding","API requests","Docker"]
level=0
mistakes=0

header = {
    'Content-Type': 'application/json',
    'Authorization': apiKey}

def getQuestion(question_sentence):

    data = {
    'model': "gpt-3.5-turbo",
    'messages': [
        {
            'role':'user',
            'content': question_sentence
        }
    ],
     'temperature':0.3,
     'n':1
  }

    response = requests.post(url, headers=header, data=json.dumps(data))

    if response.status_code != 200:
        print("Error with status code:", response.status_code)
        print("Response content:", response.content)
    else:
        response_content = response.json()['choices'][0]['message']['content']
        return response_content
    
def getAnswer(question_sentence, answer_generated):

    good_answer_letter = "Write correct answer's letter. Only letter. Not whole answer."
    data = {
        'model': "gpt-3.5-turbo",
        'messages': [
            {
                'role':'user',
                'content': question_sentence
            },
            {
                'role':'assistant',
                'content': answer_generated,
            },
            {
                'role':'user',
                'content': good_answer_letter
            }
        ],
        'temperature':0.3,
        'n':1
    }

    response = requests.post(url, headers=header, data=json.dumps(data))

    if response.status_code != 200:
        print("Error with status code:", response.status_code)
        print("Response content:", response.content)
    else:
        response_content = response.json()['choices'][0]['message']['content']
        return response_content


def checkAnswerOneLetter(inputText1, inputText2):
    answer = getAnswer(inputText1,inputText2)
    while (len(answer) != 1):
        answer = getAnswer(inputText1,inputText2)
    
    return answer

def checkUserAnswer(answer, goodAnswer):
    if answer.upper() != goodAnswer.upper():
       return False
    else:
       return True
    
def oneRound(difficulty):
    global level
    global mistakes
    subject = random.choice(subject_database)
    question = "Write ONE question, subject " + subject + ". Write 4 answers A, B, C and D, only one good and three wrong. Do not write which is good. Question difficulty in scale 0(easy), 9(extremely difficult) should be exactly " + str(difficulty)
    choices = getQuestion(question)
    print(choices)
    print()
    goodLetter = checkAnswerOneLetter(question, choices)
    userAnswer = input('Choose correct question A-D or Q to quit: ')
    if userAnswer == 'Q':
       exit()
    if checkUserAnswer(userAnswer, goodLetter):
       print('Good answer!')
       print()
       level = level + 1
    else:
       print('Bad! Correct answer is ' + goodLetter)
       mistakes=mistakes+1
       if mistakes<3:
           print('You can make only ' + str(3-mistakes) + ' mistakes more.')
       else:
           print('Game over!')
           exit()
       print()

while(level<10):
    print("Question level: " + str(level))
    oneRound(level)

print('You won!')
