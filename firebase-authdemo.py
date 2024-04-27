
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

cred = credentials.Certificate("./src/serviceAccount.json")
firebase_admin.initialize_app(cred)


db = firestore.client()
data={
    'task':'washing',
    'status':'ToDO'
}
doc_ref = db.collection('taskCollection').document()

doc_ref.set(data)
print('Document ID : ',doc_ref.id)
