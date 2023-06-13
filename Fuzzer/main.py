from urllib import response
import requests
import re
import urllib.parse
import argparse
from datetime import datetime

word_directs = []
word_subs=[]
links=[]
results=[]
parser = argparse.ArgumentParser()

parser.add_argument("-l", "--link", dest="link", help="Link for fuzzing and search subdomains (http/s://name.domain) :)", required=True)
parser.add_argument("-pd", "--pathDir", dest="path_list_dirs", help="Path List for fuzzing directions :)", required=True)
parser.add_argument("-sl", "--searchLinks", dest='is_search_links', action='store_true', help="Flag for search links on pages :)")
parser.add_argument("-e", "--extension", dest='is_extension', action='store_true', help="Flag for addresses end with '/' :)")
parser.add_argument("-ps", "--pathSub", dest="path_list_subs", help="Path List for search subdomains :)")
options = parser.parse_args()

def main(options):
    url = check_url(options.link)

    print(":) I load a check file for fuzzing directions...")
    for word in load_file(options.path_list_dirs):
        word_directs.append(word)

    if len(word_directs) == 0:
        print(":) No links to check, use --help or -h for more info")
        return 

    if options.path_list_subs != "":
        print(":) I load a check file for fuzzing subdomains...")
        for word in load_file(options.path_list_subs):
            word_subs.append(word)

    if options.is_search_links:
        print(":) I write links in file links.txt...")
        write_links(url)
        print(":) End")

    fuzzing(url,options.is_extension,options.is_search_links)
    write_results()
    print(":) End")


def fuzzing(url,is_ext,is_search_links): 
    search_direct(url,is_ext,is_search_links)
    search_subs(url,is_ext,is_search_links)

def search_subs(url,is_ext,is_search_links):
    index = str(url).find('www')
    is_not_www = index == -1
    if is_not_www:
        index = str(url).find('//') + 2
    for word in word_subs:
        word = word.replace('\n','')
        if is_not_www:
            full_link = url[:index] + word + '.' + url[index:]
        full_link = str(url).replace('www',word)

        try:
            check_resp(full_link)
        except requests.ConnectionError:
            pass
        else:
            save_link(full_link)
            search_direct(full_link,is_ext,is_search_links)


def search_direct(url,is_ext=False,is_search_links=False):
    print(f":) I do Fuzzing directions {url}...")

    extension=''
    if is_ext:
        extension = '/'

    for link in word_directs:
        link = link.replace('\n','')
        full_link= ''.join((url,link,extension))

        if check_resp(full_link):
            save_link(full_link)
            if is_search_links:
                write_links(full_link)

def save_link(link):
    result=f":) {link} - she exists!"
    print(result)
    results.append(result)

def check_resp(link):
    response = requests.get(link,timeout=3)
    return response.status_code == 200

def write_results():
    date= datetime.now()

    with open('result.txt','at') as f:
        f.write('\n'+date.strftime("%H:%M:%S %d.%m.%Y")+'\n')
        for link in results:
            f.write(link+ '\n')
            
    print(":) I write all links in file result.txt")

def write_links(url):
    response = requests.get(url, timeout=3)
    cont = str(response.content)

    href_links = re.findall('(?:href=")(.*?)"',cont)
    with open('links.txt','at') as f:
        for link in href_links:
            link= urllib.parse.urljoin(url,link)
            if '#' in link:
                link = link.split('#')[0]
            if url in link and link not in links:
                links.append(link)
                f.write(link+'\n')
                write_links(link)


def check_url(url):
    if requests.get(url).status_code != 404:
        return url
    else:
        print("URL not exists, use --help or -h for more info :(")
        exit()

def load_file(file):
    with open(file, 'rt') as f:
        return f.readlines()

if __name__ == "__main__":
    main(options)