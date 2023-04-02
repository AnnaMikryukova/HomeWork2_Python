''' На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть/
5 -> 1 0 1 1 0
2
'''
n = int(input('Введите количество монет: '))
heads = 0
tails = 0

for i in range(n):
	x = int(input())
	if x == 0:
		heads += 1
	else:
		tails += 1

if heads > tails:
	print(tails)
else:
	print(heads)
