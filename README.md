# Clinical-Trial-Matching-using-BERT-AND-XLNET
Dataset:
1. Patient Data - Generated simple patient data synthetically from synthea (https://github.com/synthetichealth/synthea) and is in patientData folder (currently 59 patient profiles in JSON format). The Patient.py file is used to get simplified patient profiles from synthea and whose output is the JSON files inside the PatientData folder.
2. Clinical Trials data - Accessed via API from https://clinicaltrials.gov/ct2/resources/download#UseURL
The above clinical Trials data is publically available for Analysis
3. Data for Medical system recommendation is present in overview_of_recordings.csv and the code is present in xlnet_medical_transcription.py
 
