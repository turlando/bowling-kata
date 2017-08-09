#!/usr/bin/env python3
import sys
from itertools import chain


def get_frames(frames_str):
    """
    Return a list of frames given a string.

    Given scenario.
    >>> get_frames("| 1 4 | 4 5 | 6 4 | 5 5 | 10 _ "
    ...            "| 0 1 | 7 3 | 6 4 | 10 _ | 2 8 6 |")
    [['1', '4'], ['4', '5'], ['6', '4'], ['5', '5'], ['10', '_'], ['0', '1'], \
['7', '3'], ['6', '4'], ['10', '_'], ['2', '8', '6']]
    """
    return [frame.lstrip().rstrip().split(' ')
            for frame in frames_str.split('|')
            if frame]


def get_throws(frames):
    """
    Return a list of throws given a list of frames.

    Given scenario.
    >>> get_throws([['1', '4'], ['4', '5'], ['6', '4'], ['5', '5'], ['10', '_'],
    ...             ['0', '1'], ['7', '3'], ['6', '4'], ['10', '_'],
    ...             ['2', '8', '6']])
    [1, 4, 4, 5, 6, 4, 5, 5, 10, 0, 0, 1, 7, 3, 6, 4, 10, 0, 2, 8, 6]

    Even number of throws.
    >>> get_throws([['1', '4'], ['4', '5'], ['6', '4'], ['5', '5'], ['10', '_'],
    ...             ['0', '1'], ['7', '3'], ['6', '4'], ['10', '_'],
    ...             ['10', '8']])
    [1, 4, 4, 5, 6, 4, 5, 5, 10, 0, 0, 1, 7, 3, 6, 4, 10, 0, 10, 8, 0]

    """
    throws = list(chain.from_iterable(frames))

    for i, throw in enumerate(throws):
        try:
            throws[i] = int(throw)

        # Is it '_'?
        except ValueError:
            throws[i] = 0

    # If there no third throw in the last frame then just make the list odd
    # adding a trailing zero
    if not len(throws) % 2:
        throws.append(0)

    return throws


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
        frame = (i+2)//2

        # By default you just sum two throws from the frame
        score = throws[i] + throws[i+1]

        # Strike
        if throws[i] == 10:

            # Assuming that two strikes straight can be done only on LAST_FRAME
            if throws[i+1] == 10:
                score += throws[i+2]

            if frame != LAST_FRAME:
                score += throws[i+2] + throws[i+3]

            total += score
            continue

        # Spare
        if score == 10:
            score += throws[i+2]
            total += score
            continue

        total += score

    return total


if __name__ == '__main__':
    if not len(sys.argv) > 1:
        print("usage: {} input.txt".format(sys.argv[0]))
        sys.exit(1)

    with open(sys.argv[1]) as f:
        frames_str = f.read().rstrip()

    frames = get_frames(frames_str)
    throws = get_throws(frames)

    score = get_score(throws)
    print(score)
