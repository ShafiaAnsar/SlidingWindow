def non_repeat_substr(str):
    window_start = 0
    max_len = 0
    char_index_map = {}
    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char in char_index_map:
            window_start = max(window_start, char_index_map[right_char]+1)
        char_index_map[right_char] = window_end
        max_len = max(max_len, window_end - window_start +1)
    return max_len

def main():
    print(" length of the longest substring:" + str(non_repeat_substr("aabccbb")))
    print(" length of the longest substring:" + str(non_repeat_substr("abbbb")))   
    print(" length of the longest substring:" + str(non_repeat_substr("abccde")))
main()