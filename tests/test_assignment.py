import unittest
from io import StringIO
from unittest.mock import patch
import assignment as ass

class TestControlStructures(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)  # Capture printed output
    def test_while_loop(self, mock_stdout):
        # Call the function
        ass.while_loop()

        # Define the expected output
        expected_output = "0\n2\n4\n6\n8\n10\n12\n14\n16\n"

        # Assert that the captured output matches the expected output
        self.assertEqual(mock_stdout.getvalue(), expected_output)
    
    @patch('sys.stdout', new_callable=StringIO)  # Capture printed output
    def test_for_loop_continue(self,mock_stdout):
        # Test if the for loop skips numbers divisible by 3
        ass.for_loop()
        expected_output = "1\n2\n4\n5\n7\n8\n10\n11\n13\n14\n"
        # Assert that the captured output matches the expected output
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_if_else(self):
        # Test if the if-else statement categorizes numbers correctly
        pass

    def test_nested_loops(self):
        # Test if the nested loops generate the correct multiplication table
        pass

if __name__ == "__main__":
    unittest.main()