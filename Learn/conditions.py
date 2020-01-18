# Learn conditions

tax_rate_user_input = input("what is your tax rate percentage? ")
tax_rate = float(tax_rate_user_input)
if 30 <= tax_rate:
    print("You are the rich person")
elif (20 <= tax_rate) & (30 > tax_rate):
    print("You are the middle income person")
else:
    print("You are the lower income person")

# String comparision is case sensitive

# Are you from India?
country_user_input = input("Which country you are from? ")
if country_user_input.lower() == "india":
    print("You are from India")
else:
    print("You are not from India, you are from : {0}".format(country_user_input.upper()))

# Are you from BRICS country?
if country_user_input.lower() in ('india', \
                                'china', 'russia', 'brazil'):
    print("You are from BRICS group of country")
else:
    print ("You are not part of BRICS country")

# Are you from NATA group countries
# or condition example
if country_user_input.lower() == 'usa' or \
    country_user_input.lower() == 'canada' or \
    country_user_input.lower() == 'mexico':
    print("You are from NATA (North America Trade agreement) country")
else:
    print("You are not from NATA (North America Trade agreement) countries")

if country_user_input.lower() == 'usa' and \
    tax_rate <= 30:
    if(tax_rate <= 20):
        print("You are low income group person")
    else:
        print("You are middle income group person")
else:
    print("You are high income group person")