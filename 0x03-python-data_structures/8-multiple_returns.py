#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        return (None, None)
    return (length, sentence[0])
if __name__ == "__main__":
    sentence = "At school, I learnt C!"
    length, first = multiple_returns(sentence)
    print("Length: {:d} - First character: {}".format(length, first))
