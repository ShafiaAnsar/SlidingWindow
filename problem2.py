def find_str_anagram(str , patt):
    matches = 0
    window_start = 0
    char_frequency = {}
    for chr in patt:
        if chr not in char_frequency:
            char_frequency[chr] = 0
        char_frequency[chr] +=1
    result_indices = []

    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char in char_frequency:
            char_frequency[right_char] -=1
            if char_frequency[right_char] ==0:
                matches +=1
        if matches == len(char_frequency):
            result_indices.append(window_start)
        if window_end >= len(patt) -1:
            left_char = str[window_start]
            window_start +=1
            if left_char in char_frequency:
                if char_frequency[left_char] ==0:
                    matches -=1
                char_frequency[left_char] +=1
    return result_indices 
def main():
    print(" permutation occur " + str(find_str_anagram("ppqp", "pq")))
    print(" permutation occur " + str(find_str_anagram("abbcabc", "abc")))

main()
