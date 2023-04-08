# RandStrGen
import string
import random

# Initial size of a string.
S = 5  # add a input function.

response = ''.join(random.choices(string.ascii_letters, k=S))

print(f'The generated random string: {str(response)}')
