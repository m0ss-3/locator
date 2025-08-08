from countryinfo import CountryInfo

def get_currency(country_name):
    try:
        country = CountryInfo(country_name)
        currency = country.currencies()[0]  
        return f"The currency for {country_name} is {currency}"
    except Exception as e:
        return f"Unable to find currency for '{country_name}': {e}"

country_input = input("Enter the full country name: ")
print(get_currency(country_input))
