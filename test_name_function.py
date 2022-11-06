import unittest
from name_function import get_formatted_name


# Unit Tests and Test Cases, unittest, test case, full coverage

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

# Adding New Tests
    def test_first_middle_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin', 'middle')
        self.assertEqual(formatted_name, 'Janis Middle Joplin')

# unittest.main()
