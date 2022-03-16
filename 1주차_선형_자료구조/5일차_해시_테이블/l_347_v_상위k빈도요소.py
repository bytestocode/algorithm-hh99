from collections import Counter

def top_k_frequent(nums, k):
    nums_count_dict = Counter(nums)
    res = []

    key_list = list(nums_count_dict.keys())
    val_list = list(nums_count_dict.values())
    sorted_list = sorted(val_list)

    for _ in range(k):
        val = sorted_list.pop()
        idx = val_list.index(val)
        val_list[idx] = 'c'
        key = key_list[idx]
        res.append(key)

        print(f'val: {val}, idx: {idx}, key: {key}')

    return res

print(top_k_frequent([1, 2], 2))