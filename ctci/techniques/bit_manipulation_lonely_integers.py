from collections import Counter


sample_inputs = [[1, 1, 2],
                 [0, 0, 1, 2, 1]]


for i in sample_inputs:
    print([k for k,v in Counter(i).items() if v==1][0])

for i in sample_inputs:
    result = 0

    for n in i:
        result = result ^ n

    print(result)