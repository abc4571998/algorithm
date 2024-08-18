def solution(nums):
    # 골라야 하는 포켓몬 수
    pick_pokemon = len(nums) // 2
    # 포켓몬 종류
    pokemon_type = set(nums)
    return min(pick_pokemon, len(pokemon_type))
