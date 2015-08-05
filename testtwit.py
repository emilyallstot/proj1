"""Demonstrate Twitter API"""

import os

import twitter


# Use Python os.environ to get at environmental variables
#
# Note: you must run `source secrets.sh` before running this file
# to make sure these environmental variables are set.

api = twitter.Api(
    consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
    consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
    access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
    access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])

# This will print info about credentials to make sure they're correct
print api.VerifyCredentials()

# Send a tweet
# status = api.PostUpdate('tweet body here')
# print status.text
# # Now you can go to http://twitter.com/ManiMapSF to see it

# search for content
pics = api.GetSearch(term="nail salon", geocode=(37.7833,-122.4167,'6km'), result_type="mixed")
for item in pics:
    print '\n'
    print item.text
    
