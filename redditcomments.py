"""
Simple Comment Parser which uses praw (Python API for Reddit) and pymongo (Python driver for MongoDB) to store certain comment attributes into
a MongoDB Database.
"""

import pymongo
import praw

"""
Open MongoDB Connection to DB "reddit"
"""
db = pymongo.MongoClient().reddit

"""
Create the reddit object, and pull comment stream from http://reddit.com/r/all/comments
"""
r = praw.Reddit('Comment Parsing by /u/joeskyyy')
all_comments = r.get_comments('all')

"""
Loop through the list of comments returned and store their id, content, author, subreddit, and permalink
"""
for comment in all_comments:
        db.comments.insert({'id':comment.id, 'comment':comment.body, 'author': str(comment.author), 'subreddit': str(comment.subreddit), 'permalink': comment.permalink})
