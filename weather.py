import os
from langchin_community.utilities import OpenweatherMapAPIWRapper
os.environ["open_WEATHERMAP_API_KEY"]=" 1507f0a1b84feab8b66e61ef64cbd06e "
weather=OpenweatherMapAPIWRapper()
result=weather.run("kanyakumari")
print(result)