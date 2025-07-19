n = input()
current_chairs = 0
max_chairs = 0

for i in n:
    if i == 'C' or i == 'U':
        current_chairs += 1
        max_chairs = max(max_chairs, current_chairs)
    elif i == 'R' or i == 'L':
        current_chairs -= 1

print(max_chairs)
