import random
kuji = random.randint(1, 100)
kuji = int(kuji)
if kuji == 1:
    print('大凶')
if kuji > 1 and kuji < 12:
    print('凶')
if kuji > 11 and kuji < 31:
    print('末吉')
if kuji > 30 and kuji < 55:
    print('吉')
if kuji > 54 and kuji < 68:
    print('小吉')
if kuji > 67 and kuji < 78:
    print('中吉')
if kuji > 77 and kuji <100:
    print('大吉')

# a1 = 0#大凶の本数
# for i in range(2, 12):#凶の本数
#     exec(f'a{i} = 1')
# for i in range(12, 31):#末吉の本数
#     exec(f'a{i} = 2')
# for i in range(31, 55):#吉の本数
#     exec(f'a{i} = 3')
# for i in range(55, 68):#小吉の本数
#     exec(f'a{i} = 4')
# for i in range(68, 78):#中吉の本数
#     exec(f'a{i} = 5')
# for i in range(78, 101):#大吉の本数
#     exec(f'a{i} = 6')
# i = random.randint(1,100)
# exec(f'print(a{i})')