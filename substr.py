#write a function to find a substring within another string without using built-ins

def substring(string,substr):
	first_char = substr[0]
	for index in range(len(string)):
		if string[index] == first_char:
			found_index = index
			if check_substr(index+1, string, substr) == True:
				return found_index
	return False

def check_substr(index, string, substr):
	for j in range(1,len(substr)):
		if string[index] == substr[j]:
			index += 1
		else:
			return False
	return True

print substring('hi the there', 'there')
