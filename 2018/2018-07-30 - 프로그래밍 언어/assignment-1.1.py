import random, time

pnu = []
count = 0
while True:
    nu = random.randint(1, 45)
    if nu not in pnu:
        print(nu)
        pnu.append(nu)
        count += 1
    time.sleep(1)
    
    if count == 6:
        break