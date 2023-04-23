from dowellconnection import dowellconnection
from event import get_event_id

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


