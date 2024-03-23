year = int(input('Which year do you wanna check? '))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print('Leap year')
    else:
      print('Not Leap year')
  else:
    print('Lear year')

else:
  print('Not Leap year')
    
