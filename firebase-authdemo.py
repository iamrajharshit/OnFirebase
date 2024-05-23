
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

# Path to the service account key file (replace with your actual path)
cred = credentials.Certificate("serviceAccount.json")
#Initialize the Firebase Admin SDK with the credentials stored in the cred object. 
firebase_admin.initialize_app(cred)


#database
db = firestore.client()
data={
    'task':'washing',
    'status':'ToDO'
}
doc_ref = db.collection('taskCollection').document()

doc_ref.set(data)
print('Document ID : ',doc_ref.id)
