from firebase_setup import video_ref

'''
    @:param data takes dictionary type argument which contains key and value pair
'''
def addDocument(data):
    new_doc = video_ref.document(data['videoID'])
    new_doc.set(data)
