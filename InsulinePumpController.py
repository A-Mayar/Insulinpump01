insulin_level = 10
insulinpump = 5
counter = 4
while insulin_level>=3:
    if insulin_level<=3:
        print("Warning! Sugar level is High")
        insulin_level=(insulinpump-counter)*10
        counter = counter-1
        print(insulin_level)
        
        insulinpump = insulinpump - 1
        print("Remaining insulin injection = ",insulinpump)
        if insulinpump==1:
            insulin_level = insulinpump*10
            print(insulin_level,"\n","Sugar level stablised")
            insulinpump=0
            print("Remaining insulin injection = ",insulinpump)
            print("Warning! Insulin out of reach......","\n","Need insulin injection...")
            break
    else:
        insulin_level = insulin_level - 1
        print(insulin_level)
