import twitter
from twitter import *
import schedule
import time
import random
import csv
# import wp

# this is the user we're going to query.

# consumer_key = "Lw3oCZmCVYGcAG3jmWYlgWcKB"
# consumer_secret = "aWC2mIakm2K7zwsx3CVVu2tk4tr8uhjlsku3hOjpMAscTlPCrc"
# access_key = "222803255-gKMMB5eB9uJUA4YaGLFNmCjFBdE0RHzFuYoMdv4a"
# access_secret = "bhuCjZ4DzxtdXnQUHY3M5dlwtgFgHxR45ISQTLYz2tFLz"

consumer_key = "WndSNVzDXDsj8Zet6NAClHr57"
consumer_secret = "L6lfGsRwcZY2O97gbWIW0MF2ysboyzArcrSKw1R53RZkbxLmnN"
access_key = "1610477173-TXOBfQOCHiEZ6zhUT9MWltw5eLtXgr1vlGkPpHb"
access_secret = "bG9pvlRgP2zEx6SSEIK0BjseRnif9HAKa9FydQaoqe2gc"


auth = OAuth(access_key, access_secret, consumer_key, consumer_secret)

try:
    twitter = Twitter(auth = auth)
except:
    print "No connection"


user_list = ['inspire_us','wisdomsquote', 'GreatestQuotes', 'alphabetsuccess', 'InspowerMinds', 'DavidRoads']#, Tweets2Motivate 

 

# fw = open('posted_twts.txt','w')
# fr = open('posted_twts.txt','r')

# results = twitter.statuses.update(status = new_status)
# print "updated status: %s" % new_status


def job():
    fw = open('posted_twts.csv', 'a')
    csvw = csv.writer(fw)
    fr = open('posted_twts.csv', 'rb')
    csvr = csv.reader(fr)
    user = random.choice(user_list)
    t_res = twitter.statuses.user_timeline(screen_name = user, include_rts=False, count=20)
    t_res = [random.choice(t_res)]
    for status in t_res:
        post = True
        for row in csvr:
            if row[0] == str(status['id']):
                post = False
        if post: 
            csvw.writerow([status['id']])
            new_status = status["text"]
            if 'http' in new_status:
                break
            new_status = new_status.replace('&amp;', '&')
            if len(new_status) < 123:
                new_status = new_status + " #Inspire" 
            print user,":", new_status
            try:
                twitter.statuses.update(status = new_status)
            except:
                print 'ERROR'
        fw.close()
        fr.close()

schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)

while 1:
    try:
        schedule.run_pending()
        time.sleep(1)
    except:
        print "ERROR"