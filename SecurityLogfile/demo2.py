from bs4 import BeautifulSoup as bs 


with open('SecurityLog.XML','r') as f:
      data= f.read()
      file = open('chart.py','a')
      soup = bs(data,'lxml')
      #print(soup)
      events = soup.find_all('event')
      ids =[]
      for event in events:
            id = event.find('eventid')
            id = id.get_text()

            if id == '4624':
                  ids.append(event)
      qs = []
      for i in ids:
            user = i.find('data' ,{'name':'TargetUserName'})
            user = user.get_text()

            if user == 'david.spade':
                  qs.append(i)
       
      count15 = []
      count14 = []
      count13 = []
      count12 = []
      count11 = []
      count10 = []
      count09 = []
      count08 = []
      
      for k in qs:
            time= k.find('timecreated')
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

            
      file.write(f"\n2011-04-16T15  {len(count15)}")
      file.write(f"\n2011-04-16T14  {len(count14)}")
      file.write(f"\n2011-04-16T13  {len(count13)}")
      file.write(f"\n2011-04-16T12  {len(count12)}")
      file.write(f"\n2011-04-16T11  {len(count11)}")
      file.write(f"\n2011-04-16T10  {len(count10)}")
      file.write(f"\n2011-04-16T09  {len(count09)}")
      file.write(f"\n2011-04-16T08  {len(count08)}")

      file.close()