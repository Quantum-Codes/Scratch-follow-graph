import matplotlib.pyplot as plt
import requests, json

with open("users.json","r") as file:
  users = json.loads(file.read())

def parse(data):
  dates = []
  follows = []
  for item in data:
    item = list(item.values())
    dates.append(item[0][2:10])
    follows.append(item[1])
  #print(dates,"\n",follows)
  return (dates, follows)

def plot_data(user):
  x = requests.get(f"https://scratchdb.lefty.one/v3/user/graph/{user}/followers?segment=10&range=1440") #gets 144 points. segment 10 = follows every 10 days within 1440 days
  if x.status_code == 200:
    x = x.json()
    print(f"{user} req done! len={len(x)}\n")
    data = parse(x)
  else:
    print(f"{user} doesn't work idk why {x.status_code}")
    return None

  plt.figure() #this to plot multiple graphs
  plt.plot(data[0], data[1], label = "line 1")
#plt.autofmt_xdate()
  plt.xticks(rotation=90)
  plt.tight_layout() 
  plt.xlabel('Dates (yy-dd-mm)')
  plt.ylabel('followers')

  plt.savefig(f"graphs/{user}.svg", bbox_inches="tight")

for user in users:
  plot_data(user)
