import glob
# path = '../leetcode-syncs/*'
# counter = 0
# hashset = set()
# ROMANS = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
# for filename in glob.glob(os.path.join(path, 'NOTES.md')):
#    with open(os.path.join(os.getcwd(), filename), 'r') as f:  # open in readonly mode
#       for line in f:
#         # print(line.rstrip())
#         if line != '\u200b':
#             myString = line.replace("* ", "").replace("\n", "")
#             myString = myString[:1].upper() + myString[1:]
#             path = "./leetcode-parser/"+myString 
#             lst = (filename.split("/")[-2]).split("-")
#             lst[0] = int(lst[0])
#             # print(filename)
#             final_dir = str(lst[0]) + ". " + " ".join([i.upper() if i.upper()
#                                                        in ROMANS else i.capitalize() for i in lst[1:]])
#             destination = path+"/"+final_dir+"/"
#             source = filename.rsplit('/', 1)[0]+"/"
#             print(source)
#             print(destination)
#             hashset.add(myString)
#             if not os.path.exists(path):
#                 os.makedirs(path)
            
# # hashset = {'Parenthesis'}
# # for i in hashset:
# #     path = "./leetcode-parser/"+myString
# #     if not os.path.exists(path):
# #         os.makedirs(path)
# print(hashset)

