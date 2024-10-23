import pandas as pd
from Doctor import Doctor
from getpass import getpass
from Patient import Patient



class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address='', patients= None):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
            patients (list, optional): List of patients Defaults to None
        """

        self.__username = username
        self.__password = password
        self.__address =  address
        
        self.patients = patients or [] #assume to have a list for storing patient's symptoms
        
        
    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    def login(self):
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
    
        print("-----Login-----")
        #Get the details of the admin

        entered_username = input('Enter the username: ')
        entered_password = getpass('Enter the password: ')

        # check if the username and password match the registered ones
 #ToDo1----------------
        if self.__username == entered_username and self.__password ==  entered_password:
            print("Login is successful.")
            return self.__username
        else:
            raise Exception("Invalid Username or Password. Please try again!")

    def find_index(self,index,doctors):
        
            # check that the doctor id exists          
        if index in range(0,len(doctors)):
            
            return True

        # if the id is not in the list of doctors
        else:
            return False
            
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
#ToDo2-------------------------
        print("----Enter Doctor Details----")
        first_name = input("Enter Doctor's First Name: ")
        surname = input("Enter Doctor's Surname: ")
        speciality = input ("Enter Doctor's Speciality:- ")
        print("Entered  details:-", first_name, surname, speciality) #this would make sure the details have been added
        
        return(first_name, surname, speciality)

    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("-----Doctor Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

#ToDo3-------------
        op = input("Please Enter your Choice from 1-4: ") 


        # register
        if op == '1':
            print("-----Register-----")

            # get the doctor details
            print('Enter the doctor\'s details:')
            first_name, surname, speciality = self.get_doctor_details()
#ToDo4
            #creating new doctor object 
            new_doctor = Doctor(first_name, surname, speciality)

            # check if the name is already registered
            name_exists = any(
                existing_doctor.get_first_name() == first_name and
                existing_doctor.get_surname() == surname
                for existing_doctor in doctors
                )
            
            
#ToDo5-------------------
            if name_exists:
                print("This Name already exist.")         # save time and end the loop
         
#ToDo6-------------
            # add the doctor ...
            
            else:
                doctors.append(new_doctor)
                print("Doctor is registered")
                                                         # ... to the list of doctors
                                                         
        # View
        elif op == '2':
            print("-----List of Doctors-----")
#ToDo7--------------
            #to check if there's any doctor record to display
            if not doctors:
                print("No doctors registered")
            else:
                #loop and printing each doctor's info
                for index, doctor in enumerate(doctors, start=1):
                    print(f'{index:3} | {doctor.full_name():<30} | {doctor.get_speciality():<15}')
        # Update
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    doctor_index=self.find_index(index,doctors)
                    if doctor_index!=False:
                        break
                        
                    else:
                        print("Doctor not found")

                    
                        # doctor_index is the ID mines one (-1)
                        

                except ValueError: # the entered id could not be changed into an int
                    print('The ID entered is incorrect')

            # menu
            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')
            op = int(input('Input: ')) # make the user input lowercase
#Retrieve the doctor object
#ToDo8-------------
            doctor_to_update = doctors[index]
            
            if op == 1:
                #update first name
                new_first_name = input("Enter the new First Name:- ")
                doctor_to_update.set_first_name(new_first_name)
                print("First name of Doctor is updated successfully")
                
                
            elif op == 2:
                #update surname
                new_surname = input("Enter the new Surname:- ")
                doctor_to_update.set_surname(new_surname)
                print("Surname is updated successfully.")
                
                
            elif op == 3:
                #update speciality
                new_speciality = input("Enter the new Speciality:- ")
                doctor_to_update.set_speciality(new_speciality)
                print("Speciality is updated successfully.")
                
                
            else:
                print("Invalid option. Please try again!")
                

        # Delete
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)
            
            try:
                doctor_index = int(input('Enter the ID of the doctor to be deleted: ')) -1
#ToDo9------------------
                if self.find_index(doctor_index, doctors):
                    deleted_doctor = doctors.pop(doctor_index)
                    print(f"Doctor {deleted_doctor.full_name()} deleted successfully.") 
                else:
                    print('The id entered is incorrect')

        # if the id is not in the list of patients
            except ValueError:
                print('Invalid operation choosen. Check your spelling!')


    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
#ToDo10---------------
        #check if there's any records of patients to display
        if not patients:
            print("No patients registered")
        else:
            #print each patient's info
            for index, patient in enumerate(patients,start=1):
                print(f"{index:2} | {patient.full_name():<30} | {patient.get_doctor():<30} | {patient.get_age():<3} | {patient.get_mobile():<15} | {patient.get_postcode():<10}")
      

    def assign_doctor_to_patient_with_symptoms(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assigning registered patient to doctor-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)
        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return 

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return
        
        #add symptoms to the patient
        
        print("--------Enter Patient Symptoms-------")
        symptom1 = input("Enter symptom 1:- ")
        symptom2 = input("Enter symptom 2:- ")
        symptom3 = input("Enter symptom 3:- ")
        
        #Add symptoms to the patient
        patients[patient_index].add_symptoms([symptom1, symptom2, symptom3])
        
        #check if the patient is already assigned to a doctor
        current_doctor = patients[patient_index].get_doctor()
        if current_doctor !="None": 
            print(f"The patient is already assigned to doctor: {current_doctor}.")
            print("-----Current Assignement----")
            print(f"ID  |    {patients[patient_index].get_id() or 'None'}   |   {patients[patient_index].full_name()}    |   Assigned to: {current_doctor}") 
        
        else: 
            print("The patient is not yet assigned to any doctor")
             
            
        
        #show all available doctors list to admin

        print("-----Doctors Select-----")
       

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors):
                
                    
                # link the patients to the doctor and vice versa
#ToDo11------------------------
                if patients[patient_index].get_doctor() == "None": #check if the patient is already assigned to a doctor
                    patients[patient_index].link(doctors[doctor_index].full_name()) #link the patient to the new doctor
                    doctors[doctor_index].add_patient(patients[patient_index]) #add the patient to the doctor's list of patients
                    print("the patient is now assigned to selected doctor")
                else:
                    print("The patient is already assigned to a doctor.")
                    

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')


    def discharge(self, patients, discharge_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        print("-----Discharge Patient-----")

        patient_index = input('Please enter the patient ID: ')

#ToDo12-----------------------
        try:
            #patient_index is the Patient ID -1
            patient_index = int(patient_index) -1
            
            #check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print("Unfortunately! The id entered was not found")
                return #procedure stopped
            
            #check in case patient is already discharged
            if patient_index in[patient.get_id() for patient in discharge_patients]:
                print("This patient is already discharged")
            else:
                discharge_patients.append(patients.pop(patient_index))
                print("This patient has been discharged")
                
        except ValueError:
            print("The id entreed is incorrect") 
            
        
    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
#ToDo13----------------------------
        if not discharged_patients:
            print("No patients have been discharged.")
        else:
            for index, patient in enumerate(discharged_patients, start=1):
                print(f'{index:3} | {patient.full_name():<30} | {patient.get_doctor():<30} | {patient.get_age():^5} | {patient.get_mobile():^15} | {patient.get_postcode():^10}')

    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """

        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        op = int(input('Enter the selected ID:-  ')) 
        if op == 1:
