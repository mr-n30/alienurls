#!/usr/bin/python3
import time
import requests
import argparse

def main() -> None:
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Fetch URLs associated with a specified domain from the AlienVault API.")
    parser.add_argument(
        "--domain", "-d", 
        type=str, 
        required=True,
        help="The domain to fetch URLs for (e.g., 'example.com')."
    )
    parser.add_argument(
        "--sleep", "-s", 
        type=float, 
        default=1.0,
        help="Time in seconds to wait between API requests (default: 1.0)."
    )
    args = parser.parse_args()

    # Extract arguments
    domain = args.domain
    sleep_duration = args.sleep
    page = 1

    # Fetch URLs from the AlienVault API
    while True:
        r = requests.get(f"https://otx.alienvault.com/api/v1/indicators/domain/{domain}/url_list?limit=500&page={page}")
        urls = r.json().get("url_list")

        if not urls:
            break

        for url in urls:
            print(url.get("url", "").encode("utf-8", "ignore").decode())

        page += 1
        time.sleep(sleep_duration)

if __name__ == "__main__":
    main()
