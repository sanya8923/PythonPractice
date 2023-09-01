def fake_bin(x):
    return ''.join(['1' if int(i) >= 5 else '0' for i in x])


print(fake_bin(["01011110001100111", "45385593107843568"]))