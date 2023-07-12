import math
def smallest_arr(s,arr):
    min_len = math.inf
    window_start=0
    window_sum=0
    for window_end in range(0,len(arr)):
        window_sum += arr[window_end]
        while window_sum >= s:
            min_len = min(min_len, window_end - window_start+1)
            window_sum -=arr[window_start]
            window_start +=1
    if min_len == math.inf:
        return 0
    return min_len

def main():
    print("smallest   of subarrays of sum  s:" + str(smallest_arr(7, [2,1,5,2,3,2])) )
    print("smallest   of subarrays of sum  s:" + str(smallest_arr(7, [2,1,5,2,8])))
    print("smallest   of subarrays of sum  s:" + str(smallest_arr(8, [3,4,1,1,6])))
main()