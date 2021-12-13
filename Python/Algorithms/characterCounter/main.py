lettercount= {}

string = "FN1gZikt5yqxMnq4GdlqDTg0dFsMdZXZX6Qy6m6DKI91wt76PffA10fGPRBFtjMjvVdHr5ayOcD1DJs4Txz8EdeXtKKVeiUGARfZRtg6a0TeBj6tteA8LzNLITlxVAxzgOisBn9wYdzOTLIyilOxHZXD7gKbKHRkaLaaBnsVdbT4GJg1z2oYpfCQ7BXqSAQntawFIus3YABckHOjvLYrKh8KHqJlHezlNtyJhJ0s5hvAfvOwWkp0CbSGPyJwljMmj8QgzPtHJ1gipcc1V1wY7QAa2hjXiz1CzHmGMIY92S8znyp8zVkwi5xbrN3SNjWuhhMasOxExRZECHheX1DkgD19b5aL2PLTUkMj6nXHRnXyHBu8uu4OmzAQ7WIcYorXTR8zyoMuTWa3T5xnqtyPkiKTukM5uWRHcXzG69WKaBF4BDuROe1Gld14DQ3ZM5igmpKkFCfUEOfuhtGibOt"

for char in string:
    if char in lettercount:
        lettercount[char] += 1
    else:
        lettercount[char] = 1

print(lettercount)