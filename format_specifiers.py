#FORMAT SPECIFERS = FORMAT THE VALUES BASED ON WHAT FLAGS ARE INSERTED

# .(number)f = round to that many decimal places (fixed point)
# :(number)  = allocate that many spaces 
# :03 = allocate 3 spaces, fill with 0s if not enough
# :< = left align
# :> = right align
# :^ = center align
# :, = add commas as thousands separators
# :% = percentage (multiply by 100 and add % sign)
# :b = binary
# :o = octal
# :x = hexadecimal
# :e = scientific notation (exponential)
# :g = general format (uses fixed point or scientific notation depending on the value)
# :s = string format (uses str() function)
# :c = character format (uses chr() function)
# :n = number format (uses locale settings for formatting)
# :d = decimal integer format (uses int() function)
# :f = fixed point format (uses float() function)
#---------------------------------------------------------------------------------------------------------------------------------


price1 = 62900.1234
price2 = -456.120
price3 = 65.012

print(f"price1 is ${price1:,.2f}")  # Fixed point with 2 decimal places (comma) divide the thousands 
print(f"price2 is ${price2:.2f}")  
print(f"price3 is ${price3:.2f}")  
