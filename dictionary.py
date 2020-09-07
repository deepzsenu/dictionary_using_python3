import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def defination(word):
	word = word.lower()
	if word in data:
		return data[word]
	elif len(get_close_matches(word, data.keys())) >0:
		yn = input("did you mean %s instead ? Enter Y if yes and N if not : " % get_close_matches(word, data.keys())[0])

		print("\n\n")
		if yn ==  "Y" or yn == "y":
			return data[get_close_matches(word, data.keys())[0]]

		elif yn == "N" or yn == "n":
			return "the word did not found , please double check the word."

		else:
			return "sorry we didn't understand your Entery."
	else:
		return"data does not exist please cross check the word"

word1 = input("Enter the word : \n\t\t\t")
output = (defination(word1))

if type(output) == list:
	print("\tDEFINATION OF THE WORD IS\n")
	for item in output:		
		print("Means --}>  ", item,"\n")

else:
	print(output)

#this dictionary is created by Deepak Kumar Saxena 
