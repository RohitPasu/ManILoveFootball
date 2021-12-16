import pandas as pd
header_row = 0

# Reading csv files we downloaded from https://www.pro-football-reference.com/
offense_stats = pd.read_csv('offense_stats.csv')
defense_stats = pd.read_csv('defense_stats.csv')
passing_stats = pd.read_csv('passing_stats.csv')
passdef_stats = pd.read_csv('passdef_stats.csv')
rushing_stats = pd.read_csv('rushing_stats.csv')
rushdef_stats = pd.read_csv('rushdef_stats.csv')

# Making the first column the header rather than data for all six dataframes
offense_stats.columns = offense_stats.iloc[header_row]
offense_stats = offense_stats.drop(header_row)

defense_stats.columns = defense_stats.iloc[header_row]
defense_stats = defense_stats.drop(header_row)

passing_stats.columns = passing_stats.iloc[header_row]
passing_stats = passing_stats.drop(header_row)

passdef_stats.columns = passdef_stats.iloc[header_row]
passdef_stats = passdef_stats.drop(header_row)

rushing_stats.columns = rushing_stats.iloc[header_row]
rushing_stats = rushing_stats.drop(header_row)

rushdef_stats.columns = rushdef_stats.iloc[header_row]
rushdef_stats = rushdef_stats.drop(header_row)