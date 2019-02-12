EXTRA_SPACES = 4

f = open('/home/shani/RnD/github_conv/confluence-to-markdown/RnD/_Adding_an_API_State_Change_Workflow_.md', 'r')
lines = f.readlines()
f.close()


isFomattingOn = False
leadingSpaces = 0

terms =["!!! tip", "!!! warning", "!!! info"]

for term in terms:
	for id, currentLine in enumerate(lines):

	    if term in currentLine:
		isFomattingOn = False
		leadingSpaces = 0
	 
	    if "TEST" in currentLine:
		isFomattingOn = False
		leadingSpaces = 0

	    if isFomattingOn:
		currentLine  = currentLine.lstrip()
		currentLine = currentLine.rjust(leadingSpaces + EXTRA_SPACES + len(currentLine))

	    if term in currentLine:
		isFomattingOn = True
		leadingSpaces = len(currentLine) - len(currentLine.lstrip())

	    lines[id] = currentLine

with open("converted_formatted.md", "wb") as file:
    for item in lines:
        if ("TEST" not in item): 
                 file.write("%s" % item)

print ('Formatting done!')
