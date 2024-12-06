# GitHub Repo Scraper

A sleek Python-based GitHub repository scraper that allows you to view or save repository file contents directly. Perfect for exploring repositories without needing the GitHub API key unless required for private repos.

Features
Dynamic ASCII Art: Showcases the repository and owner name in an epic style.
Choose Your Display: Save repository files to a folder or preview them in the terminal.
Recursive File Navigation: Seamlessly handles nested directories and files.
Error Handling: Detects and alerts on invalid links or inaccessible files.
Setup Instructions
Clone the Repository:
git clone https://github.com/your-username/github-repo-scraper.git
cd github-repo-scraper
Install Dependencies: Ensure Python 3.8+ is installed on your system. Use pip to install required libraries:
pip install requests
Run the Script: Simply execute the script:
python github_scraper.py
Usage Instructions
Launch the Script: Run the Python script in your terminal or IDE:
python github_scraper.py
Enter the Repository Link: When prompted, provide a GitHub repository link in the following format:
🔗 Enter the GitHub repository link: https://github.com/octocat/Hello-World
Choose File Handling Option: Select how you want the files to be processed:
F to save files in a folder named after the repository.
T to view files in the terminal.
Watch the Scraper in Action: The scraper will:
Display directories and files dynamically.
Save files to the folder (if chosen) or preview the first 10 lines in the terminal.
