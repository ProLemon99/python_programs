import requests

# Base URL for NASA's Astronomy Picture of the Day (APOD) API
API_URL = "https://api.nasa.gov/planetary/apod"
API_KEY = "6zgTgKqGhtuYk44fuYDLRhZLr7Ptpizmvr3GbyI2"  # Replace with your NASA API key

def fetch_apod(date=None):
    """Fetch NASA's Astronomy Picture of the Day (APOD)."""
    params = {"api_key": API_KEY}
    if date:
        params["date"] = date  # Format: YYYY-MM-DD
    
    response = requests.get(API_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return {
            "title": data.get("title", "Unknown"),
            "date": data.get("date", "Unknown"),
            "explanation": data.get("explanation", "No description available."),
            "image_url": data.get("url", "No image available")
        }
    else:
        print("Error fetching data from NASA API.")
        return None

def display_apod(apod_data):
    """Display APOD details."""
    if apod_data:
        print(f"Title: {apod_data['title']}")
        print(f"Date: {apod_data['date']}")
        print(f"Description: {apod_data['explanation'][:200]}...")
        print(f"Image URL: {apod_data['image_url']}")
    else:
        print("No data to display.")

def main():
    """Main function to run the NASA APOD application."""
    while True:
        print("\nNASA Astronomy Picture of the Day (APOD) Viewer")
        print("1. View today's APOD")
        print("2. View APOD for a specific date")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            # Fetch today's APOD
            apod_data = fetch_apod()
            display_apod(apod_data)
        elif choice == '2':
            # Fetch APOD for a specific date
            date = input("Enter the date (YYYY-MM-DD): ")
            apod_data = fetch_apod(date)
            display_apod(apod_data)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()