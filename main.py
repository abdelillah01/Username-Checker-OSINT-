import requests
from colorama import Fore, Style
from platforms import PLATFORMS
import asyncio
import aiohttp
from colorama import Fore, Style



async def check_username(session, platform, url_pattern, username):
    url = url_pattern.format(username)
    try:
        async with session.get(url, timeout=5) as resp:
            if resp.status == 200:
                return platform, "FOUND", url
            elif resp.status == 404:
                return platform, "NOT FOUND", None
            else:
                return platform, f"ERROR {resp.status}", None
    except asyncio.TimeoutError:
        return platform, "TIMEOUT", None
    except Exception:
        return platform, "ERROR", None

async def main():
    username = input("Enter username to check: ").strip()

    async with aiohttp.ClientSession() as session:
        tasks = [
            check_username(session, platform, url_pattern, username)
            for platform, url_pattern in PLATFORMS.items()
        ]
        results = await asyncio.gather(*tasks)

    print("\n=== Username Check Results ===\n")
    for platform, status, link in results:
        if status == "FOUND":
            print(f"{Fore.GREEN}{platform:<12} {status:<10} {link}{Style.RESET_ALL}")
        elif status == "NOT FOUND":
            print(f"{Fore.RED}{platform:<12} {status:<10}{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}{platform:<12} {status:<10}{Style.RESET_ALL}")

if __name__ == "__main__":
    asyncio.run(main())