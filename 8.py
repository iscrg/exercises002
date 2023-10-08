with open('input.txt', 'r') as file:
    nums = file.read().splitlines()

while '100' in nums:
    del nums[nums.index('100')]

with open('input.txt', 'w+') as file:
    for num in nums:
        file.write(f'{num}\n')
