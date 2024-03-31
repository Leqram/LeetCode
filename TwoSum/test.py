nums = [2,7,11,15]
num_indices = {}
target = 22
for i, num in enumerate(nums):
    print(f'i: {i}')
    print(f'num: {num}')
    complement = target - num
    print(f'complement: {complement}')
    if complement in num_indices:
        print([num_indices[complement], i])
    num_indices[num] = i
    print(f'num_indices: {num_indices}')