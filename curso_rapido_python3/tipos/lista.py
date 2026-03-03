nums = [1, 2, 3]
print(type(nums))

nums.append(3)
print(len(nums))
nums.append(4)
nums.append(5)
print(len(nums))
print(nums)

# Inserindo na posição 4 do array.
nums[3] = 100
print(nums)

# Realizando o método insert
nums.insert(0, -200)
nums.insert(2, 20)
print(nums)

# Alterando valor na posição 6 do array nums
nums[6] = 500
print(nums[6])
print(nums[-1])
print('Tamanho: ', len(nums))
print(nums)
print(nums[-2])
print(nums[-5])
print(nums[0])