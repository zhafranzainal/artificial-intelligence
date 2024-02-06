score = 90

print()
if score >= 90:
    print('A')
elif score >= 70:
    print('B')
else:
    print('C')

print()
print('A') if score >= 90 else print('B') if score >= 70 else print('C')
