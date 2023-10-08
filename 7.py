with open('input.txt') as file:
    nums = file.read().split(' ')

try:
    nums = list(map(int, nums))
    res = str(nums[0] / nums[1] + nums[2])

    with open('output.txt', 'w+') as file:
        file.write(res)

except ValueError:
    print('The file contains more than just numbers!')
except ZeroDivisionError:
    print('Division by zero!')
