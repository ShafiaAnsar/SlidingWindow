# Words Concatenation (hard)
def find_words_Concatenation(str, words):
    result_indices = []
    window_start , matches =0 ,0
    for chr in words:
        if chr not in words :
            words[chr] == 0
        words[chr] +=1
    for window_end in str:
        right_char = str[window_end]
        if right_char in words:
            words[right_char] -=1 
            