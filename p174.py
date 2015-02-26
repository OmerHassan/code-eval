import sys

SLANGS = (
	', yeah!',
	', this is crazy, I tell ya.',
	', can U believe this?',
	', eh?',
	', aw yea.',
	', yo.',
	'? No way!',
	'. Awesome!'
)

SENTENCE_END_CHARACTERS = ('.', '!', '?')

text = open(sys.argv[1]).read()
output = ''
wasPreviousMatchReplaced = True
slangIndex = 0
lastSlangIndex = len(SLANGS) - 1

for character in text:
	if character in SENTENCE_END_CHARACTERS:
		if wasPreviousMatchReplaced:
			output += character
			wasPreviousMatchReplaced = False
		else:
			output += SLANGS[slangIndex]
			wasPreviousMatchReplaced = True
			slangIndex += 1

			if slangIndex > lastSlangIndex:
				slangIndex = 0
	else:
		output += character

print(output)