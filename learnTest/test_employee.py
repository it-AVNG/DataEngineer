import unittest
from employees import employee

class TestEmployee(unittest.TestCase):
    
    def setUp(self):
       self.emp_1 = employee('Corey', 'Schafler',50000)
       self.emp_2 = employee('Sue', 'Smith', 60000)
    
    def tearDown(self):
        del self.emp_1
        del self.emp_2
        pass
    
    def test_email(self):

        self.assertEqual(self.emp_1.email, 'Corey.Schafler@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

        self.emp_1.first ='John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Schafler@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

    def test_fullName(self):

        self.assertEqual(self.emp_1.fullname, 'Schafler,Corey')
        self.assertEqual(self.emp_2.fullname, 'Smith,Sue')

        self.emp_1.first ='John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'Schafler,John')
        self.assertEqual(self.emp_2.fullname, 'Smith,Jane')

if __name__ == '__main__':
  unittest.main()