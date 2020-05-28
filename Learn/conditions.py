'''Learn conditions by conditions'''

TAX_RATE_USER_INPUT = input("what is your tax rate percentage? ")
TAX_RATE = float(TAX_RATE_USER_INPUT)
if TAX_RATE >= 30:
    print("You are the rich person")
elif (TAX_RATE >= 20) & (TAX_RATE > 30):
    print("You are the middle income person")
else:
    print("You are the lower income person")

# String comparision is case sensitive

# Are you from India?
COUNTRY_USER_INPUT = input("Which country you are from? ")
if COUNTRY_USER_INPUT.lower() == "india":
    print("You are from India")
else:
    print("You are not from India, you are from : {0}".format(COUNTRY_USER_INPUT.upper()))

# Are you from BRICS country?
if COUNTRY_USER_INPUT.lower() in ('india', \
                                'china', 'russia', 'brazil'):
    print("You are from BRICS group of country")
else:
    print("You are not part of BRICS country")

# Are you from NATA group countries
# or condition example
if COUNTRY_USER_INPUT.lower() == 'usa' or \
    COUNTRY_USER_INPUT.lower() == 'canada' or \
    COUNTRY_USER_INPUT.lower() == 'mexico':
    print("You are from NATA (North America Trade agreement) country")
else:
    print("You are not from NATA (North America Trade agreement) countries")

if COUNTRY_USER_INPUT.lower() == 'usa' and \
    TAX_RATE <= 30:
    if TAX_RATE <= 20:
        print("You are low income group person")
    else:
        print("You are middle income group person")
else:
    print("You are high income group person")
