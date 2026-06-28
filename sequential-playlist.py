'''
def findMinMinutes
Return the minimum time to reach m total viewings in a sequential playlist of n videos.
    Parameters:
            m: Total number of viewings to complete.
            firstWatch: Minutes to watch each video the first time.
            repeatWatch: Minutes to rewatch each video.
    Variables:
            minimumTime: To store the current lowest total time
            firstWatchSubset = To store a subset of firstWatch, from initial position to current loop iteration position (from position 0 until m).
            repeatWatchSubset = To store a subset of repeatWatch, from initial position to current loop iteration position (from position 0 until m).
            minRepeatWatchValue = To store the single minimun value of the repeatWatchSubset elements.
            minRepeatWatchTimes = To store the remaining times that we need to multiply the minRepeatWatchValue.
            cycleTime = To store algorithm logic, to validate possible new lowest time per cycle. 
    Returns:
            minimumTime: The minimum minutes required to reach m viewings
'''
def findMinMinutes(m, firstWatch, repeatWatch):
    minimumTime = float('inf')
    for i in range(m):
        firstWatchSubset = firstWatch[:i+1]
        repeatWatchSubset = repeatWatch[:i+1]
        minRepeatWatchValue = min(repeatWatchSubset)
        minRepeatWatchTimes = m - (i + 1)
        
        cycleTime = (sum(firstWatchSubset) + sum(repeatWatchSubset)) + (minRepeatWatchValue * minRepeatWatchTimes)
        
        if cycleTime < minimumTime:
            minimumTime = cycleTime
            
        print(f"Ciclo #{i}: firstWatchSubset: {firstWatchSubset}, repeatWatchSubset: {repeatWatchSubset}, minRepeatWatchValue: {minRepeatWatchValue}, minRepeatWatchTimes: {(m - (i + 1))}, cycleTime: {cycleTime}, minimumTime: {minimumTime}.")
            
    return minimumTime

if __name__ == '__main__':
    """m = input()
    n = input()
    firstWatch = [int(input()) for x in range(n)]
    n = input()
    repeatWatch = [int(input()) for x in range(n)]"""
    
    print(findMinMinutes(4, [1, 5, 9, 11], [2, 7, 10, 11]))
    print(findMinMinutes(5, [6, 8, 9], [4, 2, 10]))
    print(findMinMinutes(6, [2, 3, 7, 8, 4], [3, 6, 8, 7, 6]))