#ToDo14-------------------------------
                new_username = input("Enter the new username:- ")
                self.__username = new_username 

        elif op == 2: 
              password = input('Enter the new password: ')
              
            # validate the password
              if password == input('Enter the new password again: '):
                self.__password = password 
        elif op == 3:
#ToDo15------------------------------            
            new_address = input("Enter the new address:- ")
            self.__address = new_address

        else:
            
#ToDo16--------------------------------
            print("Invalid option. Please choose valid option between(1-3)")
        self.view_admin_details()
            
    def view_admin_details(self):
        print("-------Admin Details-----")
        print(f"Username: {self.__username}")
        print(f"Password: {self.__password}")
        print(f"Address: {self.__address}")
        
#---------admin registering more patients 
    def display_patient_menu(self):
        """Display sub-menu for patient management"""
        while True:
            print("\n----Patient Management-----")
            print("1. View Patients")
            print("2. Register New Patients")
            print("3. Update Patients Details")
            print("4. Delete Patients")
            print("5. Back to the Main Menu")
            
            patient_management_option = input("Choose an option:")
            
            if patient_management_option =='1':
                self.view_patients()
            elif patient_management_option == '2':
                self.register_patient()
            elif patient_management_option == '3':
                self.update_patient()
            elif patient_management_option == '4':
                self.delete_patient()
            elif patient_management_option == '5':
                break
            else:
                print("Invalid option. Please choose again!")
            
    def view_patients(self):
        """View existing and new patients"""
        #this would display table for all patients (existing + new)
        print("------All Patients-----")
        self.display_all_patients()
        
      #Displaying table for grouped patients based on surname
        print("\n---- Grouped Patients---")
        self.display_grouped_patients()
    
    def display_grouped_patients(self):
        print("-----Grouped Patients-----")
        grouped_patients = {}
        if self.patients:
            
        #group patients by their surname 

           for patient in self.patients:
              if patient.get_surname() in grouped_patients:
                grouped_patients[patient.get_surname()].append(patient)
              else:
                grouped_patients[patient.get_surname()] = [patient]
                
        #to display grouped patients
           for surname, patient_list in grouped_patients.items():
            print(f"Surname: {surname}")
            for patient in patient_list:
                print(f"{patient.full_name()} | Age: {patient.get_age()}  | Address: {patient.get_address()} | Postcode: {patient.get_postcode()} | Symptoms: {','.join(patient.get_symptoms())} | Allergies: {','.join(patient.get_allergies())}")
        else: 
           print("No patients to Display")
    
    def register_patient(self):
        """Register new patient"""
        #display table for all patients(existing + new)
        print("-----All patients-----")
        self.display_all_patients()
        
        #get details for new patient
        first_name = input("Enter patient's first name: ")
        surname = input("Enter patient's surname: ")
        age = input("Enter patient's age: ")
        mobile = input("Enter patient's mobile: ")
        address = input("Enter patient's address: ")
        postcode = input("Enter patient's postcode: ")
        symptoms = input("Enter patient's symptoms: ")
        allergies = input("Enter patient's allergies if they have any: ")
        
        
        #creating new patient object
        new_patient = Patient(first_name, surname, age, mobile, address, postcode, symptoms.split(','), allergies)
        
        #Adding this new patient to the existing patient's list
        self.patients.append(new_patient)
        
        print(f"{new_patient.full_name()} registered successfully.")
        
        #Display the updated table for all patients (existing + new)
        print("\n----Updated Patients----")
        self.display_all_patients()
        
        
    def update_patient(self):
        """Update patient details"""
        #table would display for all patients
        print("----All Patients----")
        self.display_all_patients()
        
        #get ID of patient to update
        patient_id = int(input("Enter the ID of patient to update: "))
        patient_to_update = next((patient for patient in self.patients if patient._id == patient_id), None)
            
        if patient_to_update:
          if isinstance(patient_to_update, Patient):
            #get details for updated patient
            first_name = input(f"Enter patient's new first name for {patient_to_update.full_name()}: ")
            surname = input(f"Enter patient's new surnamefor {patient_to_update.full_name()}: ")
            age = input(f"Enter patient's new age for {patient_to_update.full_name()}: ")
            mobile = input(f"Enter patient's new mobile for {patient_to_update.full_name()}: ")
            address = input(f"Enter patient's new address for {patient_to_update.full_name()}: ")
            postcode = input(f"Enter patient's new postcode for {patient_to_update.full_name()}: ")
            symptoms = input(f"Enter patient's new symptoms for {patient_to_update.full_name()}: ")
            allergies = input(f"Enter patient's new allergies for {patient_to_update.full_name()}: ")
            
            #updating patient's details
            
            
           
            patient_to_update._Patient__first_name = first_name
            patient_to_update._Patient__surname = surname
            patient_to_update._Patient__age = age
            patient_to_update._Patient__mobile = mobile
            patient_to_update._Patient__address = address
            patient_to_update._Patient__postcode = postcode
            patient_to_update._Patient__symptoms = symptoms
            patient_to_update._Patient__allergies = allergies
            
            print(f"{patient_to_update.full_name()} details updated successfully.")
            
            #display updated table for all patients
            print("\n---Updated Patients----")
            self.display_all_patients()
          else:
              print(f"Invalid patient object: {patient_to_update}")
        else:
            print(f"No patient found with ID {patient_id}.")
            
    def delete_patient(self):
        """Deleting patient"""
        #Display table for all patients
        print("-----All Patients----")
        self.display_all_patients()
        
        patient_id = input("Enter the ID of patient to delete: ")
        patient_to_delete = next((patient for patient in self.patients if patient._id == patient_id), None)
        
        if patient_to_delete:
            self.patients.remove(patient_to_delete)
            print(f"{patient_to_delete.full_name()} deleted successfully.")
            
            print("\n-----Updated Patients----")
            self.display_all_patients()
        else:
            print(f"no patient found with this ID {patient_id}.")
            
    def display_all_patients(self):
           print("ID | Full Name | Age | Mobile | Address | Postcode| Symptoms | Allergies")
           for patient in self.patients:
               symptoms =  ', '.join(patient.get_symptoms()) if patient.get_symptoms() else ''
               allergies = ', '.join(patient.get_allergies()) if patient.get_allergies() else ''   #this would join list with commas
              # allergies = ', '.join(allergies.split(', ')) #remove extra commas
               #symptoms = ', '.join(symptoms.split(', '))
               print(f"{patient.get_id()} | {patient.full_name()} | {patient.get_age()} | {patient.get_mobile()} | {patient.get_address()} | {patient.get_postcode()} | {symptoms} | {allergies}")
        
       
