import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('edukid-91809-firebase-adminsdk-w42df-6321ae13d7.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

video_ref = db.collection(u'videos')
