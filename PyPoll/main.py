# Import the csv module
import csv

# Initialize variables to store the results
total_votes = 0 # The total number of votes cast
candidates = {} # A dictionary of candidates and their votes
winner = "" # The winner of the election based on popular vote
max_votes = 0 # The maximum number of votes among the candidates

# Open the csv file
with open("PyPoll/Resources/election_data.csv") as csvfile:
    # Create a csv reader object
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    next(csvreader)

    # Loop through each row in the file
    for row in csvreader:
        # Increment the total votes by 1
        total_votes += 1

        # Get the candidate name from the third column
        candidate = row[2]

        # If the candidate is not in the dictionary, add it with a value of 1
        if candidate not in candidates:
            candidates[candidate] = 1
        # Otherwise, increment the value by 1
        else:
            candidates[candidate] += 1

# Print a header for the election results
print("Election Results")


# Print the total votes
print(f"Total Votes: {total_votes}")

# Loop through the candidates dictionary
for candidate, votes in candidates.items():
    # Calculate the percentage of votes for each candidate
    percentage = (votes / total_votes) * 100

    # Print the candidate name, percentage, and votes
    print(f"{candidate}: {percentage:.3f}% ({votes})")

    # If the current candidate has more votes than the max votes, update the winner and max votes
    if votes > max_votes:
        winner = candidate
        max_votes = votes

# Print the winner of the election
print(f"Winner: {winner}")


# Open a new file called analysis with write mode
with open("PyPoll/analysis/analysis.txt", "w") as outfile:
    # Print a header for the election results to the file
    print("Election Results", file=outfile)
    

    # Print the total votes to the file
    print(f"Total Votes: {total_votes}", file=outfile)

    # Loop through the candidates dictionary
    for candidate, votes in candidates.items():
        # Calculate the percentage of votes for each candidate
        percentage = (votes / total_votes) * 100

        # Print the candidate name, percentage, and votes to the file
        print(f"{candidate}: {percentage:.3f}% ({votes})", file=outfile)

        # If the current candidate has more votes than the max votes, update the winner and max votes
        if votes > max_votes:
            winner = candidate
            max_votes = votes

    # Print the winner of the election to the file
    print(f"Winner: {winner}", file=outfile)

   