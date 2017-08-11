#!/usr/bin/env python3
import sys
import re


def get_throws(frames_str):
    """
    Return a list of throws given a string representing a complete game.

    Given scenario.
    >>> get_throws("| 1 4 | 4 5 | 6 4 | 5 5 | 10 _ "
    ...            "| 0 1 | 7 3 | 6 4 | 10 _ | 2 8 6 |")
    [1, 4, 4, 5, 6, 4, 5, 5, 10, 0, 0, 1, 7, 3, 6, 4, 10, 0, 2, 8, 6]

    Even number of throws.
    >>> get_throws("| 1 4 | 4 5 | 6 4 | 5 5 | 10 _ "
    ...            "| 0 1 | 7 3 | 6 4 | 10 _ | 2 8 |")
    [1, 4, 4, 5, 6, 4, 5, 5, 10, 0, 0, 1, 7, 3, 6, 4, 10, 0, 2, 8, 0]
    """

    r = re.compile('\d+|_')
    throws = r.findall(frames_str)

    throws_sane = [0 if throw == '_' else int(throw)
                   for throw in throws]

    # If there no third throw in the last frame then just make the list odd
    # adding a trailing zero
    if not len(throws_sane) % 2:
        throws_sane.append(0)

    return throws_sane


def get_score(throws):
    """
    Return the total score of a play given its throws.

    Given scenario.
    >>> get_score([1, 4, 4, 5, 6, 4, 5, 5, 10, 0,
    ...            0, 1, 7, 3, 6, 4, 10, 0, 2, 8, 6])
    133

    Single strike on 10th frame.
    >>> get_score([1, 4, 4, 5, 6, 4, 5, 5, 10, 0,
    ...            0, 1, 7, 3, 6, 4, 10, 0, 10, 8, 0])
    143

    Same as above, but without the trailing zero. An even list is not a valid
    input and will return a wrong result. This is why get_throws adds some
    extra padding.
    >>> get_score([1, 4, 4, 5, 6, 4, 5, 5, 10, 0,
    ...            0, 1, 7, 3, 6, 4, 10, 0, 10, 8])
    107

    Double strike on 10th frame.
    >>> get_score([1, 4, 4, 5, 6, 4, 5, 5, 10, 0,
    ...           0, 1, 7, 3, 6, 4, 10, 0, 10, 10, 4])
    151

    """
    LAST_FRAME = (len(throws)-1)//2
    total = 0

    for i in range(0, len(throws)-2, 2):
        # By default you just sum two throws from the frame
        score = throws[i] + throws[i+1]

        # Strike
        if throws[i] == 10:

            # Assuming that two strikes straight can be done only on LAST_FRAME
            if throws[i+1] == 10:
                score += throws[i+2]

            frame = (i+2)//2
            if frame != LAST_FRAME:
                score += throws[i+2] + throws[i+3]

        # Spare
        elif score == 10:
            score += throws[i+2]

        total += score

    return total


if __name__ == '__main__':
    if not len(sys.argv) > 1:
        print("usage: {} input.txt".format(sys.argv[0]))
        sys.exit(1)

    with open(sys.argv[1]) as f:
        frames_str = f.read().rstrip()

    throws = get_throws(frames_str)

    score = get_score(throws)
    print(score)
