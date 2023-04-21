from bs4 import BeautifulSoup as bs 

#This block will give the first and last events in the log file
with open('SecurityLog.XML','r') as f:
      
      file = open('eventid(4624).xml','w')
      data= f.read()
      soup = bs(data,'lxml')
        #print(soup)
      events = soup.find_all('event')

      times = []

      for event in events:
                id = event.find('eventid')
                id = id.get_text()
            

                time = event.find('timecreated')
                time = time['systemtime']
                #time = time.split(":")[0]

                times.append(time)

      print('Time last event occured at: ',times[0])
      print('Time first event occured at: ',times[len(times)-1])