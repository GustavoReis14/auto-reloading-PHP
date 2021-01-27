import os
import sys
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from threading import Thread
from time import sleep
from datetime import datetime
from colorama import Fore, Style, Back

PORT = sys.argv[2]

class PhpServer(Thread):
  def __init__(self):
    Thread.__init__(self)

  def run(self):
    os.system('php -S localhost:' + PORT) 


class AutomaticReload(Thread):
  def __init__(self):
    Thread.__init__(self)
    self.browser = webdriver.Firefox(service=Service('./geckodriver'))
    self.browser.get('http://localhost:'+ PORT +'/teste.php')
    self.updated_content = ''

  def run(self):
    while True:
      self.file = open('./teste.php', 'r')
      self.content = self.file.read()
      self.file.close()
      if self.updated_content != self.content and len(self.content) != 0:
        print(f'{Fore.GREEN}{Back.WHITE}[{datetime.now()}] FILE UPDATED{Style.RESET_ALL}')
        self.updated_content = self.content
        self.browser.refresh()

    self.browser.close()

    

if __name__ == '__main__':
  PhpServer().start()
  AutomaticReload().start()