def is_valid_walk(walk: list) -> bool:
    if (walk.count('n') == walk.count('s') and
        walk.count('e') == walk.count('w') and
        len(walk) == 10
    ):
        return True
    else:
        return False


print(is_valid_walk(['n', 'w', 'e', 'w', 'n', 's', 'e', 's', 'e', 'w']))
