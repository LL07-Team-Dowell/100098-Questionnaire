# Question 3
### Problem statement 
Database Operations
### Description 
At Dowell, we approach database operations in a unique way.
### Requirements 
- Understand the documentation .
- Write the best possible and clean code/api to do the database operations using Django-DRF .
    - Insert operations should be `POST` methods
    - Find or Fetch operations should be `GET` methods
- Marks will be based on the structure of the codebase

### Notice
You are required to deploy the project on GitHub and complete it within 7 days from the date of question selection. You must share both the codebase link and the deployed link on GitHub. Based on your performance, you will be considered for the next step in the interview process.

### Documentation
1. I want you to focus on the documentation .
2. We are using mongodb . Operations that we are focusing on 
    - Insert
    - Fetch
    - Find
3. Few functions that you need to understand is
    - Dowellconnection function
        ```python
        import json
        import requests
        import pprint
        def dowellconnection(cluster,database,collection,document,team_member_ID,function_ID,command,field,update_field):
            url = "http://uxlivinglab.pythonanywhere.com"
            payload = json.dumps({
                "cluster": cluster,
                "database": database,
                "collection": collection,
                "document": document,
                "team_member_ID": team_member_ID,
                "function_ID": function_ID,
                "command": command,
                "field": field,
                "update_field": update_field,
                "platform": "bangalore"
                })
            headers = {
                'Content-Type': 'application/json'
                }

            response = requests.request("POST", url, headers=headers, data=payload)
            res= json.loads(response.text)

            return res
            ```
    - Dowellevent creation function
        ```python
        import json
        import requests
        import pprint

        def get_event_id():

            url="https://uxlivinglab.pythonanywhere.com/create_event"

            data={
                "platformcode":"FB" ,
                "citycode":"101",
                "daycode":"0",
                "dbcode":"pfm" ,
                "ip_address":"192.168.0.41", 
                "login_id":"lav",
                "session_id":"new", 
                "processcode":"1",
                "location":"22446576", 
                "objectcode":"1",
                "instancecode":"100051",
                "context":"afdafa ",
                "document_id":"3004",
                "rules":"some rules",
                "status":"work",
                "data_type": "learn",
                "purpose_of_usage": "add",
                "colour":"color value",
                "hashtags":"hash tag alue",
                "mentions":"mentions value",
                "emojis":"emojis",
                "bookmarks": "a book marks"
            }

            r=requests.post(url,json=data)
            if r.status_code == 201:
                return json.loads(r.text)
            else: 
                return json.loads(r.text)['error']
        ```
    - Function to **insert data** 
        ```python
        field = {
            "eventId" : get_event_id()["event_id"],
            "Name":"Manish",
            "Role":"Developer",
            "company_id":"1000ABCDE"
        }

        update_field = {
            "status":"Nothing to update"
        }

        inserted_data = dowellconnection("hr_hiring","hr_hiring","dowelltraining","dowelltraining","1000554","ABCDE","insert",field,update_field)

        print(inserted_data)
        <!-- The result : {"isSuccess": true, "inserted_id": "644514695dfec19f3741d015"} -->
        ```
    - Function to **find data**
        ```python
        field = {
            "_id":"644514695dfec19f3741d015"
        }

        update_field = {
            "status":"Nothing to update"
        }

        find_data = dowellconnection("hr_hiring","hr_hiring","dowelltraining","dowelltraining","1000554","ABCDE","find",field,update_field)

        print(find_data)
        <!-- The result : {"isSuccess": true, "data": {"_id": "644514695dfec19f3741d015", "Name": "Manish", "Role": "Developer", "company_id": "1000ABCDE"}} -->
        ```
    - Function to **fetch data**
        ```python
        field = {
            "company_id":"1000ABCDE"
        }

        update_field = {
            "status":"Nothing to update"
        }

        fetched_data = dowellconnection("hr_hiring","hr_hiring","dowelltraining","dowelltraining","1000554","ABCDE","fetch",field,update_field)

        print(fetched_data)

         <!-- The result : {"isSuccess": true, "data": [{"_id": "644514695dfec19f3741d015", "Name": "Manish", "Role": "Developer", "company_id": "1000ABCDE"}, {"_id": "6445179ac93da579c653ca0f", "Name": "Nitesh", "Role": "Designer", "company_id": "1000ABCDE"}]} -->
        
        ```
    Important Notes : 
    1. Every insertion there should be a unique company_id 
    2. `"hr_hiring","hr_hiring","dowelltraining","dowelltraining","1000554","ABCDE"` , this value should not change.
    3. Every insertion there should eventId , `"eventId" : get_event_id()["event_id"]` 
### Conclusion :
Deploy your project onto any deployment service provider and submit postman collection .