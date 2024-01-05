#!/usr/bin/python3

def multiple_returns(sentence):
    # Get the length of the sentence
    length = len(sentence)

    if length == 0:
        # If the sentence is empty, return (None, None)
        return (None, None)

    # Return a tuple with the length of the sentence and its first character
    return (length, sentence[0])

if __name__ == "__main__":
    sentence = "At school, I learnt C!"

    # Call the multiple_returns function and unpack the result
    length, first = multiple_returns(sentence)

    # Print the results
    print("Length: {:d} - First character: {}".format(length, first))
