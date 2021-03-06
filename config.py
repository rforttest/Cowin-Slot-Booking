from datetime import timedelta, datetime
DATE = (datetime.today() + timedelta(1)).strftime("%d-%m-%Y")
LIMIT = 3 #otp retry limit
PINCODES = [324008] #list of pincodes by your preference.  
RATE = 3.5 #single api call per {RATE} second
REGISTERED_MOBILE_NUMBER = 123456789 # 10 digit mobile number in int 
DOSE = 1 #keep this value to 1 if you want to book fist dose adn to 2 for second do
VACCINE = 'COVISHIELD' #'COVISHIELD' or 'COVAXIN' in case of dose 2. for dose 1, it does not matter what is the vaccine type given here script will book whiever is available
Beneficiaries_Ids = { 
    '18':["",""],
    '45':[""]
} #beficiary ids in str format

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Type': 'application/json',
    'Origin': 'https://selfregistration.cowin.gov.in',
    'Connection': 'keep-alive',
    'Referer': 'https://selfregistration.cowin.gov.in/',
    'TE': 'Trailers',
}
