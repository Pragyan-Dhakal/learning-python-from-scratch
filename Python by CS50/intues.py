import requests

# Ask the user to input the band name
search_term = input("Enter the band name to search for: ")

# Define the API endpoint, set limit to 10
url = f"https://itunes.apple.com/search?entity=song&limit=10&term={search_term}"

try:
    # Send the GET request to the API
    response = requests.get(url)
    response.raise_for_status()  # Check for HTTP errors

    # Parse the JSON response
    data = response.json()

    # Check if there are any results
    if data['resultCount'] > 0:
        # Loop through the results and print the song details
        print(f"\nFound {data['resultCount']} songs by '{search_term}':\n")
        for idx, song in enumerate(data['results'], 1):
            print(f"{idx}. Track Name: {song['trackName']}")
            print(f"   Artist: {song['artistName']}\n")
    else:
        print("No results found.")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
