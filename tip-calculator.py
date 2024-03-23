print('Welcome to the tip calculator!')

bill = float(input('What was the bill amount? $: '))
tip = int(input('How much tip would you like to give ? 10, 20 or 30? : '))
people = int(input('How many people to split the bill ? : '))

tip_as_percent = tip/100

total = bill + (bill * tip_as_percent)

bill_per_head = round(total / people, 2)

print(f'Everyone has to pay ${bill_per_head}')
