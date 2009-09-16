from PMS import *
from PMS.Objects import *
from PMS.Shortcuts import *

VIDEO_PREFIX   = "/video/railscasts"
BASE_URL       = "http://feeds.feedburner.com/railscasts_ipod?format=xml"
CACHE_INTERVAL = 1800
ICON           = "icon-default.png"

####################################################################################################
def Start():
  Plugin.AddPrefixHandler(VIDEO_PREFIX, VideoMenu, "Railscasts", ICON, "bg-default.png")
  Plugin.AddViewGroup("Details", viewMode="InfoList", mediaType="items")
  MediaContainer.art    = R('bg-default.png')
  MediaContainer.title1 = 'Railscasts'
  HTTP.SetCacheTime(CACHE_INTERVAL)
  
def VideoMenu():
    dir = MediaContainer(mediaType="video")  
    for item in XML.ElementFromURL(BASE_URL, False, errors='ignore').xpath('//item'):
      title       = item.find('title').text.strip()
      date        = item.find('pubDate').text.strip()
      description = item.find('description').text.strip()
      url         = item.find('enclosure').get("url").strip()
      dir.Append(VideoItem(url, title=title, summary=description, subtitle=date[0:-15]))
    return dir
