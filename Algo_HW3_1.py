# 1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны любому из чисел в диапазоне от 2 до 9.

def how_many(strt_rng, end_rng, strt_span, end_span):
    rng_how_many = {}
    for i in range(strt_span, end_span+1):
        for j in range(strt_rng, end_rng):
            if j * i <= end_rng - i:
                continue
            else:
                rng_how_many[i] = j
                break
    return rng_how_many


print(how_many(2, 99, 2, 9))