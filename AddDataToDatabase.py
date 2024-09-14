import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://attendanceautomation-758b2-default-rtdb.firebaseio.com/"
})
ref = db.reference('Students')

data = {
    "201655":
        {
            "name": "Ayush",
            "major": "CSE",
            "starting_year": 2022,
            "total_attendance": 13,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2023-12-11 00:54:34"
        },
    "201666":
        {
            "name": "Narendra Modi",
            "major": "EEE",
            "starting_year": 2023,
            "total_attendance": 10,
            "standing": "G",
            "year": 1,
            "last_attendance_time": "2023-14-11 09:14:30"
        },
    "202112":
        {
            "name": "Aayush Arya",
            "major": "CE",
            "starting_year": 2022,
            "total_attendance": 14,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2024-15-01 08:50:14"
        },
    "231456":
        {
            "name": "Kritya",
            "major": "B.Com",
            "starting_year": 2023,
            "total_attendance": 5,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2023-19-11 09:10:20"
        },
    "245645":
        {
            "name": "Deepak",
            "major": "CSE",
            "starting_year": 2021,
            "total_attendance": 22,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2023-25-11 10:20:21"
        },
    "251664":
        {
            "name": "Divyansh",
            "major": "EEE",
            "starting_year": 2023,
            "total_attendance": 10,
            "standing": "G",
            "year": 1,
            "last_attendance_time": "2023-23-11 11:47:30"
        },
    "303112":
        {
            "name": "Raghu Ram",
            "major": "BBA",
            "starting_year": 2023,
            "total_attendance": 4,
            "standing": "G",
            "year": 1,
            "last_attendance_time": "2023-23-11 11:45:30"
        },
    "303113":
        {
            "name": "Rajiv Laxman",
            "major": "BCA",
            "starting_year": 2023,
            "total_attendance": 4,
            "standing": "G",
            "year": 1,
            "last_attendance_time": "2023-23-11 11:47:10"
        },
    "852741":
        {
            "name": "Emly Blunt",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 3,
            "last_attendance_time": "2023-19-11 10:44:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2024-12-01 00:54:34"
        },
    
}
for key, value in data.items():
    ref.child(key).set(value)