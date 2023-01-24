import pandas as pd
import csv

election_df = pd.read_csv("Resources/election_data.csv", encoding= "utf-8")
#print(election_df)

#The total number of votes cast
total_votes = len(election_df["Ballot ID"].unique())
print(total_votes)

#A complete list of candidates who received votes
candidate_list = len(election_df["Candidate"].unique())
#print(candidate_list)
candidate_group = election_df.groupby(["Candidate"])
group_totals = candidate_group.count()

#The percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote
