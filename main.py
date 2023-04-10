#!/usr/bin/env python3
import csv
import re

path ="./data/user_email.csv"
with open(path) as f:
  file = list(csv.reader(f))
  user_email_list = [data[1].strip() for data in file[1:]]
print(file[1:])
print(user_email_list)