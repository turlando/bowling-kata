# The Bowling Kata

This repository contains the instructions for the Bowling Kata coding exercise, as made famous by [Robert "Uncle Bob" Martin](http://butunclebob.com/ArticleS.UncleBob.TheBowlingGameKata).

## The task

Write a program that calculates the total score of a bowling game for one player. A game of bowling is described as follows:

- the player needs to throw the bowling ball to knock down as many of the 10 pins as possible using multiple throws
- the throws are arranged in frames, where each frame is made of two throws and all the knocked down pins are reset after the second throw
- the game is made of 10 frames
- a strike is done when the player knocks down all the pins in one throw
- a spare is done when the player knocks down all the pins in two throws within the same frame
- in all frames except the last one, a strike concludes the frame
- in the last frame, a player can be allowed two or three throws as follows:
  - if the first two throws form a spare, he can throw a third time
  - if the first throw is a strike, he can throw a second time
  - if the second throw after a strike is itself a strike, he can throw a third time
- the score is calculated by summing all of the knocked down pins, plus the strike and spare bonuses
  - a spare gives an extra bonus to the frame which is equal to the number of pins knocked down in the throw right after the spare itself
  - a strike gives an extra bonus to the frame which is equal to the total number of pins knocked down in the two throws after the strike

### Example:

In the following game, each frame is written between pipe characters `|` while each throw is shown as follows:

- 0..10: the number of pins knocked down in that frame
- _    : throw skipped after a strike

```
frame #:    1     2     3     4      5     6     7     8      9      10
         | 1 4 | 4 5 | 6 4 | 5 5 | 10 _ | 0 1 | 7 3 | 6 4 | 10 _ | 2 8 6 |
score:      5     14    29    49    60     61    77    97    117     133
```

In the above example, we have spares in the frames 3, 4, 7, 8 and 10, and we have strikes in frames 5 and 9. For instance, the bonus for frame 3 is equal to 5,
the same as the first throw of frame 4, while the bonus for the spare in frame 10 (first two throws) is 6. The bonus for frame 5 is 1 as the next two throws only
knocked down one pin.

## Execution

Your program can read a file containing a single line with the game information formatted as in the example above and outputs the total game score. For instance,
if your program produces an executable called `bowling`, it should work as follows:

```
$ cat input.txt
| 1 4 | 4 5 | 6 4 | 5 5 | 10 _ | 0 1 | 7 3 | 6 4 | 10 _ | 2 8 6 |
$ bowling ./input.txt
133
```

## Remarks

- You can use any programming language or tool of your choice
- We will pay attention to your code structure and your tests, make sure to clean up your code
- Your code should include instructions on how to compile / package / run the program
