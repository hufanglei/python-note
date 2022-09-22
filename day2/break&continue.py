for i in range(1,6):
    print(f"------{i}层--------")
    if i==3:
        continue
    for j in range(1,9):
        if i==4 and j==4:
            print("遇到鬼屋了，over...")
            break
        print(f"L{i}-{i}0{j}室")