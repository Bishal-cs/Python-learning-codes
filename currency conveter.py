# WAP to convert USD to INR 

def usd_to_inr(usd):
    inr = usd * 84 # The current price of $
    print(usd, "USD = ",inr, "INR")
 
usd = float(input("Enter the usd to convart: "))
usd_to_inr(usd)