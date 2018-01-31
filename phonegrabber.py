import pyperclip
import re


phoneRegex = re.compile(r'''(
    (\+\d|\d{1,4})+  
    (\s|-|\.)+                 # Separator
    (\(\d{3}\))+
    (\s|-|\.)+
    (\d{3})+
    (\s|-|\.)+
    (\d{2})+
    (\s|-|\.)+
    (\d{2})+
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9.%_]+        # FIRST PART OF EMAIL
    @
    [a-zA-Z0-9.]+             # Domain name
    (\.[a-zA-Z]{2,4})
    )''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    matches.append(groups[0])
for groups in emailRegex.findall(text):
    matches.append(groups[0])
if len(matches) > 0:
    print(matches)
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard')
    print(pyperclip.paste())
    # print('\n'.join(matches))
else:
    print('Nothing found')