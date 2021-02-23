import unittest
import os
import subprocess


class TestPatternSearchScript(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.standard_script_command = r'python search.py -p "\d{4}" -f "example" "example2"'

    def test_mutually_exclusive(self):
        """Verifies running the script with '--color' and '--machine' arguments returns exit code 2"""
        command = f"{self.standard_script_command}{' --machine --color cyan'}"
        return_code = os.system(command)
        self.assertEqual(2, return_code, "Program exited with the wrong exit code")

    def test_missing_color(self):
        """Verifies running the script with a non-existent color returns exit code 3"""
        command = f"{self.standard_script_command}{' --color FAKE_COLOR'}"
        return_code = os.system(command)
        self.assertEqual(3, return_code, "Program existed with the wrong exit code")

    def test_happy_flow(self):
        """Test happy flow. Script should find 1 pattern with 4 consecutive numbers"""
        process = subprocess.Popen(self.standard_script_command, stdout=subprocess.PIPE, shell=True)
        (out, err) = process.communicate()
        expected_substring = "Found match 5353 in file example, line no 1"
        self.assertTrue(expected_substring == out.decode('utf-8'), "Program didn't detect pattern.")

    def test_machine_output(self):
        """Verifies machine output format"""
        command = f"{self.standard_script_command}{' --machine'}"
        process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        (out, err) = process.communicate()
        expected_substring = "example:1:17:5353"
        self.assertTrue(expected_substring == out.decode('utf-8').rstrip(), "Program didn't detect pattern.")
