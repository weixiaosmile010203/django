import random
Teachers = ['qiudengkui','qiushaowen','xushiwen','qiujinbo','liliangliang','lixiaopeng','wangshuo','zhuzhewen']
Office = [[],[],[]]

for Name in Teachers:
        index = random.randint(0, 2)
        Office[index].append(Name)
print(Office)