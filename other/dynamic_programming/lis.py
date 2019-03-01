# Problem description: http://www.geeksforgeeks.org/longest-increasing-subsequence/

def lis(seq):
    if len(seq) == 1:
        return 1
    elif not seq[-1] < seq[-2]:
        return 1 + lis(seq[:-1])
    else:
        return lis(seq[:-1])





arr1 = [10 , 22 , 9 , 33 , 21 , 50 , 41 , 60]
print(lis(arr1))

arr2 = [3, 10, 2, 1, 20]
print(lis(arr2))

arr3 = [3, 2]
print(lis(arr3))

arr4 = [50, 3, 10, 7, 40, 80]
print(lis(arr4))