#-----------------------------------------------------------------        
        
        
    # storing and loading, all patient data from file
    
    def update_csv_file(new_patient_data):
        file_path = 'patient_data.csv'
        
       
       #reading existing patient data from csv file
        patient_data = pd.read_csv(file_path)
       
       #appending data
        patient_data = patient_data.append(new_patient_data, ignore_index=True )
       
       #write the updated DataFrame back to CSV file
        patient_data.to_csv(file_path, index = False)
        print("CSV file updated successfully with new patient data")
       
        new_patient_data = pd.DataFrame({
           'Index no': [1],
           'First name': ['Sara'],
           'Surname': ['Smith'],
           'Age': [20],
           'Mobile': [7012345678],
           'Address': ['Some Address 1'],
           'Postcode': ['B1 234'],
           'Symptoms': ['N/A'],
           'Allergies': ['N/A']
           
}) 
       #Call the function to update the csv file with new patient data
        
   # update_csv_file(new_patient_data)
#***********--------Shows error in above line saying, 'update_csv_file' is undefined
#-------------------------------------------------------------------        
      

#Relocating patient from one doctor to another  
import datetime
class Hospital: 
    def __init__(self, patients=None):
               self.patients = patients or []
               
    def relocate_patients(self, patient_name, new_doctor, reason, referring_doctor):
        print("Registred patients:")       
       # for patient in self.patients:
