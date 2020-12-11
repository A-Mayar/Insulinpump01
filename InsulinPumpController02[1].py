import random
import logging
import time

logging.basicConfig(filename='Logs.log',level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(message)s')

def sensorcontroller(insulin):
    while insulin >= 0:
        Sugar_Level = random.randint(99,400)
        if insulin == 0:
            print("please fill insulin \n insulin = ",insulin)
            insulin = -1
        elif Sugar_Level <= 100: 
            print("SUGAR-LEVEL NORMAL...." )
        elif Sugar_Level > 100 and Sugar_Level <= 149:
            print("Sugar Level = ",Sugar_Level,"\n 1 unit injected....\n Sugar Level normalised...." )
            insulin = insulin - 1
        elif Sugar_Level > 149 and Sugar_Level <= 199:
            print("Sugar Level = ",Sugar_Level,"\n 2 units injected....\n Sugar Level normalised...." )
            insulin = insulin - 2
        elif Sugar_Level > 199 and Sugar_Level <= 249:
            print("Sugar Level = ",Sugar_Level,"\n 3 units injected....\n Sugar Level normalised...." )
            insulin = insulin - 3
        elif Sugar_Level > 249 and Sugar_Level <= 299:
            print("Sugar Level = ",Sugar_Level,"\n 4 units injected....\n Sugar Level normalised...." )
            insulin = insulin - 4
        elif Sugar_Level > 299 and Sugar_Level <= 349:
            print("Sugar Level = ",Sugar_Level,"\n 5 units injected....\n Sugar Level normalised...." )
            insulin = insulin - 5
        else:
            print("Sugar Level = ",Sugar_Level,"\n 6 units injected....\n Sugar Level normalised...." )
            insulin = insulin - 6
        logging.debug('Logs of Program... \n Insulin_injected = {} \n Sugar_Level = {}'.format(insulin,Sugar_Level))
        time.sleep(5)
    if insulin < 0 and insulin != 0:
        print("Insulin finished.....\n fill insulin....")


 
sensorcontroller(20)
        
