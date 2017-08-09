#!/usr/bin/env python3
import sys
from itertools import chain


def get_frames(file_):
    with open(file_) as f:
        frames_str = f.read().rstrip()

    frames = [frame.lstrip().rstrip().split(' ')
              for frame in frames_str.split('|')
              if frame]

    return frames


def get_throws(frames):
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
    total = 0
    LAST_FRAME = (len(throws)-1)//2

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

    frames = get_frames(sys.argv[1])
    throws = get_throws(frames)

    score = get_score(throws)
    print(score)
