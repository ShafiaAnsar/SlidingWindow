def fruit_basket(fruits):
    window_start = 0
    max_len = 0
    fruit_freq = {}
    for window_end in range(len(fruits)):
        right_fruit = fruits[window_end]
        if right_fruit not in fruit_freq:
            fruit_freq[right_fruit] = 0
        fruit_freq[right_fruit] +=1
        while len(fruit_freq) >2:
            left_fruit = fruits[window_start]
            fruit_freq[left_fruit] -=1
            if  fruit_freq[left_fruit]==0:
                del fruit_freq[left_fruit]
            window_start +=1
        max_len = max(max_len, window_end-window_start +1)
    return max_len

def main():
    print("max num of fruits:" + str(fruit_basket(["A","B","C","A","C"])))
main()