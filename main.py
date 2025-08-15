import requests
from colorama import Fore, Style
from platforms import PLATFORMS
import asyncio
import aiohttp
from colorama import Fore, Style


PLATFORMS = {
    "Facebook": "https://www.facebook.com/{}",
    "GitHub": "https://github.com/{}",
    "Instagram": "https://www.instagram.com/{}",
    "Twitter": "https://twitter.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
}

def generate_variations(name):
    base = name.strip()
    no_space = base.replace(" ", "")
    underscore = base.replace(" ", "_")
    dash = base.replace(" ", "-")
    dot = base.replace(" ", ".")

    variations = {
        no_space,
        underscore,
        dash,
        dot,
        f"{no_space}_",
        f"_{no_space}",
        f"{no_space}123",
        f"{no_space}_123",
        f"{no_space}_official",
    }

    return list(variations)

async def check_username(session, platform, url_pattern, username):
    url = url_pattern.format(username)
    try:
        async with session.get(url, timeout=5) as resp:
            if resp.status == 200:
                return platform, username, "FOUND", url
            elif resp.status == 404:
                return platform, username, "NOT FOUND", None
            else:
                return platform, username, f"ERROR {resp.status}", None
    except asyncio.TimeoutError:
        return platform, username, "TIMEOUT", None
    except Exception:
        return platform, username, "ERROR", None

async def main():
    base_name = input("Enter username to check: ").strip()
    use_variations = input("Do you want to check variations? (y/n): ").strip().lower()

    if use_variations == "y":
        usernames_to_check = generate_variations(base_name)
    else:
        usernames_to_check = [base_name]

    async with aiohttp.ClientSession() as session:
        tasks = [
            check_username(session, platform, url_pattern, username)
            for username in usernames_to_check
            for platform, url_pattern in PLATFORMS.items()
        ]
        results = await asyncio.gather(*tasks)

    print("\n=== Username Check Results ===\n")
    for platform, username, status, link in results:
        if status == "FOUND":
            print(f"{Fore.GREEN}{platform:<12} {username:<15} {status:<10} {link}{Style.RESET_ALL}")
        elif status == "NOT FOUND":
            print(f"{Fore.RED}{platform:<12} {username:<15} {status:<10}{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}{platform:<12} {username:<15} {status:<10}{Style.RESET_ALL}")

if __name__ == "__main__":
    asyncio.run(main())