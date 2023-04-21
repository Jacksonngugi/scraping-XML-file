import matplotlib.pyplot as plt

time = []
frq = []

for line in open('chartdata.xml','r'):
    data = [i for i in line.split()]
    time.append(data[0])
    frq.append(data[1])

colour = ['yellow','green','red','blue','orange','cyan','pink','purple']

plt.title('A frequency chart of when this user(david.spade) logs in to event with eventid 4624',fontsize = 10)

plt.pie(frq,labels = time,colors = colour, startangle = 90,shadow = True,radius = 1.2,autopct = '%1.1f%%')

plt.show()