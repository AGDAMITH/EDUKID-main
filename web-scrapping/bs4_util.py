from bs4 import BeautifulSoup
import requests
from config import HEADER

'''
    @:param source - YouTube video url
    @:returns
        videoID
        videoTitle
        videoImage
        videoUrl
        videoViews
        videoDatePublished
        videoDuration
'''
def getYouTubeVideoStats(source):
    response = requests.get(source, headers=HEADER)
    soup = BeautifulSoup(response.text, "html.parser")
    idSoupMeta = soup.find("meta",itemprop="videoId")
    titleSoupMeta = soup.find("meta",property="og:title")
    thumbSoupMeta = soup.find("meta",property="og:image")
    videoSoupMeta = soup.find("meta",property="og:video:url")
    viewsSoupMeta = soup.find("meta",itemprop="interactionCount")
    datePublishedSoupMeta = soup.find("meta",itemprop="datePublished")
    videoDurationSoupMeta = soup.find("meta",itemprop="duration")

    videoID = idSoupMeta["content"] if idSoupMeta else "Notfound"
    videoTitle = titleSoupMeta["content"] if titleSoupMeta else "NotFound"
    videoImage = thumbSoupMeta["content"] if thumbSoupMeta else "NotFound"
    videoUrl = videoSoupMeta["content"] if videoSoupMeta else "Not Found"
    videoViews = viewsSoupMeta["content"] if viewsSoupMeta else "NotFound"
    videoDatePublished = datePublishedSoupMeta["content"] if datePublishedSoupMeta else "Not Found"
    videDuration = videoDurationSoupMeta["content"] if videoDurationSoupMeta else "Not Found"

    data = {"videoID" : videoID, "videoTitle" : videoTitle, "videoImage" : videoImage, "videoUrl" : videoUrl,
            "videoViews" : videoViews, "videoDatePublished" : videoDatePublished , "videDuration" : videDuration}

    return data
