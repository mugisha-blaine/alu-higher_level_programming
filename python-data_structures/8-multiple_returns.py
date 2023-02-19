#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if sentence == "":
        sentence[0] = None
    return (length, sentence[0])
