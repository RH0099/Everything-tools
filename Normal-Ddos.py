import requests
from concurrent.futures import ThreadPoolExecutor

# Function to send a request
def send_request(url):
    try:
        response = requests.get(url)
        print(f"Response code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

# URL to test
url = 'https://yourwebsite.com'

# Number of concurrent requests
num_requests = 100

# Create a ThreadPoolExecutor to send requests concurrently
with ThreadPoolExecutor(max_workers=num_requests) as executor:
    futures = [executor.submit(send_request, url) for _ in range(num_requests)]

    # Wait for all futures to complete
    for future in futures:
        future.result()

print("Load test completed.")
