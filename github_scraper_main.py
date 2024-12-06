import requests
import re
import os

def epic_ascii_intro(repo_name, owner):
    """Displays epic ASCII art at the start with repo name and owner."""
    print(f"""
 ██▀███   ██▓ ██▓███   ▄▄▄      
▓██ ▒ ██▒▓██▒▓██░  ██▒▒████▄    
▓██ ░▄█ ▒▒██▒▓██░ ██▓▒▒██  ▀█▄  
▒██▀▀█▄  ░██░▒██▄█▓▒ ▒░██▄▄▄▄██ 
░██▓ ▒██▒░██░▒██▒ ░  ░ ▓█   ▓██▒
░ ▒▓ ░▒▓░░▓  ▒▓▒░ ░  ░ ▒▒   ▓▒█░
  ░▒ ░ ▒░ ▒ ░░▒ ░       ▒   ▒▒ ░
  ░░   ░  ▒ ░░░         ░   ▒   
   ░      ░                 ░  ░
                               
🌟 Repo: {repo_name} | Owner: {owner} 🌟
""")

def fancy_github_scraper():
    """Ultimate fancy GitHub repository scraper."""
    print("✨ Welcome to the GitHub Repo Scraper ✨")

    # Get repository details from the user
    repo_link = input("🔗 Enter the GitHub repository link: ").strip()
    match = re.match(r'https://github\.com/(?P<owner>[^/]+)/(?P<repo>[^/]+)', repo_link)
    if not match:
        print("❌ Invalid GitHub repository link. Make sure it's in the format: https://github.com/owner/repo")
        return

    owner = match.group('owner')
    repo = match.group('repo')
    base_url = f"https://api.github.com/repos/{owner}/{repo}/contents"
    headers = {}

    # File display options
    display_option = input("📂 Would you like files saved in a folder (F) or displayed in the terminal (T)? [F/T]: ").strip().upper()
    if display_option not in ['F', 'T']:
        print("❌ Invalid choice. Please enter 'F' or 'T'.")
        return
    
    save_to_folder = (display_option == 'F')
    if save_to_folder:
        save_dir = f"{repo}_files"
        os.makedirs(save_dir, exist_ok=True)

    # Display ASCII header
    epic_ascii_intro(repo, owner)

    def process_directory(url, path=""):
        """Recursively processes directories and displays or saves files."""
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            items = response.json()
            for item in items:
                if item['type'] == 'file':
                    process_file(item['download_url'], item['name'], path)
                elif item['type'] == 'dir':
                    print(f"📁 Directory: {item['name']}")
                    process_directory(item['url'], path + "/" + item['name'])
                else:
                    print(f"⚠️ Unknown item type: {item['type']}")
        else:
            print(f"❌ Error accessing {url}: {response.status_code}")

    def process_file(file_url, file_name, path):
        """Displays or saves the content of a file."""
        response = requests.get(file_url, headers=headers)
        if response.status_code == 200:
            file_content = response.text
            print(f"📄 File: {file_name}")
            if save_to_folder:
                file_path = os.path.join(save_dir, path.lstrip("/"))
                os.makedirs(file_path, exist_ok=True)
                with open(os.path.join(file_path, file_name), "w", encoding="utf-8") as f:
                    f.write(file_content)
                print(f"✅ Saved: {file_name}")
            else:
                print(f"--- Start of {file_name} ---")
                print("\n".join(file_content.splitlines()[:10]))
                print("--- End of File Preview ---")
        else:
            print(f"❌ Error fetching file {file_name}: {response.status_code}")

    print(f"✨ Starting to scrape '{repo}' by '{owner}' ✨")
    process_directory(base_url)
    print("\n🎉 Scraping completed! Thank you for using the GitHub Repo Scraper! 🎉")

# Run the scraper
if __name__ == "__main__":
    fancy_github_scraper()
