import pyshorteners

# Get the targetted URL from the user
long_url = input("Pleas enter your long URL: ")

# Shortening the URL using pyshorteners
s = pyshorteners.Shortener()
short_url = s.tinyurl.short(long_url)

print(short_url)
