# def longest_substring_with_1s(arr,k):
#     window_start = 0
#     max_len =0
#     maxOnesCount = 0
#     for window_end in range(len(arr)):
#         if arr[ window_end] == 1:
#             maxOnesCount+=1
#         if(window_end-window_start+1 - maxOnesCount)>k:
#             if arr[window_start] == 1:
#                 maxOnesCount -=1
#             window_start+=1
#         max_len = max(max_len, window_end-window_start+1)
#     return max_len
# def main():
#     print(" length of the longest substring:" + str(longest_substring_with_1s([0,1,1,0,0,0,1,1,0,1,1], 2)))
# main()
#another approach
def longest_substring_with_1s(arr,k):
    window_start =0
    window_end =0
    max_len =0
    noOfZero = 0
    while(window_end < len(arr)):
        if(arr[window_end] == 0):
            noOfZero +=1
        if (noOfZero > k):
            if(arr[window_start] ==0):
                noOfZero-=1
            window_start +=1
        max_len = max(window_end-window_start+1, max_len)
        window_end +=1
    return max_len

def main():
   print(" length of the longest substring:" + str(longest_substring_with_1s([0,1,1,0,0,0,1,1,0,1,1], 2)))
main()