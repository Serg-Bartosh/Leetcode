# 28. Find the Index of the First Occurrence in a String
# Given two strings needle and haystack, return the index of the first
# occurrence of needle in haystack, or -1 if needle is not part of haystack.

def strStr(haystack: str, needle: str) -> int:
    return haystack.find(needle)


# test №1
haystack = "sadbutsad"
needle = "sad"
print(strStr(haystack, needle))
# test №2
haystack = "leetcode"
needle = "leeto"
print(strStr(haystack, needle))
