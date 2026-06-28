# Problem: findMinMinutes

A learner is given a sequential playlist of n videos. Implement a function
to calculate the minimum time required to complete a total of m viewings
while adhering to the platform's constraints.

## Rules

1. Sequential Viewing
   - Videos must be watched in playlist order.
   - To watch the video at index i for the first time, the learner must have
     already watched every video from index 0 to i-1 at least once.

2. Initial Full Viewing
   - The first viewing of video i costs firstWatch[i] + repeatWatch[i] minutes.

3. Subsequent Viewings
   - Every later viewing of video i costs only repeatWatch[i] minutes.
   - Any already-watched video can be rewatched at any time.

4. Minimum Total Watch Count
   - The learner must reach at least m total viewings across all videos.
   - Videos can be rewatched freely; they need not be watched equally.

Return the minimum time to reach m total viewings under these rules.

## Function Signature

long findMinMinutes(int m, int[] firstWatch, int[] repeatWatch)

## Parameters
- int   m            : total number of viewings to complete
- int[] firstWatch[n]: minutes to watch each video the first time
- int[] repeatWatch[n]: minutes to rewatch each video

## Returns
- long: the minimum minutes required to reach m viewings

## Constraints
- 1 <= n <= 10^5
- 1 <= m <= 10^9
- 1 <= firstWatch[i], repeatWatch[i] <= 10^9

## Input Format (custom testing)
- Line 1: m
- Line 2: n  (size of firstWatch)
- Next n lines: firstWatch[i]
- Next line: n  (size of repeatWatch)
- Next n lines: repeatWatch[i]

## Examples

Example 0
  n = 4, m = 4
  firstWatch  = [1, 5, 9, 11]
  repeatWatch = [2, 7, 10, 11]
  Strategy: first-watch video 0 (1+2=3), rewatch it 3x (2*3=6).
  Output: 9

Sample Case 1
  m = 5
  firstWatch  = [6, 8, 9]
  repeatWatch = [4, 2, 10]
  Strategy: first-watch video 0 (6+4=10), first-watch video 1 (8+2=10),
            rewatch video 1 three times (2*3=6).
  Output: 26

Sample Case 2
  m = 6
  firstWatch  = [2, 3, 7, 8, 4]
  repeatWatch = [3, 6, 8, 7, 6]
  Strategy: first-watch video 0 (2+3=5), rewatch it 5x (3*5=15).
  Output: 20
