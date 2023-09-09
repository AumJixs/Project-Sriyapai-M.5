import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred , {
    "databaseURL" :"https://databasestudentid-default-rtdb.firebaseio.com/"
    }
)

ref = db.reference("Students")

data = {
    "46264":
        {
            "Name":"Jirapat Wichaidit",
            "Gender":"Male",
            "Status" : "Student" ,
            "Class" : "M.5/3" ,
            "No" : "1" ,
            "Score" : "0" ,
            "Number" : "46264"
        },
    "46281":
        {
            "Name":"Natnaree Salaanan",
            "Gender":"Female",
            "Status" : "Student" ,
            "Class" : "M.5/3" ,
            "No" : "21" ,
            "Score" : "0" ,
            "Number" : "46281"

        },
    "46305":
        {
            "Name":"Chunchill",
            "Gender":"Male",
            "Status" : "Student" ,
            "Class" : "M.5/3" ,
            "No" : "6" ,
            "Score" : "0" ,
            "Number" : "46305"
            
        },
    "46319":
        {
            "Name":"Niphattiya Jamjuree",
            "Status" : "Student" ,
            "Class" : "M.5/3" ,
            "No" : "22" ,
            "Score" : "0" ,
            "Number" : "46319"

        }
}

for key,value in data.items():
    ref.child(key).set(value)