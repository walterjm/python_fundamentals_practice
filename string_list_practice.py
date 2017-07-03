# words = "It's thanksgiving day. It's my birthday, too!"
# print words.find ("day")
# words.find("day")
# words = words.replace ("day","month")
# print words

# x = [2,54,-2,7,12,98]
# print "Min of x is:", min(x)
# print "Max of x ix:", max(x)

# x = ["hello", 2,54,-2,7,12,98,"world"]
# print x[0], x[len(x)-1]

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
listA = x[:len(x)/2]
listB = x[len (x)/2:]
print listA
print listB
listB.insert(0,listA)
print listB
