def find_substr(str , pattern):
    window_start , matches , substr_start = 0,0,0
    min_len = len(str) +1
    char_frequency ={}
    for chr in pattern:
        if chr not in char_frequency:
            char_frequency[chr] = 0
        char_frequency[chr] += 1
    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] >= 0:
                matches += 1
        while matches == len(pattern):
            if min_len > window_end - window_start +1:
                min_len = window_end - window_start +1
                substr_start = window_start
            left_char = str[window_start]
            window_start +=1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matches -=1
                char_frequency[left_char] +=1
    if min_len > len(str):
         return ""
    return str[ substr_start : substr_start + min_len]
def main():
    print(" min_len of substr is  " + str(find_substr("aabdec", "abc")))
    print(" min_len of substr is " + str(find_substr("abdabca", "dc")))

main()
                

