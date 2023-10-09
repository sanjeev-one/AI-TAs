import tiktoken
from time import time

# Initialize tokenizer
tokenizer = tiktoken.get_encoding("cl100k_base")

# Sample text
text = "Your sample text goes here. Repeat this or use a larger text until you have at least 3000 tokens."

# List of token lengths
token_lengths = [3000, 6000, 9000, 12000, 15000]

# List to store times
times = []

for length in token_lengths:
    # Ensure we have at least 'length' tokens
    while len(list(tokenizer.encode(text))) < length:
        text += text

    # Start timing
    start_time = time()

    # Tokenize text
    tokens = list(tokenizer.encode(text))

    # End timing
    end_time = time()

    # Calculate elapsed time
    elapsed_time = end_time - start_time

    # Append elapsed time to times list
    times.append(elapsed_time)

# Print times for each token length
for i in range(len(token_lengths)):
    print(f"Time taken to tokenize to {token_lengths[i]} tokens: {times[i]} seconds")
