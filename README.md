# locator.py

**country currency and postal code lookup**
- a simple python tool for looking up a country's currency and finding the postal (zip) codes from full addresses.
- this combines countryinfo for currency identification and geopy's Nominatim for reverse postal code lookups.
- quickly retrieve key geographic info with minimal input

**key features**
- country currency lookup -> instantly find the official currency of an country by name.
- postal code finder -> retrieve postal (zip) codes from full address input, acting as an inverse zip code finder

**installation**
- clone the repository -> "git clone https://github.com/m0ss-3/locator.py.git cd locator.py

**install dependencies**
- "pip3 install -r requirements.txt"

**example**
- $ python3 countries.py "Canada"
  -> Currency: CAD

- $ python3 zip.py "1600 Amphitheatre Parkway, Mountain View, CA"
    -> Postal Code: 94043

