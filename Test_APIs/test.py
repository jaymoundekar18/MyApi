import requests

API_URL = "https://myapiservice-yn1p.onrender.com/employees"

employees = [
    {
        "firstname": "Lewis",
        "lastname": "Hamilton",
        "gender": "Male",
        "email": "lewis.hamilton@example.com",
        "address": "United Kingdom",
        "phone": "9000000001"
    },
    {
        "firstname": "Max",
        "lastname": "Verstappen",
        "gender": "Male",
        "email": "max.verstappen@example.com",
        "address": "Netherlands",
        "phone": "9000000002"
    },
    {
        "firstname": "Charles",
        "lastname": "Leclerc",
        "gender": "Male",
        "email": "charles.leclerc@example.com",
        "address": "Monaco",
        "phone": "9000000003"
    },
    {
        "firstname": "Sergio",
        "lastname": "Perez",
        "gender": "Male",
        "email": "sergio.perez@example.com",
        "address": "Mexico",
        "phone": "9000000004"
    },
    {
        "firstname": "Fernando",
        "lastname": "Alonso",
        "gender": "Male",
        "email": "fernando.alonso@example.com",
        "address": "Spain",
        "phone": "9000000005"
    },
    {
        "firstname": "Lando",
        "lastname": "Norris",
        "gender": "Male",
        "email": "lando.norris@example.com",
        "address": "United Kingdom",
        "phone": "9000000006"
    },
    {
        "firstname": "George",
        "lastname": "Russell",
        "gender": "Male",
        "email": "george.russell@example.com",
        "address": "United Kingdom",
        "phone": "9000000007"
    },
    {
        "firstname": "Carlos",
        "lastname": "Sainz",
        "gender": "Male",
        "email": "carlos.sainz@example.com",
        "address": "Spain",
        "phone": "9000000008"
    },
    {
        "firstname": "Oscar",
        "lastname": "Piastri",
        "gender": "Male",
        "email": "oscar.piastri@example.com",
        "address": "Australia",
        "phone": "9000000009"
    },
    {
        "firstname": "Pierre",
        "lastname": "Gasly",
        "gender": "Male",
        "email": "pierre.gasly@example.com",
        "address": "France",
        "phone": "9000000010"
    },
    {
        "firstname": "Esteban",
        "lastname": "Ocon",
        "gender": "Male",
        "email": "esteban.ocon@example.com",
        "address": "France",
        "phone": "9000000011"
    },
    {
        "firstname": "Valtteri",
        "lastname": "Bottas",
        "gender": "Male",
        "email": "valtteri.bottas@example.com",
        "address": "Finland",
        "phone": "9000000012"
    },
    {
        "firstname": "Zhou",
        "lastname": "Guanyu",
        "gender": "Male",
        "email": "zhou.guanyu@example.com",
        "address": "China",
        "phone": "9000000013"
    },
    {
        "firstname": "Yuki",
        "lastname": "Tsunoda",
        "gender": "Male",
        "email": "yuki.tsunoda@example.com",
        "address": "Japan",
        "phone": "9000000014"
    },
    {
        "firstname": "Alexander",
        "lastname": "Albon",
        "gender": "Male",
        "email": "alex.albon@example.com",
        "address": "Thailand",
        "phone": "9000000015"
    },
    {
        "firstname": "Logan",
        "lastname": "Sargeant",
        "gender": "Male",
        "email": "logan.sargeant@example.com",
        "address": "United States",
        "phone": "9000000016"
    },
    {
        "firstname": "Kevin",
        "lastname": "Magnussen",
        "gender": "Male",
        "email": "kevin.magnussen@example.com",
        "address": "Denmark",
        "phone": "9000000017"
    },
    {
        "firstname": "Nico",
        "lastname": "Hulkenberg",
        "gender": "Male",
        "email": "nico.hulkenberg@example.com",
        "address": "Germany",
        "phone": "9000000018"
    },
    {
        "firstname": "Lance",
        "lastname": "Stroll",
        "gender": "Male",
        "email": "lance.stroll@example.com",
        "address": "Canada",
        "phone": "9000000019"
    },
    {
        "firstname": "Daniel",
        "lastname": "Ricciardo",
        "gender": "Male",
        "email": "daniel.ricciardo@example.com",
        "address": "Australia",
        "phone": "9000000020"
    }
]

headers = {
    "Content-Type": "application/json"
}

for emp in employees:
    response = requests.post(API_URL, json=emp, headers=headers)

    if response.status_code in (200, 201):
        print(f"✅ Added: {emp['firstname']} {emp['lastname']}")
    else:
        print(f"❌ Failed: {emp['firstname']} {emp['lastname']}")
        print(response.status_code, response.text)
