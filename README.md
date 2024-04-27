# CRUD
CRUD: Create Read Update Delete Using Python and Admin Firebase

## Create firebase app
You'll need a Firebase project set up. If you don't have one, create one on the Firebase console.
<img src="https://github.com/iamrajharshit/firebaseCRUD/blob/main/img/create%20an%20app.png" title="create an app on fire base" alt="create an app on fire base" />&nbsp; 

- Here, we have created CRUD named web app.
- Select web app.
- Give a name.
- Select hosting. 

## Create firestore database
Once app is created,


<img src="https://github.com/iamrajharshit/firebaseCRUD/blob/main/img/Firestore%20create%20db.png" title="Go to Firestore" alt="Go to Firestore" />&nbsp; 

- Go to Firestore Database
- Create database


<img src="https://github.com/iamrajharshit/firebaseCRUD/blob/main/img/creating%20db.png" title="create DataBase" alt="create DataBase" />&nbsp;

- Select Start in Production mode
- Remember, once database is created will change the *allow read, write to true*.
- Click on Create

<img src="https://github.com/iamrajharshit/firebaseCRUD/blob/main/img/database%20is%20ready.png" title="DataBase is ready" alt="DataBase is ready" />&nbsp;

Your Database will look like this,
Once the database is created,

<img src="https://github.com/iamrajharshit/firebaseCRUD/blob/main/img/change%20to%20true.png" title="Change to true" alt="Change to true" />&nbsp;

- Go to _Rules_ inside the Fire database.
- Change the *allow read, write to __true__*.
- Click on _Publish_.

## Get Python config code
- Go to project setting -> Service Accounts -> Python(We will get the config code)
<img src="https://github.com/iamrajharshit/firebaseCRUD/blob/main/img/project%20setting.png" title="Go to project settings" alt="Go to project settings" />&nbsp;
<img src="https://github.com/iamrajharshit/firebaseCRUD/blob/main/img/copy%20the%20admin%20sdk%20code.png" title="Copy the Admin SDK file to your py app" alt="Copy the Admin SDK file to your py app" />&nbsp;

- Copy the Python code to your app.py on your local system.
Then, click on Service Account it will redirect to a page.

## Get the Key
Now will get key, after getting redirected to our Google Cloud, Service Account. 
<img src="https://github.com/iamrajharshit/firebaseCRUD/blob/main/img/manage%20keys.png" title="Go to Manage Keys" alt="Go to Manage Keys" />&nbsp;

- There again select service accounts, your account will be displayed.
- Click on 3 dots and click manage keys.

<img src="https://github.com/iamrajharshit/firebaseCRUD/blob/main/img/get%20json%20key.png" title="Get .json key" alt="Get .json key" />&nbsp;

- Click on **_Add Key_**.
- Select ***JSON*** as key type.
- Click on Create.

A file will be automatically downloaded.
<img src="https://github.com/iamrajharshit/firebaseCRUD/blob/main/img/downloaded%20key.png" title="Download the key" alt="Download the key" />&nbsp;

- Then just copy it to your project directory.

## Code
Here, we have renamed the ***JSON*** file as ***serviceAccount***.
<img src="https://github.com/iamrajharshit/firebaseCRUD/blob/main/img/pass%20to%20code%20.png" title="Pass the downloaded key" alt="Pass the downloaded key" />&nbsp;

- Pass the key and initialize firebase_admin

```
cred = credentials.Certificate("./serviceAccount.json")
firebase_admin.initialize_app(cred)

```


<img src="https://github.com/iamrajharshit/firebaseCRUD/blob/main/img/database%20code.png" title="Write a simple database code" alt="Write a simple database code" />&nbsp;
- add a database

## Run
- run the code
<img src="https://github.com/iamrajharshit/firebaseCRUD/blob/main/img/run%20the%20code%20.png" title="Run the code" alt="Run the Code" />&nbsp;
- check on firebase
<img src="https://github.com/iamrajharshit/firebaseCRUD/blob/main/img/stored%20in%20firebase.png" title="Check on FireBase" alt="Check on FireBase" />&nbsp;
