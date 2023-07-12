def prm_in_str(str , patt):
    matches = 0
    window_start = 0
    char_frequency = {}
    for chr in patt:
        if chr not in char_frequency:
            char_frequency[chr] = 0
        char_frequency[chr] +=1


    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char in char_frequency:
            char_frequency[right_char] -=1
            if char_frequency[right_char] ==0:
                matches +=1
        if matches == len(char_frequency):
            return True
        if window_end >= len(patt) -1:
            left_char = str[window_start]
            window_start +=1
            if left_char in char_frequency:
                if char_frequency[left_char] ==0:
                    matches -=1
                char_frequency[left_char] +=1
    return False 
def main():
    print(" permutation occur " + str(prm_in_str("oidbcaf", "abc")))
    print(" permutation occur " + str(prm_in_str("odicf", "dc")))

main()



















# neet code
# def checkInclusion(s1,s2)-> bool:
#     if len(s1) > len(s2) : return False
    
#     s1count , s2count = [0] * 26, [0] * 26
#     for i in range(len(s1)):
#         s1count[ord(s1[i]) - ord("a")] +=1
#         s2count[ord(s2[i])- ord("a")] +=1
#     matches = 0
#     for i in range(26):
#         matches +=(1 if s1count[i] == s2count[i] else  0 )
#     left = 0
#     for right in range(len(s1), len(s2)):
#         if  matches == 26 : return True
#         index = ord(s2[right]) - ord("a")
#         s2count[index] +=1
#         if s1count[index] == s2count[index]:
#             matches +=1
#         elif  s1count[index] + 1 == s2count[index]:
#               matches -=1
#         # left
#         index = ord(s2[left]) - ord("a")
#         s2count[index] -=1
#         if s1count[index] == s2count[index]:
#             matches +=1
#         elif  s1count[index] - 1 == s2count[index]:
#               matches -=1
#         left +=1
#         return matches == 26

# def main():
#     print(" permutation occur " + str(checkInclusion("abc", "oidbcaf")))
# main()