import anonclass
from anonclass import *
import ftp_modul
import calc

print "What kind of information do you want take?"
print "1.What is my IP adress (proxy)"
print "2.Generation password for 3 and 4"
print "3.Facebook"
print "4.Gmail"
print "5.FTP"
print "6.Search and upload files in FTP"
print "7.Additional task"
print "8.Calculator"


x = int(raw_input("please enter your choice 1-3: "))
br = anonclass.Anon(useragent, proxies)
if x == 1:
     br.anonymize()
     anoymize_ip = br.connect_my_ip()

elif x == 2:
    br.generation_password()

elif x == 3:
    login_facebook = br.password()

elif x == 4:
    br.password_gmail()

elif x == 5:
    ip = raw_input("please enter FTP's IP: ")
    port = raw_input("please enter FTP's port: ")
    login_to_server = raw_input("please enter login for FTP: ")
    ftp_modul.bruteFTP(ip, port, login_to_server).FTPlogin()


elif x == 6:
    print "1.Do you want search file?"
    print "2.Do you want upload file?"
    y = int(raw_input("Enter you choose: "))
    if y == 1:
        ip = raw_input("please enter FTP's IP: ")
        port = raw_input("please enter FTP's port: ")
        login_to_server = raw_input("please enter login for FTP: ")
        file_name = raw_input("Which file are you  looking for? Enter his name(ex. index.php): ")
        ftp_modul.bruteFTP(ip,port, login_to_server, file_name).connect_to_server()
    elif y == 2:
        ip = raw_input("please enter FTP's IP: ")
        port = raw_input("please enter FTP's port: ")
        login_to_server = raw_input("please enter login for FTP: ")
        file_name = raw_input("Which file do you uploaded? Enter his name(ex. index.php): ")
        ftp_modul.bruteFTP(ip, port, login_to_server, file_name).send_file_to_server()
elif x == 7:
    print "1.Do you want check to port 21 is open?"
    print "2.Do you want check list of file in server?"
    print "3.Do you want change file in the server?"
    message = int(raw_input("Enter you choose: "))
    if message == 1:
        ip = raw_input("please enter FTP's IP: ")
        port = raw_input("please enter FTP's port: ")
        anonclass.Anon().check_port(ip, port)
    if message == 2:
        url = raw_input("Enter link to web-site: ")
        anonclass.Anon().printLinks(url)
    if message == 3:
        login_to_server = raw_input("please enter login for FTP: ")
        ip = raw_input("please enter FTP's IP: ")
        file_name = raw_input("Which file do you uploaded? Enter his name(ex. index.php): ")
        br = anonclass.Anon(useragent, proxies)
        anonclass.Anon().change_data_file(login_to_server, ip, file_name)

elif x == 8:
    print "1: ADDITION"
    print "2: SUBTRACTION"
    print "3: MULTIPLICATION"
    print "4: DIVITION"
    print "0: QUIT"
    while True:
        CHOICE = int(raw_input("ENTER THE CORRESPONDING NUMBER FOR CALCULATION "))
        if CHOICE == 1:
            print 'ADDING TWO NUMBERS:'
            print "Enter the two numbers to Add"
            A = int(raw_input("Enter A: "))
            B = int(raw_input("Enter B: "))
            calc.calculator(A, B).add()

        elif CHOICE == 2:
            print 'SUBTRACTING TWO NUMBERS'
            print "Enter the two numbers to Subtract"
            A = int(raw_input("Enter A: "))
            B = int(raw_input("Enter B: "))
            calc.calculator(A, B).sub()

        elif CHOICE == 3:
            print 'MULTIPLYING TWO NUMBERS'
            print "Enter the two numbers to Multiply"
            A = int(raw_input("Enter A: "))
            B = int(raw_input("Enter B: "))
            calc.calculator(A, B).mul()

        elif CHOICE == 4:
            print "DIVIDEING TWO NUMBERS"
            print "Enter the two number to Divide"
            A = float(raw_input("Enter A: "))
            B = float(raw_input("Enter B: "))
            calc.calculator(A, B).div()


        elif CHOICE == 0:
            exit()
        else:
            print "The value Enter value from 1-4"

