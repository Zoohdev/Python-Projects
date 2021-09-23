import sys

sys.path.append('/usr/local/lib/python3.7/dist-packages/')

import pyjokes
import time

while True:
 list_of_jokes = pyjokes.get_joke('en','neutral')
 print(list_of_jokes, sep='\n')
 time.sleep(5)

