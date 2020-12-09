import requests
import csv

def rss_check():
    f = open("source.csv")
    csv_f = csv.reader(f)

    for row in csv_f:
        row = "".join(row)
        url = "https://" + row
        rss = ['/feed', '/rss', '/xml']
        for items in rss:
            feed = url + items
            try:
                r = requests.get(feed, timeout=5)
            except requests.exceptions.ConnectionError:
                pass
            except requests.exceptions.ReadTimeout:
                pass
            if r.status_code == 200:
                print("An RSS feed was found: " + feed)
                #Insert CSV writer here for results
                with open("rss.csv", "a") as output:
                        output.write(feed + "\n")
                break
            else:
                pass
rss_check()
