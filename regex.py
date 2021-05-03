import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

#MetaCharacters (Need to be escaped):
#. ^ $ * + ? { } [ ] \ | ( )


#print('\tTAB')
#print(r'\tTab')

#pattern = re.compile(r'\d')
#pattern = re.compile(r'cba')
# pattern = re.compile(r'\D')
# pattern = re.compile(r'\w')
# pattern = re.compile(r'\W')
# pattern = re.compile(r'\s')
# pattern = re.compile(r'\S')

# ANCHORS de navegacion

#pattern = re.compile(r'\b')
#pattern = re.compile(r'\BHa')
#pattern = re.compile(r'^Start')
#pattern = re.compile(r'end$')
#pattern = re.compile(r'coreyms\.com')
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')



matches = pattern.finditer(text_to_search)


for match in matches:
    print(match)



