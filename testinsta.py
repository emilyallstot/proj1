from instagram.client import InstagramAPI

client_secret = "INSTAGRAM_CLIENT_SECRET"
client_id = "INSTAGRAM_CLIENT_ID"

# api = InstagramAPI(access_token=access_token, client_secret=client_secret)

# http://jelled.com/instagram/lookup-user-id#
api = InstagramAPI(client_id=client_id, client_secret=client_secret)
popular_media = api.media_popular(count=20)
for media in popular_media:
    print media.images['standard_resolution'].url