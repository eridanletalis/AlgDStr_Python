"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9
"""

multiplicity = [0, 0, 0, 0, 0, 0, 0, 0]
for i in range(2, 100):
    for j in range(2, 10):
        multiplicity[j - 2] += 1 if i % j == 0 else 0

print(multiplicity)
