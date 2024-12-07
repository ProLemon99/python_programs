import time
import random

# Function to calculate Levenshtein Distance
def levenshtein_distance(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[n][m]

# List of sentences
sentences = [
    "The quick brown fox jumps over the lazy dog",
    "Python is a powerful programming language",
    "Artificial intelligence is the future",
    "Typing tests are a fun way to improve your skills",
    "Consistency is the key to success"
]

# Select a random sentence
sentence = random.choice(sentences)

# Game instructions
print("Type the following sentence as quickly and accurately as you can:")
print(sentence)

input("Press Enter when you're ready...")

# Record the start time
start_time = time.time()

# Player types the sentence
typed_sentence = input("\nStart typing: ")

# Record the end time
end_time = time.time()

# Calculate time taken
time_taken = end_time - start_time

# Calculate errors using Levenshtein Distance
errors = levenshtein_distance(sentence, typed_sentence)

# Display results
print("\nResults:")
print(f"Time taken: {time_taken:.2f} seconds")
if errors == 0:
    print("Perfect typing! No errors.")
else:
    print(f"Number of errors: {errors}")