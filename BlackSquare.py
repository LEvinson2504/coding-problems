name = input()

# # stack pointer
# ptr = "a"
# rotations = 0
# uni_ptr = ord(ptr)
# # check if to go clockwise or anti-clockwise
# # for chr in name:
#     # unicode valuees
#     uni_chr = ord(chr)
#     # difference between chr and ptr
#     diff = abs(uni_chr - uni_ptr)
#     # check which way to go
#     if diff < 13:
#         while(uni_ptr != uni_chr):
#             uni_ptr += 1
#             rotations += 1
#     else:
#         while(uni_ptr != uni_chr):
#             # edge case to handle going anti-clockwise a to z

#             if (uni_ptr <= 97):
#                 uni_ptr = 122
#                 rotations += 1
#                 continue

#             uni_ptr -= 1
#             rotations += 1

rotations = 0


for i in range(1, len(name)):
    rotations += min(abs(ord(name[i]) - ord(name[i-1])),
                     26 - abs(ord(name[i]) - ord(name[i-1])))

print(rotations)


# count the rotations required
