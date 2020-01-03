def multiplesOf3and5(number):
    total = 0
    for i in range(number):
        if i % 3 == 0:
            total += i
        elif i % 5 == 0:
            total += i
    return total

print('multiplesOf3and5(1000) should return 233168')
print(multiplesOf3and5(1000))

print('multiplesOf3and5(49) should return 543')
print(multiplesOf3and5(49))

print('multiplesOf3and5(19564) should return 89301183')
print(multiplesOf3and5(19564))

print('multiplesOf3and5(8456) should return 16687353')
print(multiplesOf3and5(8456))
