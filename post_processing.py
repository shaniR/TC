EXTRA_SPACES = 4

f = open('/home/shani/RnD/github_conv/confluence-to-markdown/RnD/_Adding_a_New_API_Store_Theme_.md', 'r')
lines = f.readlines()
f.close()

isFomattingOn = False
leadingSpaces = 0

toFormat = False
toFormatPrevious = False

terms = ["!!! tip", "!!! warning", "!!! info", "!!! note"]

for term in terms:
    for id, currentLine in enumerate(lines):

        if(terms.index(term) == 0):
        	if (currentLine.rstrip().lstrip() == "```"):
        		leadingSpaces = leadingSpaces - 4
        		toFormat = toFormatPrevious
                        toFormat = True
        		if(toFormat):
            			leadingSpaces = 0
       
        if term in currentLine:
            toFormat = True
            EXTRA_SPACES = 0
            leadingSpaces = len(currentLine) - len(currentLine.lstrip())
            if(leadingSpaces == 0):
                leadingSpaces = 4 
            continue
            # isFomattingOn = False
            # leadingSpaces = 0

        if toFormat:
            # currentLine  = currentLine.lstrip()
            currentLine = currentLine.rjust(leadingSpaces + EXTRA_SPACES + len(currentLine))
            if("TEST" in currentLine):
                toFormat = False
                EXTRA_SPACES = 0
                leadingSpaces = 0

	if(terms.index(term) == 0):
		if "``` " in currentLine:
       			leadingSpaces = len(currentLine) - len(currentLine.lstrip())
       			toFormatPrevious = toFormat

        lines[id] = currentLine

for id, currentLine in enumerate(lines):
    

    lines[id] = currentLine

with open("converted_formatted.md", "wb") as file:
    for item in lines:
        if ("TEST" not in item):
            file.write("%s" % item)

print ('Formatting done!')
