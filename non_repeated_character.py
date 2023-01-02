str1 = "EEDYOODA"
order = []
counts = {}

for i in str1:
    if i in counts:
        counts[i] += 1
    else:
        counts[i] = 1
        order.append(i)
for j in order:
    if counts[j] == 1:
        break
print("first non-repeated character : ",j)
