import requests
from weather import *
import random

class Poetry:
  def poem():
    list = Weather.tempWeek()
    
    number = list[0]
    api_url = "https://poetrydb.org/linecount/"+str(number)
    
    request = requests.get(api_url)
    listofPoems = request.json()
    num = len(listofPoems)
    chooseOne = random.randrange(num+1)

    thePoem =listofPoems[chooseOne]
    
    title = thePoem['title']
    line = thePoem['lines']

    numLine = int(list[1])
    windLine = line[numLine]
    
    return([title,windLine])
    
  
  poem()