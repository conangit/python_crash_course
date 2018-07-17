
import unittest

from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    '''
    针对AnonymousSurvey类的测试
    '''
    def test_single_response(self):
        '''测试一个答案会被妥善储存'''
        question = 'What language did you first learn to speek ?'
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)

    def test_three_responses(self):
        '''测试三个答案会被妥善储存'''
        question = 'What language did you first learn to speek ?'
        my_survey = AnonymousSurvey(question)
        responses = ['Chinese', 'English', 'Franch']
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)


unittest.main()

