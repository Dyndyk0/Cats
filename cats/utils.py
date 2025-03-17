import requests

def get_random_cats(num_cats=10):
    api_key = CAT_API_KEY
    if not api_key:
        raise ValueError("CAT_API_KEY is not set in environment variables.")

    url = f'https://api.thecatapi.com/v1/images/search?limit={num_cats}&api_key={api_key}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching cats from API: {e}")
        return []

def get_random_dogs(num_dogs=5):
    api_key = DOG_API_KEY
    if not api_key:
        raise ValueError("DOG_API_KEY is not set in environment variables.")

    url = f'https://api.thedogapi.com/v1/images/search?limit={num_dogs}&api_key={api_key}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching cats from API: {e}")
        return []