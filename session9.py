from datetime import date
from faker import Faker
from collections import namedtuple
from time import perf_counter

def check_length_0(input_list):
    """ Check if the length of list is empty or not """
	
    if len(input_list) > 0:
        return True
    else:
        return False

def fetch_profiles(num_profiles, dtype):
	
    """ create a list of fake profiles by using the Faker module and returns this list. """
	
    data_desc = ['job', 'company', 'ssn', 'residence', 'current_location', 'blood_group', 'website', 'username', 'name', 'sex', 'address', 'mail', 'birthdate','age'] 
    profiles = []
    fake = Faker()
    Faker.seed(0)

    if dtype == 'namedtuple':
        Data = namedtuple('Data', data_desc)
        Data.__doc__ = "Contains the person's profile "
        for _ in range(num_profiles):
            p = fake.profile()
            p['age'] = (date.today() - p['birthdate']).days
            profiles.append(Data(**p))

    elif dtype == 'dict':
        for _ in range(num_profiles):
            p = fake.profile()
            p['age'] = (date.today() - p['birthdate']).days
            profiles.append(p)

    return profiles

def largest_blood_group(profiles, dtype):
    """ Function to get the largest blood group type """
	
    if check_length_0(profiles):

        if dtype == 'namedtuple': 
            blood_groups = [i.blood_group for i in profiles ]
        elif dtype == 'dict':
            blood_groups = [i['blood_group'] for i in profiles ]
        else:
            return

        m = 0
        for i in set(blood_groups):
            x = blood_groups.count(i)
            if x>=m:
                m=x
                major = i
                    
        return major
    else:
        return "No profiles available"


def get_oldest_person_age(profiles,dtype):
    """ Function to get the age of the oldest person in days. """
	
    if check_length_0(profiles):
        
        if dtype == 'namedtuple': 
            m = 0
            for i in profiles:
                if i.age >m:
                    m=i.age
            return m
        elif dtype == 'dict': 
            m = 0
            for i in profiles:
                if i['age'] >m:
                    m=i['age']
            return m
    else:
        return "No profiles available"

def get_averge_age(profiles,dtype):
    """ Function to get the average age of all the people in the given list of profiles. """
	
    if check_length_0(profiles):
        if dtype == 'namedtuple':
            m = 0
            for i in profiles:
                m+=i.age
            return m/len(profiles)
        elif dtype == 'dict':
            m = 0
            for i in profiles:
                m+=i['age']
            return m/len(profiles)
    else:
        return "No profiles available"
		
def get_mean_current_location(profiles,dtype):
    """ Function to ge the mean current location. """
	
    if check_length_0(profiles):
        if dtype == 'namedtuple':
            x_tot = 0
            y_tot = 0
            a = []
            for i in profiles:
                x_tot+= i.current_location[0]
                y_tot+= i.current_location[1]

            return x_tot/len(profiles), y_tot/len(profiles)
        elif dtype == 'dict':
            x_tot = 0
            y_tot = 0
            a = []
            for i in profiles:
                x_tot+= i['current_location'][0]
                y_tot+= i['current_location'][1]

            return x_tot/len(profiles), y_tot/len(profiles)
    else:
        return "No profiles available"

def prove_namedtuple_faster():
    """ Function to prove that namedtuple executes faster than dictionary. """
	
    profiles = fetch_profiles(num_profiles=10,dtype='dict')
    s = perf_counter()
    print(get_mean_current_location(profiles,dtype='dict'))  
    e = perf_counter()
    print('Time taken by dictionary',e-s)
    profiles = fetch_profiles(num_profiles=10,dtype='namedtuple')
    s = perf_counter()
    print(largest_blood_group(profiles,dtype='namedtuple'))
    e = perf_counter()
    print('Time taken by namedtuple',e-s)
	
	
