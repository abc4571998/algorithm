from itertools import permutations

def solution(k, dungeons):
    max_count = 0
    dungeons_perm = list(permutations(dungeons, len(dungeons)))
    for dungeon_list in dungeons_perm:
        my_value = k
        count = 0
        for i in range(len(dungeon_list)):
            min_value, spend_value = dungeon_list[i]
            if my_value >= min_value:
                my_value -= spend_value
                count += 1
            else: break
        if max_count < count : max_count = count
    return max_count