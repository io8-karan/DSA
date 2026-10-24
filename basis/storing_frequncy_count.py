# # simple and  normal method 
# freq_count={}
# num=[1,5,55,45,2,1,45,98,285,1,44,6,6,45,2,1,4,2,34,43,4,23,5,6,65,4,64,54,4,5]
# for i in range(0,len(num)):
#     if num[i] in freq_count:
#         freq_count[num[i]] += 1
#     else:
#         freq_count[num[i]] = 1
# print(freq_count)

# using get 
freq_count={}
num=[1,5,55,45,2,1,45,98,285,1,44,6,6,45,2,1,4,2,34,43,4,23,5,6,65,4,64,54,4,5]
for i in range(0,len(num)):
    freq_count[num[i]]=freq_count.get(num[i],0)+1
print(freq_count)