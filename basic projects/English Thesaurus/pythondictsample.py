import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches


sqmatch=SequenceMatcher(None, "rainn", "rain").ratio()
print("sequenceaMatchRatio: ", sqmatch)
closematch=get_close_matches("rainn", ["help", "pyramid", "rain"])
print("closeMatch: ", closematch)

data = json.load(open("data.json"))

closematch1=get_close_matches("rainn",data.keys())
print(closematch1)
closematch2=get_close_matches("rainn",data.keys(), n=5)
print(closematch2)


def translate(w):
	w = w.lower()
	if w in data:
		return data[w]
	elif len(get_close_matches(w, data.keys())) > 0:
		yn=input( "Did you mean %s instead? Enter (y/n): " % get_close_matches(w, data.keys())[0])
		if yn == "y":
			return data[get_close_matches(w, data.keys())[0]]
		elif yn == "n":
			return "The word doesn,t exist."
		else :
			return "Didn't Understand your entry."
	else:
		return "Not Exist the word try again."
		
word = input("Enter word: ")

print(translate(word))





