import json
import os

input_directory = 'output/fhir_stu3'
output_directory = 'output/simple_profiles'

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

def process_condition(condition_resource):
    return {
        "id": condition_resource["id"],
        "code": condition_resource["code"]["coding"][0]["code"],
        "display": condition_resource["code"]["coding"][0]["display"],
    }

for file_name in os.listdir(input_directory):
    with open(os.path.join(input_directory, file_name), 'r') as f:
        data = json.load(f)
    
    simple_profile = {}
    conditions = []
    for entry in data['entry']:
        resource = entry['resource']
        
        if resource['resourceType'] == 'Patient':
            simple_profile = {
                "id": resource["id"],
                "name": {
                    "family": resource["name"][0]["family"],
                    "given": resource["name"][0]["given"]
                },
                "gender": resource["gender"],
                "birthDate": resource["birthDate"],
                "conditions": conditions
            }
        elif resource['resourceType'] == 'Condition':
            conditions.append(process_condition(resource))

    if simple_profile:
        with open(os.path.join(output_directory, f'simple_{file_name}'), 'w') as f:
            json.dump(simple_profile, f, indent=2)
