import textwrap

websiteText = '''
   Leaving can happen anywhere with our apps on your computer,
mobile device, and TV, featuring enhanced navigation and farstr
streaming for anytime leaving.'''

print('No Dedent:')
print(textwrap.fill(websiteText))

print('Dedent')
dedent_text = textwrap.dedent(websiteText).strip()
print(dedent_text)

print('Fill')
print(textwrap.fill(dedent_text, width=50))
print(textwrap.fill(dedent_text, width=100))

print('controlling Indent')
print(textwrap.fill(dedent_text, initial_indent='   '))
