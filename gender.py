#Gender

male = 'M'
female = 'F'
other = 'O'

gender = 'X'

while gender != 'M' and gender != 'F' and gender != 'O':
	gender = str(input('Enter your gender, M for male, F for female or O for other:\n')).strip().upper()
	
	if gender != 'M' and gender != 'F' and gender != 'O':
		print('Invalid option, try again!')
	
if gender == 'M':
	print('Gender: Male registered')

elif gender == 'F':
	print('Gender: Female registered')
	
else:
	print('Gender: Other registered')
	