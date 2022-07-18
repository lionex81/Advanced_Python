import re


print("____________Task 1________________")
patt = r'\d\d\d\D\d\d\D\d\d'
text_1 = r"""
        Hello, my phone number is 251-65-23.
        """
text_2 = r"""
        Henry Ford was born July 30, 1863, on a farm in Springwells Township, Michigan.
        """
match = re.search(patt, text_1)
print(match[0] if match else 'Not found')

match = re.search(patt, text_2)
print(match[0] if match else 'Not found')


print("____________Task 2________________")
patt = r"[a-zA-Z0-9_\.]{1,255}@[^\.][a-zA-Z0-9_\.]{1,255}[^\.\b ]"
text = r"""
        I have next e-mail: lex_@google.com lex22_@.e_mail.com lex_@ua_.com  hffh@.jfjhf
        """
res = re.findall(pattern=patt, string=text)
print(res)

print("____________Task 3________________")
patt = r"\.0{1,2}"
text = r"216.008.094.196"
res = re.sub(pattern=patt, repl=".", string=text)
print(res)


print("____________Task 4________________")
patt = r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"
ip_adress = ["216.8.94.196", "0.0.0.0", "127.0.0.1", "216.8.94", "14.0..139", "153.192.392.84"]
for ip_adr in ip_adress:
    if len(re.findall(pattern=patt, string=ip_adr)) == 0:
        print(f"IP address {ip_adr} is invalid")
    else:
        str_ip_adr = re.split(r'\.+', ip_adr)
        if int(str_ip_adr[0]) < 256 and int(str_ip_adr[1]) < 256 and\
                int(str_ip_adr[2]) < 256 and int(str_ip_adr[3]) < 256:
            print(f"IP address {ip_adr} is valid")
        else:
            print(f"IP address {ip_adr} is invalid")

