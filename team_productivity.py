#!/usr/bin/env python3

import csv

data_list = []
with open('data_file_team_productivity.csv', newline='') as team_data:
  data = csv.DictReader(team_data)
  for column in data:
    data_list.append(column)

#print(data_list[0])
first_row = data_list[0]
if first_row['Rep'] == 'Rep A':
  print(first_row['Rep'])