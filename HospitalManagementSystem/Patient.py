class Patient:
    """Patient class"""
    next_id = 1 

    def __init__(self, first_name, surname, age, mobile, address, postcode,assigned_doctor, symptoms=None, allergies=None):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            address (string): address
            postcode(string): postcode
            symptoms(list) : List of symptoms
            patients (list) : List of patients
            allergies(list) : List of allergies
        """
        self._id = Patient.next_id  #set the ID based on length of patients list
        Patient.next_id += 1

#ToDo1---------------
        self.__first_name = first_name
        self.__surname = surname
        self.__age = age
        self.__mobile = mobile
        self.__postcode = postcode
        self.__doctor = 'None' 
        self._address = address
        self.assigned_doctor = assigned_doctor
        self.__symptoms = symptoms or []
        self.__allergies = []
    #following two def are for, relocation of patient    
    def get_assigned_doctor(self):
        return self.__assigned_doctor
    
    def set_assigned_doctor(self, new_assigned_doctor):
        self.__assigned_doctor = new_assigned_doctor
        
    def display_patient_info(self):
        print(f"Name: {self._Patient__first_name}, Assigned Doctor: {self._Patient__assigned_doctor}, Referring Doctor: {self._Patient__referring_doctor}")
        
        
        
    
    def full_name(self) :
        """full name is first_name and surname"""
#ToDo2-----------
        return f'{self.__first_name} {self.__surname}'
    
    
    def get_surname(self):
        return self.__surname

    def get_doctor(self) :
#ToDo3------------
        return self.__doctor
    
    def get_age(self):
        return self.__age
    
    def get_mobile(self):
        return self.__mobile
    
    def get_postcode(self):
        return self.__postcode
    
    def get_address(self):
        return self._address
    
    def get_address_and_postcode(self):
        #Return a tuple containing address and postcode
        return self.__address, self.__postcode
    
    #adding method to get patient id
    def get_id(self):
        return self._id
    
    #adding another method to set patient id
    def set_id(self, patient_id):
        self._id = patient_id
        
    def add_symptoms(self, symptoms):
        if isinstance(symptoms, list): 
            self.__symptoms.extend(symptoms)
        else:
            self.__symptoms.append(symptoms)
            
    def add_allergies(self, allergies):
        if isinstance(allergies, list): 
            self.__symptoms.extend(allergies)
        else:
            self.__symptoms.append(allergies)
            
        
    def get_symptoms(self):
        return self.__symptoms
    
    def get_allergies(self):
        return self.__allergies
        
        
    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor

    def print_symptoms(self):
        """prints all the symptoms"""
 #ToDo4---------
        #lets assume, list of symptoms are stored in variable named, symptoms
        symptoms = ["symptom1", "symptom2", "symptom3"]
        
        print("symptoms:")
        for symptom in symptoms:
            print(f'- {symptom}')

    def __str__(self):
        return f'{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}'
