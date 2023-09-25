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
    "46266":
        {
            "Name":"Chanotai Jansenak",
            "Gender":"Male",
            "Status" : "Student" ,
            "Class" : "M.5/3" ,
            "No" : "2" ,
            "Score" : "0" ,
            "Number" : "46266"
        },
    "46270":
        {
            "Name":"Papinwit Sungklum",
            "Gender":"Male",
            "Status" : "Student" ,
            "Class" : "M.5/3" ,
            "No" : "3" ,
            "Score" : "0" ,
            "Number" : "46270"
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
    "46300":
        {
            "Name":"Kittikun Phetmunee",
            "Gender":"Male",
            "Status" : "Student" ,
            "Class" : "M.5/3" ,
            "No" : "4" ,
            "Score" : "0" ,
            "Number" : "46300"
        },
    "46301":
        {
            "Name":"Chanatip Kumchatip",
            "Gender":"Male",
            "Status" : "Student" ,
            "Class" : "M.5/3" ,
            "No" : "5" ,
            "Score" : "0" ,
            "Number" : "46301"
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
    "46309":
        {
            "Name":"Ratchanon Chosungnoen",
            "Gender":"Male",
            "Status" : "Student" ,
            "Class" : "M.5/3" ,
            "No" : "7" ,
            "Score" : "0" ,
            "Number" : "46309"
        } , 
    "46312":
        {
            "Name":"Sirawish Rattanaprasert",
            "Gender":"Male",
            "Status" : "Student" ,
            "Class" : "M.5/3" ,
            "No" : "8" ,
            "Score" : "0" ,
            "Number" : "46312"
        } ,   
    "46319":
        {
            "Name":"Niphattiya Jamjuree",
            "Gender":"Female",
            "Status" : "Student" ,
            "Class" : "M.5/3" ,
            "No" : "22" ,
            "Score" : "0" ,
            "Number" : "46319"
        },
    "46339":
        {
            "Name":"Tanapat Rodauna",
            "Gender":"Male",
            "Status" : "Student" ,
            "Class" : "M.5/3" ,
            "No" : "9" ,
            "Score" : "0" ,
            "Number" : "46339"
        } , 
    "46340":
        {
            "Name":"Tanyanit Inthanasak",
            "Gender":"Male",
            "Status" : "Student" ,
            "Class" : "M.5/3" ,
            "No" : "10" ,
            "Score" : "0" ,
            "Number" : "46340"
        } , 
    "46353":
        {
            "Name":"Athitat Witthayapraphakorn",
            "Gender":"Male",
            "Status" : "Student" ,
            "Class" : "M.5/3" ,
            "No" : "11" ,
            "Score" : "0" ,
            "Number" : "46353"
        } , 
    "46376":
        {
            "Name":"Thanapoj Changbua",
            "Gender":"Male",
            "Status" : "Student" ,
            "Class" : "M.5/3" ,
            "No" : "12" ,
            "Score" : "0" ,
            "Number" : "46376"
        } , 
    "46377":
        {
            "Name":"Tanapat Simkaow",
            "Gender":"Male",
            "Status" : "Student" ,
            "Class" : "M.5/3" ,
            "No" : "13" ,
            "Score" : "0" ,
            "Number" : "46377"
        } , 
    "46379":
        {
            "Name":"Mark Thasawang",
            "Gender":"Male",
            "Status" : "Student" ,
            "Class" : "M.5/3" ,
            "No" : "14" ,
            "Score" : "0" ,
            "Number" : "46379"
        } , 
    "46396":
        {
            "Name":"Nuchjarin Nguanchoo",
            "Gender":"Female",
            "Status" : "Student" ,
            "Class" : "M.5/3" ,
            "No" : "23" ,
            "Score" : "0" ,
            "Number" : "46396"
        } , 
    "46404":
        {
            "Name":"Woon Warittha",
            "Gender":"Female",
            "Status" : "Student" ,
            "Class" : "M.5/3" ,
            "No" : "24" ,
            "Score" : "0" ,
            "Number" : "46404"
        } , 
    "46455":
        {
            "Name":"Kaiwit Khongcharoen",
            "Gender":"Male",
            "Status" : "Student" ,
            "Class" : "M.5/3" ,
            "No" : "15" ,
            "Score" : "0" ,
            "Number" : "46455"
        } , 
    "46474":
        {
            "Name":"Sirawit Chuaychuklin",
            "Gender":"Male",
            "Status" : "Student" ,
            "Class" : "M.5/3" ,
            "No" : "16" ,
            "Score" : "0" ,
            "Number" : "46474"
        } , 
    "46508":
        {
            "Name":"Tanawut Thongchay",
            "Gender":"Male",
            "Status" : "Student" ,
            "Class" : "M.5/3" ,
            "No" : "17" ,
            "Score" : "0" ,
            "Number" : "46508"
        } , 
    "46614":
        {
            "Name":"Setthawut Ounjai",
            "Gender":"Male",
            "Status" : "Student" ,
            "Class" : "M.5/3" ,
            "No" : "18" ,
            "Score" : "0" ,
            "Number" : "46614"
        } , 
    "46670":
        {
            "Name":"Tarin Klinsum",
            "Gender":"Female",
            "Status" : "Student" ,
            "Class" : "M.5/3" ,
            "No" : "26" ,
            "Score" : "0" ,
            "Number" : "46670"
        } , 
    "46713":
        {
            "Name":"Gadkanok Tuberg",
            "Gender":"Female",
            "Status" : "Student" ,
            "Class" : "M.5/3" ,
            "No" : "27" ,
            "Score" : "0" ,
            "Number" : "46713"
        } , 
    "46714":
        {
            "Name":"Kwanchira Charoenkasikit",
            "Gender":"Female",
            "Status" : "Student" ,
            "Class" : "M.5/3" ,
            "No" : "28" ,
            "Score" : "0" ,
            "Number" : "46714"
        } , 
    "48845":
        {
            "Name":"Kittiwat Sungchai",
            "Gender":"Male",
            "Status" : "Student" ,
            "Class" : "M.5/3" ,
            "No" : "19" ,
            "Score" : "0" ,
            "Number" : "48845"
        } ,
    "48846":
        {
            "Name":"Tachin Himthong",
            "Gender":"Male",
            "Status" : "Student" ,
            "Class" : "M.5/3" ,
            "No" : "20" ,
            "Score" : "0" ,
            "Number" : "48846"
        } , 
    "48847":
        {
            "Name":"Natwalan Limanont",
            "Gender":"Male",
            "Status" : "Student" ,
            "Class" : "M.5/3" ,
            "No" : "28" ,
            "Score" : "0" ,
            "Number" : "48847"
        } , 
    "48848":
        {
            "Name":"Phattathida Sanguanwong",
            "Gender":"Male",
            "Status" : "Student" ,
            "Class" : "M.5/3" ,
            "No" : "29" ,
            "Score" : "0" ,
            "Number" : "48848"
        } , 
        
    
}

for key,value in data.items():
    ref.child(key).set(value)