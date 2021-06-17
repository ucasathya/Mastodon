from mastodon import Mastodon
import os

#   Set up Mastodon
mastodon = Mastodon(
    access_token = 'spxq-ji5UCJ3GCUEvFjart739K6tttG5dlQGog9D7h0',
    api_base_url = 'https://mastodon.social'
)

media = mastodon.media_post("C://Users//Asus//Desktop//New folder//test1.jpg")
mastodon.status_post("image!", media_ids=media)
print("succesfully")
