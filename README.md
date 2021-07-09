# Tuples

## Assigment

Use the Faker (Links to an external site.)library to get 10000 random profiles. Using namedtuple, calculate the largest blood type, mean-current_location, oldest_person_age, and average age (add proper doc-strings).
Do the same thing above using a dictionary. Prove that namedtuple is faster

## Functions

**check_length_0**

1. This function check if the given list is empty or not.
2. If the list is empty then it returns False else returns True

**fetch_profiles**
1. This function takes as arguments, the number of profiles which we want from Faker library and also the data type in which the profiles must be stored.
2. It returns a list of profiles

**largest_blood_group**
1. This function takes the profiles list and the type of each profile, as arguments.
2. It traverses through the profiles and stores the blood groups of all the profiles in a list.
3. Finally it get the blood group which is majority in the list and returns this blood group type as the result.

**get_oldest_person_age**
1. This function takes the profiles list and the type of each profile, as arguments.
2. It traverses through the profiles and tries to find the oldest age and returns this age as reasult.

**get_averge_age**
1. This function takes the profiles list and the type of each profile, as arguments.
2. The function calculates the average age of the profiles.


**get_mean_current_location**
1. This function takes the profiles list and the type of each profile, as arguments.
2. This function calculates the mean current_location using the current_location field in the profiles.
3. It finds the mean of the x and y coordinates available in the current_location field and returns it as result. 

**prove_namedtuple_faster**
1. This function shows that namedtuples execute faster than dictionaries.
