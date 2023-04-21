#I used this file to answer stage2 

from bs4 import BeautifulSoup as bs 


with open('SecurityLog.XML','r') as f:

      file = open('eventid(4624).xml','a')
      files = open('no of times an eventid occured.xml','a')
      fil = open('events with id.xml','a')
      data= f.read()
      soup = bs(data,'lxml')
        #print(soup)
      events = soup.find_all('event')
#THIS FUNCTION WHEN CALLED WILL GIVE ALL EVENT WITH GIVEN EVENTID AS OUTPUT
      def eventswithid(eventid):
            ids = []

            for event in events:
                  id = event.find('eventid')
                  id = id.get_text()

                  if id == eventid:
                        ids.append(event)
   
            print(ids)
            fil.write(f'{ids}')

      
#When pass eventid as argument inside event() function the call the function you will get the number of time an eventid occured
      def event(eventid):
            
            ids = []

            for event in events:
                  id = event.find('eventid')
                  id = id.get_text()

                  if id == eventid:
                        ids.append(id)
                        #files.write(f'\n{event}')

            print(eventid,len(ids))

            files.write(f'\nEventid {eventid} occured {len(ids)} times')

          

#When noofevents() is called,it gives the total number of events that occured in a certain time 
      

      def noofevent(eventid):
            ids = []
            for event in events:
                  id = event.find('eventid')
                  id = id.get_text()

                  if id == eventid:
                        ids.append(event)
            count08 = []
            count09 = []
            count10 = []
            count11 = []
            count12 = []
            count13 = []
            count14 = []
            count15 = []
            for i in ids:
                  time = i.find('timecreated')
                  time = time['systemtime']
                  time = time.split(":")[0]

                  if time == '2011-04-16T15':
                        count15.append(1)

                  if time == '2011-04-16T14':
                        count14.append(1)

                  if time == '2011-04-16T13':
                        count13.append(1)

                  if time == '2011-04-16T12':
                        count12.append(1)

                  if time == '2011-04-16T11':
                        count11.append(1)

                  if time == '2011-04-16T10':
                        count10.append(1)

                  if time == '2011-04-16T09':
                        count09.append(1)

                  if time == '2011-04-16T08':
                        count08.append(1)

            print('2011-04-16T15', len(count15))
            print('2011-04-16T14', len(count14))
            print('2011-04-16T13', len(count13))
            print('2011-04-16T12', len(count12))
            print('2011-04-16T11', len(count11))
            print('2011-04-16T10', len(count10))
            print('2011-04-16T09', len(count09))
            print('2011-04-16T08', len(count08))

            file.write(f'\nNUMBER OF TIMES THAT THE EVENT WITH EVENTID {eventid} OCCURED OVER TIME:')
            file.write('\n')
            file.write(f"\n2011-04-16T15  {len(count15)}")
            file.write(f"\n2011-04-16T14  {len(count14)}")
            file.write(f"\n2011-04-16T13  {len(count13)}")
            file.write(f"\n2011-04-16T12  {len(count12)}")
            file.write(f"\n2011-04-16T11  {len(count11)}")
            file.write(f"\n2011-04-16T10  {len(count10)}")
            file.write(f"\n2011-04-16T09  {len(count09)}")
            file.write(f"\n2011-04-16T08  {len(count08)}")

      
      #if you to write to a file,just uncomment the write() function containing the information the call the main function

      file.close()
      files.close()
      fil.close()

            

            

