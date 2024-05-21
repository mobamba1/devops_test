import requests

# Define the URL
primary_url = "https://api.punkapi.com/v2/beers"
fallback_url = "https://s3-eu-west-1.amazonaws.com/kg-it/devopsTest/api-punkapi-com-v2-beers.json"

def fetch_beers(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise status if unsuccessful 
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None

def main():
    # Fetch from the primary API
    beers = fetch_beers(primary_url)
    
    # Fetch fallback URL
    if beers is None:
        print("Primary API failed. Fetching from the secondary URL.")
        beers = fetch_beers(fallback_url)
    
    # If both fails, program exits
    if beers is None:
        print("Failed to fetch data from both URLs")
        return
    
    # Prints out the results 
    for beer in beers:
        name = beer.get('name', 'number')
        abv = beer.get('abv', 'number')
        print(f"{name},{abv}")

if __name__ == "__main__":
    main()
