def em_comum(numeros1, numeros2):
    numeros1 = set(numeros1)
    numeros2 = set(numeros2)

    comuns = numeros1.intersection(numeros2)

    if len(comuns) == 0:
        return False
    return True

nums1 = [1, 2, 3, 4]
nums2 = [4, 5, 6, 7]

print(em_comum(nums1, nums2))