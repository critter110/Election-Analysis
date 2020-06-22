# The data that we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote


# Add our Dependencies
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize a total vote counter
total_votes = 0

# Creating list of candidate names
candidate_options = []

#Create empty dictionary. Key = candidate name, value = votes
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Create a blank list of counties
countiesList = []

# Create empty dictionary where county is key and votes in that county are value
countiesDict = {}

# Create empty string for largest county turnout
largestCounty = ""
largestCountyCount = 0
largestCountyPercentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:

        # increment total votes by 1
        total_votes += 1

        # Counting candidate votes
        candidate_name = row[2]
        # if the candidate does not match an existing candidate...
        if candidate_name not in candidate_options:
            # Add the cadidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        # Increment by 1 for every vote
        candidate_votes[candidate_name] += 1

        # Counting county votes
        county_name = row[1]
        # if county does not match an existing county ...
        if county_name not in countiesList:
            # Add the county to the county list
            countiesList.append(county_name)

            # Begin tracking votes from that county
            countiesDict[county_name] = 0

        # Increment by 1 for every vote from that county
        countiesDict[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # print county info header
    countyHeader = "County Votes:\n"
    print(countyHeader)
    # Write county info header to txt file
    txt_file.write(countyHeader)

    # loop through county options
    for county in countiesDict:
        # retreive vote count of a county
        countyVotes = countiesDict[county]
        # calculate county percentage of votes
        countyVotePercentage = float(countyVotes) / float(total_votes) * 100
        # print the county name and percentage of votes
        county_results = (f"{county}: {countyVotePercentage:.1f}% ({countyVotes:,})\n")
        print(county_results)
        # Save county results to text file
        txt_file.write(county_results)

        # Determine largest county
        if (countyVotes > largestCountyCount) and (countyVotePercentage > largestCountyPercentage):
            largestCountyCount = countyVotes
            largestCountyPercentage = countyVotePercentage
            largestCounty = county

    largestCountySummary = (
        f"-------------------------\n"
        f"Largest County Turnout: {largestCounty}\n"
        f"-------------------------\n"
    )
    print(largestCountySummary)
    txt_file.write(largestCountySummary)

        #loop through candidate options
    for candidate in candidate_votes:
        # retreive vote count of a candidate
        votes = candidate_votes[candidate]
        # calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print the candidate name and percentage of votes
        
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate  
        
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)

