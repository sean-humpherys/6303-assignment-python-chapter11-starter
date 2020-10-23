import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/questions"


"""
If you get an error of
    AttributeError: 'NoneType' object has no attribute 'getText'
the error means you spelled the class selector wrong
in .select() or .select_one()
soup cannot find any class with the wrong name.
Correct your spelling and try again.
"""

"""
Here are the URLs for page 2, 3, and 4. Notice a pattern?
https://stackoverflow.com/questions?tab=newest&page=2
https://stackoverflow.com/questions?tab=newest&page=3
https://stackoverflow.com/questions?tab=newest&page=4

We can build a loop to crawl through more pages.
"""
