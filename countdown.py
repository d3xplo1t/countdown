import time 

for i in range(120,0,-1):
    print(f"{i}", end="\r", flush=True)
    time.sleep(1)
