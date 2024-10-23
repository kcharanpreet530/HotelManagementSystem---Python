# Imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient
from Admin import Hospital


def main():
    """
    the main function to be ran when the program runs
    """

    # Initialising the actors
   
    doctors = [Doctor('John','Smith','Internal Med.'),
               Doctor('Jone','Smith','Pediatrics'),
               Doctor('Jone','Carlos','Cardiology')]
    patients = [Patient('Sara','Smith', 20, '07012345678', 'Some Address 1', 'B1 234', 'Dr. John Smith'),
                Patient('Mike','Jones', 37,'07555551234','Some Address 1','L2 2AB', 'Dr Jone Smith'), 
                Patient('Daivd','Smith', 15, '07123456789', 'Some Address 1', 'C1 ABC', 'Dr Jone Carlos')]
    discharged_patients = []
    admin = Admin('admin','123','B1 1AB', patients) # username is 'admin', password is '123'
    
   
   # patients = [
       # {'name': 'John', 'assigned_doctor': 'Dr.Smith', 'relocating_reason': '', 'referral_doctor': '' },
        #{'name': 'Alice', 'assigned_doctor': 'Dr.Johnson', 'relocating_reason': '', 'referral_doctor': '' }
        #]
        
    
    hospital = Hospital(patients)#Initializing the hospital 

    # keep trying to login tell the login details are correct
    while True:
        if admin.login():
            running = True # allow the program to run
            break
        else:
            print('Incorrect username or password.')

    while running:
        # print the menu
        print('Choose the operation:')
        print(' 1. Register/View/Update/Delete doctor')
        print(' 2. Discharge patients')
        print(' 3. View discharged patient')
        print(' 4. Assign doctor to a patient')
        print(' 5. Update admin details')
        print(' 6. Review/Register/Update/Delete Patients')
        print('7. Relocate patient to another doctor')
        print('8. Quit')

        # get the option
        op = input('Option: ')

        if op == '1':
            # 1- Register/view/update/delete doctor
#ToDo1-------------------
            print("-----Doctor Management----")
            #doctor Management
            admin.doctor_management(doctors)

        elif op == '2':
            # 2- View or discharge patients
#ToDo2---------------
            admin.view_patient(patients)

            while True:
                op = input('Do you want to discharge a patient(Y/N):').lower()

                if op == 'yes' or op == 'y':
#ToDo3------------------
                    admin.discharge(patients, discharged_patients)

                elif op == 'no' or op == 'n':
                    break

                # unexpected entry
                else:
                    print('Please answer by yes or no.')
        
        elif op == '3':
            # 3 - view discharged patients
#ToDo4-----------------------
            admin.view_discharge(discharged_patients)

        elif op == '4':
            
            # 4- Assign doctor to a patient
            admin.assign_doctor_to_patient_with_symptoms(patients, doctors)
            
            #first_name = input("Enter patient's First name:- ")
            #surname = input("Enter patient's surname:- ")
            #age = input("Enter patient's age:- ")
            #mobile = input("Enter patient's mobile:- ")
            #postcode = input("Enter patient's postcode:- ")
            
            #getting symptoms from user
            #symptoms = input("Enter patient's symptoms (comma-separated): ").split(',')
            
            
            #admin.register_patient(first_name, surname, age, mobile, postcode, symptoms)
            
            
            
            
        elif op == '5':
            # 5- Update admin detais
            admin.update_details()
            
        elif op == '6':
            #6 - Review/Register/ Update /Delette patients
            admin.display_patient_menu()
            

        elif op == '7':
            patient_name = input("Enter the name of patient to relocate: ")
            new_doctor = input("Enter the name of new doctor: ")
            reason = input("Enter the reason for relocation: ")
            referring_doctor = input("Enter the referring doctor's name: ")
            hospital.relocate_patients(patient_name, new_doctor, reason, referring_doctor)
            
 
            
        elif op == '8':
            print("program Exits. GoodBye!")
            running = False #if running is set to false, the pogram will exit loop
            

        else:
            # the user did not enter an option that exists in the menu
            print('Invalid option. Try again')
            
    
        


if __name__ == '__main__':
    main()
