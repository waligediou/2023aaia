a = int(input())

ss = a%60
mm = a//60%60
hh = a//60//60

print(f'{hh}:{mm}:{ss}', end='')