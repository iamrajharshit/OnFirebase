# CRUD
CRUD: Create Read Update Delete Using Python and Admin Firebase

## Create firebase app
You'll need a Firebase project set up. If you don't have one, create one on the Firebase console.
<img src="https://github.com/iamrajharshit/firebaseCRUD/blob/main/img/create%20an%20app.png" title="create an app on fire base" alt="create an app on fire base" />&nbsp; 

- Here, we have created ***CRUD*** named web app.
- Select ***Web App***.
- Give a ***Name*** and **ID**.
- Select your hosting ***Server*** and **Location**. 

## Create firestore database
Once app is created,


<img src="https://github.com/iamrajharshit/firebaseCRUD/blob/main/img/Firestore%20create%20db.png" title="Go to Firestore" alt="Go to Firestore" />&nbsp; 

- Go to ***Firestore Database***
- Click on ***Create database***


<img src="https://github.com/iamrajharshit/firebaseCRUD/blob/main/img/creating%20db.png" title="create DataBase" alt="create DataBase" />&nbsp;

- Select ***Start in Production mode***
- Remember, once database is created will change the *allow read, write to true*.
- Click on ***Create***.

<img src="https://github.com/iamrajharshit/firebaseCRUD/blob/main/img/database%20is%20ready.png" title="DataBase is ready" alt="DataBase is ready" />&nbsp;

Your database will look like this,
Once the database is created,

<img src="https://github.com/iamrajharshit/firebaseCRUD/blob/main/img/change%20to%20true.png" title="Change to true" alt="Change to true" />&nbsp;

- Go to **_Rules_** inside the Fire database.
- Change the *allow read, write to __true__*.
- Click on *__Publish__*.

## Get Python config code
We will get the `python config` code.
<img src="https://github.com/iamrajharshit/firebaseCRUD/blob/main/img/project%20setting.png" title="Go to project settings" alt="Go to project settings" />&nbsp;

- Select ***Project Settings*** under ***Project OVerview***.

Here, Admin SDK configuration snippet is available.
<img src="https://github.com/iamrajharshit/firebaseCRUD/blob/main/img/copy%20the%20admin%20sdk%20code.png" title="Copy the Admin SDK file to your py app" alt="Copy the Admin SDK file to your py app" />&nbsp;

- Select ***python***.
- Copy the ***Python config code*** to your ***app.py*** on your local system.
Then, click on ***Service Account*** it will redirect to a page.

## Get the Key
Now will get the key, after getting redirected to our Google Cloud, ***Service Account***. 
<img src="https://github.com/iamrajharshit/firebaseCRUD/blob/main/img/manage%20keys.png" title="Go to Manage Keys" alt="Go to Manage Keys" />&nbsp;

- Again select ***service accounts***, your account will be displayed.
- Click on 3 dots and click ***manage keys***.

<img src="https://github.com/iamrajharshit/firebaseCRUD/blob/main/img/get%20json%20key.png" title="Get .json key" alt="Get .json key" />&nbsp;

- Click on **_Add Key_**.
- Select ***JSON*** as key type.
- Click on ***Create***.

A file will be automatically downloaded.
<img src="https://github.com/iamrajharshit/firebaseCRUD/blob/main/img/downloaded%20key.png" title="Download the key" alt="Download the key" />&nbsp;

- Then just copy it to your project directory.

## Code

Remember to download all the dependencies mentioned in `requirements.txt` on your python venv.

```
pip install -r requirements.txt
```
To learn about python venv, check out the tutorial on [python venv](https://youtu.be/Gl88lVQOYAY?si=eS2d1xIaj1JqP9Yd).

Now added the dependencies to your app.py, here we have named our app.py as "firebase-authdemo.py".
```
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
```

Here, we have renamed the ***JSON*** file as ***serviceAccount***.
<img src="https://github.com/iamrajharshit/firebaseCRUD/blob/main/img/pass%20to%20code%20.png" title="Pass the downloaded key" alt="Pass the downloaded key" />&nbsp;

Inside the Python config code, 
- Pass the key ***"serviceAccount.json"*** and initialize `firebase_admin`

```
cred = credentials.Certificate("./serviceAccount.json")
firebase_admin.initialize_app(cred)

```


<img src="https://github.com/iamrajharshit/firebaseCRUD/blob/main/img/database%20code.png" title="Write a simple database code" alt="Write a simple database code" />&nbsp;

### Add a database.
Here, we have defined a dictionary named `data` that contains information about a task.

### The dictionary has two key-value pairs:
- **task**: The value is "washing," which presumably describes the task itself.
- **status**: The value is "ToDO," likely indicating the current state of the task.

Establishes a connection to your Firebase Firestore database.
- `firestore` is a module imported from the `firebase_admin` library, which provides functionality to interact with Firestore from your Python application.
- The `client()` method creates a client object that handles communication with the Firestore database.

```
db = firestore.client()
data={
    'task':'washing',
    'status':'ToDO'
}
doc_ref = db.collection('taskCollection').document()

doc_ref.set(data)
print('Document ID : ',doc_ref.id)
```

- `db.collection('taskCollection')`: This selects the existing collection named "taskCollection" within your Firestore database.
- `.document()`: This creates a new, empty document within the chosen collection. A unique document ID is automatically generated by Firestore.
- `.set(data)`: This method sets the data for the newly created document. The provided data dictionary is used to populate the fields within the document.
- The` doc_ref.id` attribute holds the unique identifier assigned to the document by Firestore.

## Run the code

Now, we run the firebase-authdemo.py file.

<img src="https://github.com/iamrajharshit/firebaseCRUD/blob/main/img/run%20the%20code%20.png" title="Run the code" alt="Run the Code" />&nbsp;

- We see Document ID being displayed in the terminal.
- They are different objects being stored to the database CRUD.

### Check on firebase

In Firebase Firestore,`taskCollection` is a collection within your Firestore database. A collection is a container that groups related documents together. In this case, each document likely represents a task.

- **Firestore**: A NoSQL database service offered by Firebase that allows you to store and retrieve data in a flexible and scalable manner.
- **Collection**: A group of documents with a similar theme or purpose. Think of it like a folder in a filing cabinet that holds related documents.
- **Document**: An individual unit of data within a collection, similar to a file in a folder. It contains fields (like key-value pairs) that represent the data for a specific task.
- **Field**: A property or attribute within a document that holds a specific piece of information. In this case, you have two fields:
    - `status`: A string field that likely indicates the current state of the task (e.g., "ToDO," "In Progress," "Done").
    - `task`: A string field that describes the actual task itself (e.g., "washing," "groceries," "exercise").

<img src="https://github.com/iamrajharshit/firebaseCRUD/blob/main/img/stored%20in%20firebase.png" title="Check on FireBase" alt="Check on FireBase" />&nbsp;
