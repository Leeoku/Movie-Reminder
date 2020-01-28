from bs4 import BeautifulSoup
from datetime import date
import os, requests,json, ezgmail
from gmail import *

#from docxcleaner, movie_library is the list of titles we have
#get today's date
today = str((date.today()))

#create the url for tcm site
url = "http://www.tcm.com/schedule/canada/index.html?tz=est&sdate="+today
page = requests.get(url)

#get all items with class titleData and return text
soup = BeautifulSoup(page.text, 'lxml')
soup1 = soup.find_all ("div",class_="titleData")
titles = []

for movie in soup1:
    #movie_name = movie.contents[1].contents[0].contents[0] alternative way to get the movie name
    movie_name = movie.strong.text
    if movie_name.endswith(", The"):
        movie_name = "The "+ movie_name[:-5]
    elif movie_name.endswith(", A"):
        movie_name = "A "+movie_name[:-3]
    else:
        pass
    titles.append(movie_name)

#get all items with class timeData and return text
soup2 = soup.find_all("div",class_="timeData")
times = []

for time in soup2:
    if "\n" in time.text:
        time = time.text.replace("\n","")
    times.append(time)

#logic to check if titles are in movie_library
with open('/home/admin/Projects/Movie-Recording-Reminder/cleanedmovies.json') as json_file:
    movieLibrary = json.load(json_file)
recordList = [record for record in titles if record not in movieLibrary]

#create a dictionary to associate the current TCM schedule
schedule = dict(zip(titles, times))

#compare the shortened movie list not in data base to the schedule
recordSchedule = []
for program in recordList:
    if program in schedule:
        recordSchedule.append(f"{program} will be shown at {schedule[program]}\n")
recordScheduleString= '\n'.join(str(recordScheduleString) for recordScheduleString in recordSchedule)

'''alternate version
results = ""
for output in recordSchedule:
    results = results + "\n" + str(schedule)
print(results)'''

#send an email based on this data
emailSubject = f'Movies for {today}'
emailMessage = f"The following movies you don't have on {today} are: \n\n{recordScheduleString}"
header = 'To: '+to_address+'\n'
msg = f"{header}Subject: {emailSubject}\n\n{emailMessage}"
#print(msg)
smtpObj.sendmail(from_address,to_address,msg)