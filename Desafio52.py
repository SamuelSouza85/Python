n = int(input('Digite um número: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[36m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[m0 O número {} foi divisivél {} vezes'.format(n, tot))
if tot == 2:
    print("Ele é primo")
else:
    print("Ele não é primo")