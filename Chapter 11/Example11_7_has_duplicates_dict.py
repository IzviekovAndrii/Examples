import Example11_5_invert_dict

def has_duplicates_dic(d):
	'''Use a dictionary to write a faster, simpler version of has_duplicates from Example10.7 
	(that takes a list as a parameter and returns True if there is any object 
	that appears more than once in the list.)'''
	for key in d:
		value = d[key]
		if len(value) > 1:
			return True
		else:
			return False


if __name__ == '__main__':	
	d = {'name_work':'andrey', 'name_friend':'andrey', 'name_home':'andrusha', 'name_face':'andrii'}
	d1 = {1:'name', 2:'last_name', 3:'phone', 4:'mail', 5:'skype', 6:'adress', 7:'work', 8:'age', 9:'education'}	
	inv_d = Example11_5_invert_dict.invert_dict(d)
	inv_d1 = Example11_5_invert_dict.invert_dict(d1)
	print(d)
	print(inv_d)
	print(has_duplicates_dic(inv_d))
	print()
	print(d1)
	print(inv_d1)
	print(has_duplicates_dic(inv_d1))
