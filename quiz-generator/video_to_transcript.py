from youtube_transcript_api import YouTubeTranscriptApi
import re

# transcription language
languages=['en']

# regex to remove transcript tags
regex_for_remove_transcript_tags = '^\[.*\]$'

'''
    @param video_id - YouTube video id 
    @:returns transcript
'''
def youtube_video_transcript(video_id):

    transcript = []
    # call for YouTube Transcript API
    data = YouTubeTranscriptApi.get_transcript(video_id,languages)
    if data is None:
        return None
    for _ in data:
        # check _ is in dictionary format
        if type(_) is dict:
            text = _['text']
            if text is not None and not re.search(regex_for_remove_transcript_tags, text):
                transcript.append(text)

    transcript_text = ' '.join(transcript)
    return transcript_text
