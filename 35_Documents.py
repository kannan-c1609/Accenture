"""
Documents
	The United Nations Organization released an official document regarding the most important events from the beginning of time (dated 00-00-0000) with a brief description of the events. The date of all the events is mentioned in the ‘DD-MM-YYYY’ format.
	Find the total number of distinct years referenced in the document.
	Input Specification:
	input1: String containing the content of the document
	Output Specification:
	Return the total number of distinct years referenced in the document.

"""
import re
def distinct_years(str):
	str2 = ""

	uniqueDates = set()
	pattern="[0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9]"
	dates = re.findall(pattern,str)
	for item in dates:
		uniqueDates.add(item.split('-')[-1])
	return len(uniqueDates)


if __name__ == "__main__":
    str = input()
    print(distinct_years(str))

