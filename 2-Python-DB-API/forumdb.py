# "Database code" for the DB Forum.

import psycopg2
import datetime

#POSTS = [("This is the first post.", datetime.datetime.now())]



def get_posts():
  """Return all posts from the 'database', most recent first."""
  db = psycopg2.connect(database = "forum")
  pointer = db.cursor()
  query = "select content,time from posts order by time"
  pointer.execute(query)
  POSTS = pointer.fetchall()
  db.close()
  return POSTS
  #return reversed(POSTS)

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  db = psycopg2.connect(database = "forum")
  pointer = db.cursor()
  pointer.execute("insert into posts values(%s)",(content,))
  db.commit()
  db.close()
  #POSTS.append((content, datetime.datetime.now()))


