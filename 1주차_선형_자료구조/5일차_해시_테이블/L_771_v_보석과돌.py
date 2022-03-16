from collections import Counter

def numJewelsInStones(jewels, stones):
    # jewels_list = list(jewels)
    stone_dict = Counter(stones)
    jewels_count = 0

    # for i in range(len(jewels_list)):
    #     jewel = jewels_list[i]
    #     jewels_count += stone_dict[jewel]
    for jewel in jewels:
        jewels_count += stone_dict[jewel]

    return jewels_count

print(numJewelsInStones('aA', 'aAAbbbb'))