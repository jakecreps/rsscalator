# RSScalator
A utility that searches for RSS feeds from a CSV list of URLs

Thanks to @markditsworth for helping me make this happen

RSScalator is a Python script that takes a csv list that you have containing URLs and checks to see if an RSS feed exists for them. If an RSS feed exists, it will save that feed URL to a new csv.

Here are some ground rules:

1. You need to have a CSV with URLs you want to check named "source.csv". If you don't want to change your file name, make sure to change the name in rss.py
2. URLs should have https:// or http:// removed because the script adds https:// to your URL automatically
3. This script only checks /feed, /rss, and /xml. Because of this reason, I'm not guaranteeing that all RSS feeds were found. I'll be improving this once I find the gaps.
