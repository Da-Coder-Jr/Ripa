# **GitHub Repo Scraper Setup Guide**

Follow these steps to set up and run the GitHub Repo Scraper.

### **1. Clone the Repository**
Clone the repository using the following command:
```bash
git clone https://github.com/Da-Coder-Jr/Ripa.git
cd Ripa
```

### **2. Install Dependencies**
Make sure you have Python 3.8 or higher installed. Then, install the required dependencies with:
```bash
pip install requests
```

### **3. Run the Script**
Start the scraper by running:
```bash
python3 github_scraper_main.py
```

### **4. Provide the GitHub Repository Link**
When prompted, enter a valid GitHub repository link in the format:
```
https://github.com/<owner>/<repo>
```
For example:
```
https://github.com/octocat/Hello-World
```

### **5. Choose File Handling Option**
You will be asked how you want to handle the files:
- Enter **F** to save all repository files in a folder named after the repository.
- Enter **T** to preview the first 10 lines of each file in the terminal.

Example prompt:
```
Save files locally (F), preview in terminal (T), or both (A)? [F/T/A]: T
```

### **6. Done!**
