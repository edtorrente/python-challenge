# PYTHON HOMEWORK - Py Me Up, Charlie

## Background: 

Apply the concepts learned about python programming in two projects,
    1. PyBank
    2. PyPoll

### PyBank:

Create a Python script for analyzing the financial records of a "dummy" company. You will give a set of financial data called 
[budget_data.csv](PyBank/Resources/budget.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`.

Deliverables to include:
* The total number of months included in the dataset
* The net total amount of "Profit/Losses" over the entire period
* Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
* The greatest increase in profits (date and amount) over the entire period
* The greatest decrease in profits (date and amount) over the entire period

```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```

### PyPoll:

In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election.csv). 
The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. 

Deliverables to include:
* The total number of votes cast
* A complete list of candidates who received votes
* The percentage of votes each candidate won
* The total number of votes each candidate won
* The winner of the election based on popular vote.

```text
  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  ```
