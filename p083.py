import sys

def maxBeauty(string):
	lowerCaseString = string.lower()
	characterToFrequencyMap = {}

	for character in lowerCaseString:
		if character.islower() and character not in characterToFrequencyMap:
			characterToFrequencyMap[character] = lowerCaseString.count(character)

	frequencies = list(characterToFrequencyMap.values())
	frequencies.sort()
	numFrequencies = len(frequencies)
	beauty = 0

	for i, frequency in enumerate(frequencies):
		beauty += (26 - (numFrequencies - i - 1)) * frequency

	return beauty

for line in open(sys.argv[1]):
	print(maxBeauty(line))

'''
aabbccc
2 2 3

3 * 26
2 * 25
2 * 24
'''