from bs4 import BeautifulSoup as bs 

#USED THIS BLOCK OF CODE TO GET THE NAME OF USERS(BOTH HUMAN AND COMPUTER) WHO CONNECTED TO THE NETWORK
with open('SecurityLog.XML','r') as f:
      data= f.read()
      soup = bs(data,'lxml')
        #print(soup)
      events = soup.find_all('event')
      df =[]
      for event in events:
            id = event.find('eventid')
            id = id.get_text()

            if id == '4624':
                  df.append(event)
      username = []
      compname = []
      for i in df:
            name = i.find('data' ,{'name':'TargetUserName'})
            name = name.get_text()
            #Here i separate computer and human users
            if '$' not in name:
                  username.append(name)

            elif '$' in name:#Compuuter usernames have $ as one of character 
                  compname.append(name)
       #The function below will produce the frequent login user
      def frequent_user(list):

            print(max(set(list),key = list.count))
      
      print(len(username))

            