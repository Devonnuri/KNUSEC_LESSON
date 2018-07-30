a = [str(i) for i in range(1, 45)]
__import__('random').shuffle(a)
print('\n'.join(a[:6]))
