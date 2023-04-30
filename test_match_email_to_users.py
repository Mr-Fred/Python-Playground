#!/usr/bin/env python3

import unittest
from match_email_to_users import find_email

class EmailsTest(unittest.TestCase):
  def test_base(self):
    testcase = [None, "Bree", "Campbell"]
    expected = "breee@abc.edu"
    self.assertEqual(find_email(testcase), expected)

  def test_one_name(self):
    testcase = [None, John]
    expected = "Missing parameters. Please provide your first and last name"
    self.assertEqual(find_email(testcase), expected)

  def test_name_noexist(self):
    testcase = [None, "Roy", "Cooper"]
    expected = "No email address found"
    self.asserEqual(find_email(testcase), expected)

if __name__ == '__main__':
  unittest.main()
  