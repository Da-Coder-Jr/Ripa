import requests
import os
import re

def display_banner():
    """Display an epic banner at startup."""
    print("""
    ██▀███   ██▓ ██▓███   ▄▄▄      
    ▓██ ▒ ██▒▓██▒▓██░  ██▒▒████▄    
    ▓██ ░▄█ ▒▒██▒▓██░ ██▓▒▒██  ▀█▄  
    ▒██▀▀█▄  ░██░▒██▄█▓▒ ▒░██▄▄▄▄██ 
    ░██▓ ▒██▒░██░▒██▒ ░  ░ ▓█   ▓██▒
    ░ ▒▓ ░▒▓░░▓  ▒▓▒░ ░  ░ ▒▒   ▓▒█░
      ░▒ ░ ▒░ ▒ ░░▒ ░       ▒   ▒▒ ░
      ░░   ░  ▒ ░░░         ░   ▒   
       ░      ░                 ░  ░
    """)

def get_repository_details():
    """Gets repository details from user input."""
    repo_link = input("Enter the GitHub repository link: ").strip()
    print(f"Rippin' up {repo_link}...")
    match = re.match(r'https://github\.com/(?P<owner>[^/]+)/(?P<repo>[^/]+)', repo_link)
    if not match:
        print("Invalid GitHub repository link. Make sure it's in the format: https://github.com/owner/repo")
        return None, None
    return match.group('owner'), match.group('repo')

def ask_file_handling_option():
    """Asks user how they want to handle the files."""
    while True:
        choice = input("Save files locally (F), preview in terminal (T), or both (A)? [F/T/A]: ").strip().upper()
        if choice in ['F', 'T', 'A']:
            return choice
        print("Invalid choice. Please enter 'F', 'T', or 'A'.")

def scrape_repository(owner, repo, save_to_folder, preview_files):
    """Scrapes the GitHub repository based on user input."""
    base_url = f"https://api.github.com/repos/{owner}/{repo}/contents"
    save_dir = f"{repo}_files" if save_to_folder else None
    if save_to_folder and save_dir:
        os.makedirs(save_dir, exist_ok=True)

    response = requests.get(base_url)
    if response.status_code != 200:
        print(f"Error accessing {base_url}: {response.status_code}")
        return

    items = response.json()
    for item in items:
        if item['type'] == 'file':
            process_file(item, save_to_folder, save_dir, preview_files)
        elif item['type'] == 'dir':
            print(f"Processing directory: {item['name']} - Recursively processing...")
            scrape_directory(item['url'], save_dir, preview_files, path=item['name'])

def scrape_directory(url, save_dir, preview_files, path=""):
    """Recursively scrapes a directory and handles its files."""
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error accessing {url}: {response.status_code}")
        return

    items = response.json()
    for item in items:
        if item['type'] == 'file':
            process_file(item, True, save_dir, preview_files, path=path)
        elif item['type'] == 'dir':
            print(f"Processing subdirectory: {item['name']} - Continuing...")
            scrape_directory(item['url'], save_dir, preview_files, os.path.join(path, item['name']))

def process_file(item, save_to_folder, save_dir, preview_files, path=""):
    """Processes a file by saving or displaying its content."""
    file_url = item['download_url']
    file_name = item['name']
    response = requests.get(file_url)
    if response.status_code != 200:
        print(f"Error fetching file {file_name}: {response.status_code}")
        return

    file_content = response.text
    if save_to_folder:
        save_path = os.path.join(save_dir, path) if path else save_dir
        os.makedirs(save_path, exist_ok=True)
        with open(os.path.join(save_path, file_name), "w", encoding="utf-8") as f:
            f.write(file_content)
        print(f"Saved: {file_name} to {save_path}")

    if preview_files:
        print(f"--- Start of {file_name} ---")
        print("\n".join(file_content.splitlines()[:10]))
        print("--- End of File Preview ---")

def main():
    display_banner()
    owner, repo = get_repository_details()
    if not owner or not repo:
        return

    choice = ask_file_handling_option()
    save_to_folder = choice in ['F', 'A']
    preview_files = choice in ['T', 'A']

    print(f"Starting to scrape '{repo}' by '{owner}'")
    scrape_repository(owner, repo, save_to_folder, preview_files)
    print("\nScraping completed! Here are some fragments of the repository.")

if __name__ == "__main__":
    main()
