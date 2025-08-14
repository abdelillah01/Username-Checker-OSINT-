import requests
from colorama import Fore, Style
from platforms import PLATFORMS

def check_username(username):
    results = []
    for platform, url_pattern in PLATFORMS.items():
        url = url_pattern.format(username)
        try:
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                results.append((platform, "FOUND", url))
            elif r.status_code == 404:
                results.append((platform, "NOT FOUND", None))
            else:
                results.append((platform, f"ERROR {r.status_code}", None))
        except requests.RequestException as e:
            results.append((platform, "ERROR", None))
    return results

if __name__ == "__main__":
    user = input("Enter username to check: ").strip()
    data = check_username(user)

    print("\n=== Username Check Results ===\n")
    for platform, status, link in data:
        if status == "FOUND":
            print(f"{Fore.GREEN}{platform:<12} {status:<10} {link}{Style.RESET_ALL}")
        elif status == "NOT FOUND":
            print(f"{Fore.RED}{platform:<12} {status:<10}{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}{platform:<12} {status:<10}{Style.RESET_ALL}")