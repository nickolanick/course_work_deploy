from apiclient.discovery import build

DEVELOPER_KEY = "AIzaSyArhRiaMcsLQIyhfH2_c32OE3N9YjtDelA"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def youtube_search(options):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey="AIzaSyArhRiaMcsLQIyhfH2_c32OE3N9YjtDelA")

    search_response = youtube.search().list(
        q=options + "review",
        part="id,snippet",
        maxResults=5
    ).execute()

    videos = []

    for search_result in search_response.get("items", []):
        videos.append("www.youtube.com/embed/" + search_result["id"]["videoId"])
    return videos


if __name__ == '__main__':
    print(youtube_search(input("enter name of product to EXPLORE! for example iphone 6, macbook air, etc... : ")))
