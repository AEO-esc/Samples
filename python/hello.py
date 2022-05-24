# initial checks
import time

print("Hello World");
time.sleep(5);

peak = [6,7,4,3,2,1,4,5]

for x in peak:
    print(x)
time.sleep(5)

n = len(peak)


# Find the peak in O(n) time complexity
def findPeak(arr, n) :
    # check if the first or last element is the peak element
    if(n == 1):
        return 0
    if (arr[0] >= arr[1]):
        return 0
    if(arr[n -1] >= arr[n -2]):
        return n - 1
    # loop thru list and check other elements
    for i in range(1, n - 1):
        if(arr[i] >= arr[i-1] and arr[i] >= arr[i+1]):
            return i

print("Index of peak point is", findPeak(peak,n))
time.sleep(3)