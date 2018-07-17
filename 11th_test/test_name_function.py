
import unittest

from name_function import get_formatted_name



class NameTestCase(unittest.TestCase):
    '''
    测试name_function.py
    '''

    def test_first_last_name(self):
        '''
        能够处理像Janis Joplin这样的姓名吗? 
        '''
        formated_name = get_formatted_name('Janis', 'Joplin')
        self.assertEqual(formated_name, 'Janis Joplin')

    def test_first_middle_last_name(self):
        '''
        能够处理像Wen Qiu Ping这样的姓名吗? 
        '''
        formated_name = get_formatted_name('Wen', 'Ping', 'Qiu')
        self.assertEqual(formated_name, 'Wen Qiu Ping')


unittest.main()