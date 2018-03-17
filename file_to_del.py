from apiclient.discovery import build

DEVELOPER_KEY = "AIzaSyArhRiaMcsLQIyhfH2_c32OE3N9YjtDelA"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def youtube_search(options):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey="AIzaSyArhRiaMcsLQIyhfH2_c32OE3N9YjtDelA")

    search_response = youtube.search().list(
        # the key on which it finds the video
        q=options
        part="id,snippet",
        maxResults=5
    ).execute()
    # outputs the json file
    return search_response.get("items", [])
