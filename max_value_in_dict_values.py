# Assignment: Find who tweeted the most

# You will be given a list of tweets
# Your program should find the user who has tweeted the most

# Note:
# If multiple users are having same number of tweets, then print all the users in alphabetical order of user names.
# Use Python 3
# Follow python coding style guide
# Only <filename>.py file should be uploaded. Do not upload <filename>.ipnb file

# Input format:
# Read the input from console.
# First line of input should be number of test cases
# Remaining lines of input should contain each test case input. 

# For each test case input:
# First line should contain number of tweets.
# Followed by N lines, each containing user name and tweet id separated by a space.

# Output format:
# Find the user with max number of tweets. Print user name and total number of tweets.


# Sample 1:
# Input 
# 1
# 4
# sachin tweet_id_1
# sehwag tweet_id_2
# sachin tweet_id_3
# sachin tweet_id_4

# Output
# sachin 3


# Sample 2:
# Input 
# 1
# 6
# sachin tweet_id_1
# sehwag tweet_id_2
# sachin tweet_id_3
# sehwag tweet_id_4
# kohli tweet_id_5
# kohli tweet_id_6

# Output
# kohli 2
# sachin 2
# sehwag 2



# Sample 3:
# Input 
# 2
# 4
# sachin tweet_id_1
# sehwag tweet_id_2
# sachin tweet_id_3
# sehwag tweet_id_4
# 5
# dhoni tweet_id_10
# dhoni tweet_id_11
# kohli tweet_id_12
# dhoni tweet_id_13
# dhoni tweet_id_14

# Output
# sachin 2
# sehwag 2
# dhoni 4

# Sample 4:
# Input
# 3
# 4
# sehwag tweet_id_2
# sehwag tweet_id_4
# sachin tweet_id_1
# sachin tweet_id_3
# 7
# sehwag tweet_id_10
# sehwag tweet_id_11
# kohli tweet_id_12
# sachin tweet_id_13
# sachin tweet_id_14
# sachin tweet_id_1
# sehwag tweet_id_4
# 5
# sachin tweet_id_2
# kohli tweet_id_4
# kohli tweet_id_1
# kohli tweet_id_3
# sachin tweet_id_5

# Output
# sachin 2
# sehwag 2
# sachin 3
# sehwag 3
# kohli 3




t = int(input())
while t>0:
    username = []
    id = []
    n = int(input())
    
    for i in range(n):
        string = input()
        y = string.split()
        username.append(y[0])
        id.append(y[1])
    # print(username, id)
    username.sort()
    my_dict = {i:username.count(i) for i in username}
    itemMaxValue = max(my_dict.items(), key=lambda x : x[1])
    # print('Max value in Dict: ', itemMaxValue[1])
    listOfKeys = list()
    for key, value in my_dict.items():
        if value == itemMaxValue[1]:
            listOfKeys.append(key)
            print(key, itemMaxValue[1])
    # for i in range(len(username)):
    #     x=username[i]
    #     count1 = username.count(x)
    #     print('{} has occurred {} times'.format(x, count1))

    t -= 1
