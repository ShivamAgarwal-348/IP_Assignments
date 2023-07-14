# Assignment - 2
# Name - Shivam Agarwal
# Roll No - 2020123

import json


'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- DO NOT modify/delete the given functions. 

- DO NOT import any python libraries, except for the ones already included.

- DO NOT create any global variables in this module.

- DO NOT add print statements anywhere in this module.

- Make sure to return value as specified in the function description.

- Remove the pass statement from the functions when you implement them.
'''


def read_data_from_file(file_path="data.json"):
	'''
	**** DO NOT modify this function ****
	Description: Reads the data.json file, and converts it into a dictionary.

	Parameters: 
	- file_path (STRING): The path to the file (with .json extension) which contains the initial database. You can pass the file_path parameter as "data.json".

	Returns:
	- A dictionary containing the data read from the file
	'''
	
	with open(file_path, 'r') as data:
		records = json.load(data)

	return records


def filter_by_first_name(records, first_name):
	'''
	Description: Searches the records to find all persons with the given first name (case-insensitive)

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- first_name (STRING): The first name

	Returns:
	-  A list of INTEGERS denoting the IDs of thepersons with the given first name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	'''
	n = len(records)
	firstname_ids = []
	for i in range(n):
		if (records[i]['first_name'].lower() == first_name.lower()):
			firstname_ids.append(records[i]['id'])
	return firstname_ids
	

def filter_by_last_name(records, last_name):
	'''
	Description: Searches the records to find all persons with the given last name (case-insensitive)

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- last_name (STRING): The last name

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given last name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	'''
	n = len(records)
	lastname_ids = []
	for i in range(n):
		if (records[i]['last_name'].lower() == last_name.lower()):
			lastname_ids.append(records[i]['id'])
	return lastname_ids
	

def filter_by_full_name(records, full_name):
	'''
	Description: Searches the records to find all persons with the given full name (case-insensitive)

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- full_name (STRING): The full name (a single string with 2 space-separated words, the first name and the last name respectively)

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given full name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	'''
	n = len(records)
	fullname_ids = []
	first_name,last_name = full_name.split()
	
	for i in range(n):
		if (records[i]['first_name'].lower() == first_name.lower()):
			if (records[i]['last_name'].lower() == last_name.lower()):
				fullname_ids.append(records[i]['id'])
			
	return fullname_ids
	


def filter_by_age_range(records, min_age, max_age):
	'''
	Description: Searches the records to find all persons whose age lies in the given age range [min_age, max_age]

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- min_age (INTEGER): The minimum age (inclusive)
	- max_age (INTEGER): The maximum age (inclusive)

	Note: 0 < min_age <= max_age

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given full name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	'''
	n = len(records)
	age_ids = []

	for i in range(n):
		if (records[i]['age'] >= min_age and records[i]['age']<=max_age):
			age_ids.append(records[i]['id'])
	return age_ids


def count_by_gender(records):
	'''
	Description: Counts the number of males and females

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)

	Returns:
	- A dictionary with the following two key-value pairs:
		KEY        VALUE
		"male"     No of males (INTEGER)
		"female"   No of females (INTEGER)
	'''
	n = len(records)
	gender = {'male' : 0 , 'female' : 0}

	for i in range(n):
		if (records[i]['gender'].lower() == 'male' ):
			gender['male'] += 1
		else :
			gender['female'] += 1
	return gender


def filter_by_address(records, address):
	'''
	Description: Filters the person records whose address matches the given address. 

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- address (DICTIONARY): The keys are a subset of { "house_no", "block", "town", "city", "state", "pincode" } (case-insensitive)
		Some examples are:
			Case 1: {} 
				=> All records match this case
			
			Case 2: { "block": "AD", "city": "Delhi" } 
				=> All records where the block is "AD" and the city is "Delhi" (the remaining address fields can be anything)
			
			Case 3: { "house_no": 24, "block": "ABC", "town": "Vaishali", "city": "Ghaziabad", "state": "Uttar Pradesh", "pincode": 110020 }

	Returns:
	- A LIST of DICTIONARIES with the following two key-value pairs:
		KEY            VALUE
		"first_name"   first name (STRING)
		"last_name"    last name (STRING)
	'''
	n = len(records)
	names = []
	flag = True
	for i in range(n):
		flag = True
		if(len(address)==0):
			flag = True
		else:
			for j in address:
				if(str(address[j]).lower() != str(records[i]['address'][j]).lower()):
					flag = False
					break
		if(flag):
			names.append({'first_name':records[i]['first_name'],'last_name':records[i]['last_name']})
	return names


def find_alumni(records, institute_name):
	'''
	Description: Find all the alumni of the given institute name (case-insensitive). 
	
	Note: A person is an alumnus of an institute only if the value of the "ongoing" field for that particular institute is False.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- institute_name (STRING): Name of the institute (case-insensitive)

	Returns:
	- A LIST of DICTIONARIES with the following three key-value pairs:
		KEY            VALUE
		"first_name"   first name (STRING)
		"last_name"    last name (STRING)
		"percentage"   percentage (FLOAT)
	'''
	n = len(records)
	names = []
	ids = []
	for i in range(n):
				
		for j in range(len(records[i]['education'])-1,-1,-1):

			if(institute_name.lower() == records[i]['education'][j]['institute'].lower()):
				if(records[i]['education'][j]['ongoing']==False):	
					if i not in ids:
						ids.append(i)
						names.append({'first_name':records[i]['first_name'],'last_name':records[i]['last_name'],'percentage':records[i]['education'][j]['percentage']})

	return names


def find_topper_of_each_institute(records):
	'''
	Description: Find topper of each institute

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)

	Returns:
	- A DICTIONARY with the institute name (STRING) as the keys and the ID (INTEGER) of the topper of that institute.

	Note: If there are `N` distinct institutes in records, the dictionary will contain `N` key-value pairs. The ongoing status does NOT matter. It is guaranteed that each institute will have exactly one topper.
	'''
	n = len(records)
	toppers = {}
	names = {}

	for i in range(n):
		
		institutes = []
		
		for j in range(len(records[i]['education'])-1,-1,-1):

			if records[i]['education'][j]['institute'].lower() not in names:
				if(records[i]['education'][j]['ongoing']==False):	
					institutes.append(records[i]['education'][j]['institute'].lower())	
					names[records[i]['education'][j]['institute'].lower()] = [records[i]['id'],records[i]['education'][j]['percentage']]

			else: 
				if(records[i]['education'][j]['ongoing']==False):	
					if records[i]['education'][j]['institute'].lower() not in institutes:
						institutes.append(records[i]['education'][j]['institute'].lower())
						if(records[i]['education'][j]['percentage'] > names[records[i]['education'][j]['institute'].lower()][1]):
							
							names[records[i]['education'][j]['institute'].lower()] = [records[i]['id'],records[i]['education'][j]['percentage']]

	for k in names:
		toppers[k.upper()] = names[k][0]

	return toppers


def find_blood_donors(records, receiver_person_id):
	'''
	Description: Find all donors who can donate blood to the person with the given receiver ID.

		Note: 
		- Possible blood groups are "A", "B", "AB" and "O".

		Rules:
		BLOOD GROUP      CAN DONATE TO
		A                A, AB
		B                B, AB
		AB               AB
		O                A, B, AB, O

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- receiver_person_id (INTEGER): The ID of the donee
		Note: It is guaranteed that exactly one person in records will have the ID as receiver_person_id

	Returns:
	- A DICTIONARY with keys as the IDs of potential donors and values as a list of strings, denoting the contact numbers of the donor
	'''
	n = len(records)
	recievefrom = {'A':['A','O'],'B':['B','O'],'AB':['A','B','AB','O'],'O':['O']}
	donors = {}
	blood_donee = ''
	for i in range(n):
		if (records[i]['id'] == receiver_person_id):
			blood_donee = records[i]['blood_group']
			break
	for i in range(n):
		if (records[i]['id'] != receiver_person_id):
			if records[i]['blood_group'].upper() in recievefrom[blood_donee.upper()] :
				donors[records[i]['id']] = records[i]['contacts']
	
	return donors


def get_common_friends(records, list_of_ids):
	'''
	Description: Find the common friends of all the people with the given IDs

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- list_of_ids (LIST): A list of IDs (INTEGER) of all the people whose common friends are to be found

	Returns:
	- A LIST of INTEGERS containing the IDs of all the common friends of the specified list of people
	'''
	n = len(records)
	all_friends = []
	
	for j in range(len(list_of_ids)):	
		for i in range(n):
			if(records[i]['id'] == list_of_ids[j]):
				all_friends.append(records[i]['friend_ids'])
	
	common_friends = all_friends[0]
	not_common = []
	for i in range(len(common_friends)):
		for j in range(len(all_friends)):	
			
			if common_friends[i] not in all_friends[j]:
				not_common += [common_friends[i]]
				break
	for i in not_common:
		common_friends.remove(i)

	return common_friends	



def is_related(records, person_id_1, person_id_2):
	'''
	**** BONUS QUESTION ****
	Description: Check if 2 persons are friends

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id_1 (INTEGER): first person ID
	- person_id_2 (INTEGER): second person ID

	Returns:
	- A BOOLEAN denoting if the persons are friends of each other, directly or indirectly (if A knows B, B knows C and C knows D, then A knows B, C and D).
	'''
	n = len(records)
	if(person_id_1 == person_id_2):
		return False
		
	for i in range(n):
		if(records[i]['id'] == person_id_1):
			friends = records[i]['friend_ids']

	new_friends = False

	if person_id_2 in friends : 
		return True
	else : 
		while True : 
			new_friends = False
			for i in range(n):
			
				if records[i]['id'] in friends:
					for j in records[i]['friend_ids'] :
						if j not in friends :
							friends.append(j)
							new_friends = True
			
			if person_id_2 in friends:
				return True
			elif (new_friends == False):
				return False
				
						 



def delete_by_id(records, person_id):
	'''
	Description: Given a person ID, this function deletes them from the records. Note that the given person can also be a friend of any other person(s), so also delete the given person ID from other persons friend list. If the person ID is not available in the records, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	
	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	'''
	n = len(records)
	friends = []
	for i in range(n):
		if(records[i]['id'] == person_id):
			friends = records[i]['friend_ids']
			del records[i]
			break

	n = len(records)
	temp = []
	for i in range(n):
		if records[i]['id'] in friends :
			temp = []
			for j in records[i]['friend_ids']:
				if (j != person_id):
					temp.append(j)
			records[i]['friend_ids'] = temp
			

	return records		


def add_friend(records, person_id, friend_id):
	'''
	Description: Given a person ID and a friend ID, this function makes them friends of each other. If any of the IDs are not available, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	- friend_id (INTEGER): The friend id
	
	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	'''
	n = len(records)
	flag = [False,False]

	if(person_id == friend_id):
		return records

	for i in range(n):
		if (records[i]['id'] == person_id):
			flag[0] = True
		if (records[i]['id'] == friend_id):
			flag[1] = True
	
	if flag[0]:
		if flag[1]:
			for i in range(n):
				if records[i]['id'] == person_id :
					if friend_id not in records[i]['friend_ids']:
						records[i]['friend_ids'].append(friend_id)
					
				if records[i]['id'] == friend_id:
					if person_id not in records[i]['friend_ids']:
						records[i]['friend_ids'].append(person_id)					
				
	
	return records


def remove_friend(records, person_id, friend_id):
	'''
	Description: Given a person ID and a friend ID, this function removes them as friends of each other. If any of the IDs are not available, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	- friend_id (INTEGER): The friend id
	
	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	'''
	n = len(records)
	flag = [False,False]

	if(person_id == friend_id):
		return records

	for i in range(n):
		if (records[i]['id'] == person_id):
			flag[0] = True
		if (records[i]['id'] == friend_id):
			flag[1] = True
	
	if flag[0]:
		if flag[1]:
			for i in range(n):
				if records[i]['id'] == person_id :
					if friend_id in records[i]['friend_ids']:
						records[i]['friend_ids'].remove(friend_id)
					
				if records[i]['id'] == friend_id:
					if person_id in records[i]['friend_ids']:
						records[i]['friend_ids'].remove(person_id)					
				
	
	return records


def add_education(records, person_id, institute_name, ongoing, percentage):
	'''
	Description: Adds an education record for the person with the given person ID. The education record constitutes of insitute name, the person's percentage and if that education is currently ongoing or not. Please look at the format of an education field from the PDF. If the person ID is not available in the records, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	- institute_name (STRING): The institute name (case-insensitive)
	- ongoing (BOOLEAN): The ongoing value representing if the education is currently ongoing or not
	- percentage (FLOAT): The person's score in percentage

	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	'''
	n = len(records)


	for i in range(n):
		if(records[i]['id'] == person_id):
			if(ongoing == True):
				records[i]['education'].append({'institute' : institute_name , 'ongoing' : ongoing})
			else :
				records[i]['education'].append({'institute' : institute_name , 'ongoing' : ongoing , 'percentage' : percentage})
	return records	
