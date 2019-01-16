#!/usr/bin/python
import re, logging, csv
# logger setup
LOG_FORMAT = "%(asctime)s %(levelname)s - %(message)s"
logging.basicConfig(filename="logger1.log",
level=logging.DEBUG, format=LOG_FORMAT, filemode='w')
logger = logging.getLogger()
#regex
regex_Email = '(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
regex_Vorname = "^[A-Za-z-]{2,} [A-Za-z-]{2,}$"
#OPENING FIlE
logger.info("OPENING FILE")
ifile = open('data.csv')
reader = csv.reader(ifile, delimiter=";")
ofile = open('data_output.csv', "w")
writer = csv.writer(ofile, delimiter=";")

#a for-loop to write all rows in the new file called data_output.csvself.
#The if checks the email with regex if the email isnt valid,
#else, all of the the arry-objects will be none
#added a logger in the else statement
x = 0
for row in reader:
    if re.search(regex_Email, row[3]) and re.search(regex_Vorname, row[2]):
        if x > 0:
            print("")
        else:
            print('Datensatz wurde gespeichert')
    else:
        logger.info("Writing data in new file failed")
        print('Datensatz konnte nicht gespeichert werden, da er nicht valid ist.')
        row[0] = None
        row[1] = None
        row[2] = None
        row[3] = None
    #Wirtes the the data in the new file
    print(x)
    writer.writerow(row)
    x = x + 1
􏰉􏰐􏰗􏰨􏱇􏱓􏰾􏰘􏰨􏰣􏰑􏰚􏰐􏰗􏰨􏱇􏰬􏰾􏰘􏰨􏰣􏰗􏰦􏱇􏱓􏰾􏰘􏰨􏰣􏰑􏰚􏰐􏰥􏰦􏰑􏰏
