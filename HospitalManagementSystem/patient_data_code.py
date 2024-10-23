"""import pandas as pd

#to read CSV file into dataframe

file_path = 'coding/patient_records.csv'
patient_data = pd.read_csv(file_path)

#Display the DataFrame to verify data
print(patient_data)

#To print basic information about dataframe
print(patient_data.info())

#creating new DataFrame for new patient data
new_patient_data = pd.DataFrame({
    'Index no': [],
    'First name': [],
    'Surname': [],
    'Age': [],
    'Mobile': [],
    'Address': [],
    'Postcode': [],
    'Symptoms': [],
    'Allergies': []
    })

#lets assume, new_patient_data is dataframe that contains new patient records

#appending new patient data to existing DataFrame
patient_data = patient_data.append(new_patient_data, ignore_index = True)
patient_data.to_csv(file_path, index = False)

#retriveing specific data from DataFrame
#first_name = patient.data.loc[0, 'First name']
#print(first_name)
print(patient_data)
"""











