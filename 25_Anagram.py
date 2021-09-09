"""
Anagrams
	An anagram is a word, phrase, or name formed by rearranging the letters of phrase, or name.
	Write a function to check if two given strings are anagrams or not. Return “Yes” anagrams, otherwise return “no”.
	Input Specification:
	input1: the first string
	input2: the second string
	Output Specification:
	Return “yes” if they are anagrams, otherwise return “no”.
	Example 1:
	input1: build
	input2: dubli
	Output: yes
	Explanation:
	First string can be rearranged to form the second string other.
	Example 2:
	input1: beast
	input2: yeast
	Output: no

"""


NO_OF_CHARS = 256

def areAnagram(str1, str2):
    count1 = [0] * NO_OF_CHARS
    count2 = [0] * NO_OF_CHARS

    for i in str1:
        count1[ord(i)] += 1

    for i in str2:
        count2[ord(i)] += 1

    if len(str1) != len(str2):
        return 0

    for i in range(NO_OF_CHARS):
        if count1[i] != count2[i]:
            return 0
    return 1

str1 = input()
str2 = input()
if areAnagram(str1, str2):
    print("yes")
else:
    print("no")