#            print(f"Name: {patient.get_first_name()}, Assigned Doctor: {patient.get_assigned_doctor()},
        for patient in self.patients:
                   if patient._Patient__assigned_doctor.lower() == patient_name.lower():#-!!!!--Patient' object has no attribute '_Patient__assigned_doctor'
                       patient._Patient__assigned_doctor = new_doctor
                       patient._Patient__relocating_reason = reason
                       patient._Patient__referring_doctor = referring_doctor
                       print(f"{patient_name} has been relocated to {new_doctor}")
                       self.display_patient_table()
                       return
        print(f"Patient {patient_name} not found in records.")
                  
    def display_patient_table(self): 
        print("---------Registered Patients-------")
        for patient in self.patients:
            print(f"Name: {patient._Patient__first_name()}, Assigned Doctor: {patient._Patient__assigned_doctor()}, Referring Doctor: {patient._Patient__referring_doctor()}")


                   
#-------------------------------------------------------------------        
               
        #admin requested management report and this following function would provide that report;
        
    def generate_management_report(self):
        #1. Total number of doctors in system
        total_doctors = len(self.doctors)
        current_month = datetime.datetime.now().month
        
        #2.Total number of patients per doctor
        patients_per_doctor = {}
        for doctor in self.doctors:
            patients_per_doctor[doctor.get_name()] = len([patient for patient in self.patients if patient.get_assigned_doctor() == doctor.get_name()])
            
          #3 total number of appointments per month
        appointments_per_doctor_per_month = {}
        for doctor in self.doctor:
              appointments_per_doctor_per_month[doctor.get_name()] = len([appointment for appointment in self.appointments if appointment.get_doctor() == doctor.get_name() and appointment.get_date().month == current_month ])
              
        #4 Total number of patients based on  illness type, lets assume, patients have illnes attribute
        patients_per_illness_type = {}
        for patient in self.patients:
            illness_type = patient.get_illness_type() 
            if illness_type in patients_per_illness_type:
                patients_per_illness_type[illness_type] += 1 
            else:
                patients_per_illness_type[illness_type]
                
        #displaying management report
        print("Management Report:")
        print(f"1. Total number of doctors in the system: {total_doctors}")
        print("2. Total number of patients per doctor:")
        for doctor, patient_count in patients_per_doctor.items():
            print(f"    -{doctor}: (patient_count) patients")
        print("3. Total number of appointments per month per doctor:")
        for doctor, appointment_count in appointments_per_doctor_per_month.items():
            print(f"    -{doctor}: (patient_count) appointments")
        print("4. Total number of patients based on illnes type:")
        for illness_type, patient_count in patients_per_illness_type.items():
            print(f"    -{illness_type}: (patient_count) patients")
   
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        