def count_strings(book):
    counts = {}
    for char in book:
        lower = char.lower()
        if(lower in counts):
            counts[lower] += 1
        else:
            counts[lower] = 1
    return(counts)

def print_results(path, total, dict):
    print(f"--- Begin report of {path} ---")
    print(f"{total} words found in the document")
    for char in dict:
            print(f"the '{char}' character was found {dict[char]} times")
    print("--- End report ---")



def main():

    path = "books/frankenstein.txt"

    with open(path) as f:
        file_contents = f.read()
        total = len(file_contents.split())
        char_count = count_strings(file_contents)
        print_results(path,total,char_count)
        
# p: 6121
# r: 20818
# o: 25225
# j: 504
# e: 46043
# c: 9243
# t: 30365
#  : 74144
# g: 5974
# u: 10407
# n: 24367
# b: 5026
# ': 229
# s: 21155
# f: 8731
# a: 26743
# k: 1755
# i: 24613
# ,: 5097
# y: 7914
# m: 10604
# w: 7638
# l: 12739
# (: 39
# d: 16863
# ): 39
# h: 19725

# : 7652
# v: 3833
# .: 3124
# -: 445
# :: 68
# 1: 92
# 7: 23
# 2: 24
# 0: 21
# 8: 20
# [: 4
# #: 1
# 4: 17
# ]: 4
# *: 28
# z: 243
# ?: 220
# ;: 970
# x: 677
# q: 324
# !: 239
# ": 796
# 3: 18
# 5: 16
# 9: 13
# 6: 10
# _: 2
# /: 24
# %: 1
# @: 2
# $: 2
main()