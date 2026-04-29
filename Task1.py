#import math
# a = 10
# b = 20
# lcm = abs(a * b) // math.gcd(a, b)
# print(lcm)


# import math
# a = 10
# b = 20
# hcf = math.gcd(a, b)
# print(hcf)


# r = [1,2,3,4,5]
# result = []
# s = 0
# for i in r:
#     s += i
#     result.append(s)
# print(result)


# k1 = [1,2,5]
# k2 = [7,6,3]
# result = [(x, y) for x, y in zip(k1, k2) if x != y]
# print(result)


# k = "a3"
# char = k[0]
# num = int(k[1])
# print(char * num)


# m = "ab2"
# chars = m[:-1]
# num = int(m[-1])
# print(chars * num)

# k = "a[3]"
# char = k[0]
# num = int(k[2])
# print(char * num)


# n = "ac[2]"
# text = n[:2]
# num = int(n[3])
# print(text * num)


# a = "Hello"
# b = "World"
# print("{}{}".format(a, b))



# n = int(input("Enter n: "))
# count = 0
# num = 2
# while count < n:
#     is_prime = True
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num, end=" ")
#         count += 1
#     num += 1