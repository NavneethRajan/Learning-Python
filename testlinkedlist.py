import practicelib
import unittest

def build_predictable_list():
    link = practicelib.LinkedList()
    link.append(1)
    link.append(2)
    link.append(3)
    link.append(4)
    return link 

class TestLinkedlistMethods(unittest.TestCase):

    def test_length(self):
        # Todo: this is broken!!!!
        #       please fix, this is urgent in production - SEV 0
        self.assertEqual(len(build_predictable_list()), 4)

if __name__ == '__main__':
    unittest.main()