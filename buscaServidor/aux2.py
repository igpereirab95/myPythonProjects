# -*- coding: utf-8 -*-
from multiprocessing.dummy import Pool
import argparse
import requests
from bs4 import BeautifulSoup

def doRequest(req):
 try:
  session = requests.Session()
  browserContent = requests.get(req,timeout=5).content
  soup = BeautifulSoup(
    browserContent,"html.parser"
    )

  for script in soup.findAll("script"):
   src = script.attrs.get("src")
   if src:
    print(src)

 except requests.exceptions.Timeout:
    print("[Timeout]",req)
    pass
 except requests.exceptions.TooManyRedirects:
    print("[Too many redirect]",req)
    pass
 except OSError as dnsResolution:
    print("[Resolution Failed]",req)
    pass

 except Exception as e:
  print(e)
  #pass
 
def main(args):
 with open(args.file) as f:
  lines = f.read().splitlines()

  pool = Pool(args.threads)
  pool.map(doRequest, lines)
  pool.close()
  pool.join()

def menu():
 parser = argparse.ArgumentParser(
  description="Tool to be fool"
 )
 parser.add_argument(
  '-f', '--file',  
  help='Path location file where URLs seeds are presents', 
  default="urls.txt"
 )
 parser.add_argument(
  '-t', '--threads',
  help="Set max threads per second",
  type=int,
  default=40
 )

 return parser.parse_args()

if __name__ == "__main__":
    main(menu())