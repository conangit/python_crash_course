

from survey import AnonymousSurvey

question = 'What language did you first learn to speek ?'

my_survey = AnonymousSurvey(question)
my_survey.show_question()

print("Enter 'q' to quit at any time")
while True:
    response = input('Language: ')
    if response == 'q':
        break
    my_survey.store_response(response)

my_survey.show_results()

