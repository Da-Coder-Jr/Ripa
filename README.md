<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GitHub Repo Scraper - Setup and Instructions</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            background-color: #f8f9fa;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background: #ffffff;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
            color: #007bff;
        }
        h2 {
            color: #495057;
            margin-bottom: 10px;
            border-bottom: 2px solid #dee2e6;
            padding-bottom: 5px;
        }
        pre {
            background: #f1f1f1;
            border-radius: 5px;
            padding: 15px;
            font-size: 14px;
            overflow-x: auto;
        }
        code {
            background: #f8f9fa;
            color: #d63384;
            padding: 2px 4px;
            border-radius: 4px;
            font-size: 95%;
        }
        .box {
            background: #e9ecef;
            border-left: 5px solid #007bff;
            padding: 15px;
            margin: 20px 0;
            border-radius: 4px;
        }
        ul {
            padding-left: 20px;
        }
        li {
            margin: 5px 0;
        }
        .btn {
            display: inline-block;
            background: #007bff;
            color: white;
            padding: 10px 15px;
            text-decoration: none;
            border-radius: 5px;
            font-size: 16px;
        }
        .btn:hover {
            background: #0056b3;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>GitHub Repo Scraper</h1>
        <p><strong>🚀 A sleek Python-based scraper</strong> that allows you to explore and save GitHub repository contents effortlessly. Perfect for developers looking to inspect or download repositories without requiring a GitHub API key (unless accessing private repos).</p>

        <h2>📂 Setup Instructions</h2>

        <div class="box">
            <h3>1. Clone the Repository</h3>
            <p>Clone the scraper from the official GitHub repository:</p>
            <pre>
git clone https://github.com/Da-Coder-Jr/Ripa.git
cd Ripa
            </pre>
        </div>

        <div class="box">
            <h3>2. Install Dependencies</h3>
            <p>Make sure Python 3.8 or higher is installed on your system. Use the following command to install dependencies:</p>
            <pre>
pip install requests
            </pre>
        </div>

        <div class="box">
            <h3>3. Run the Script</h3>
            <p>Start the scraper by running:</p>
            <pre>
python github_scraper.py
            </pre>
        </div>

        <h2>🔧 Usage Instructions</h2>

        <div class="box">
            <h3>1. Launch the Script</h3>
            <p>Run the script in your terminal or IDE:</p>
            <pre>
python github_scraper.py
            </pre>
        </div>

        <div class="box">
            <h3>2. Enter a Valid GitHub Repository Link</h3>
            <p>When prompted, input the GitHub repository link in the following format:</p>
            <pre>https://github.com/<owner>/<repo></pre>
            <p>Example:</p>
            <pre>https://github.com/octocat/Hello-World</pre>
        </div>

        <div class="box">
            <h3>3. Choose How Files Are Handled</h3>
            <p>Select how you want to process the files:</p>
            <ul>
                <li><code>F</code>: Save all files in a structured folder named after the repository.</li>
                <li><code>T</code>: Preview the first 10 lines of each file directly in the terminal.</li>
            </ul>
        </div>

        <div class="box">
            <h3>4. Observe the Scraper in Action</h3>
            <p>If <code>Save (F)</code> is selected:</p>
            <ul>
                <li>Files will be saved in a folder named <code>&lt;repo_name&gt;_files</code>, preserving the original directory structure.</li>
            </ul>
            <p>If <code>Preview (T)</code> is selected:</p>
            <ul>
                <li>The first 10 lines of each file will be displayed in your terminal.</li>
            </ul>
        </div>

        <h2>📁 Example Walkthrough</h2>

        <div class="box">
            <h3>Input Example</h3>
            <pre>
🔗 Enter the GitHub repository link: https://github.com/octocat/Hello-World
📂 Would you like files saved in a folder (F) or displayed in the terminal (T)? [F/T]: F
            </pre>
        </div>

        <div class="box">
            <h3>Output Example</h3>
            <pre>
🌟 Repo: Hello-World | Owner: octocat 🌟

✨ Starting to scrape 'Hello-World' by 'octocat' ✨
📁 Directory: src
📄 File: main.py
✅ Saved: main.py
📄 File: README.md
✅ Saved: README.md

🎉 Scraping completed! Thank you for using the GitHub Repo Scraper! 🎉
            </pre>
        </div>

        <h2>📂 Saved File Structure</h2>
        <div class="box">
            <p>If the <strong>Save option</strong> is selected, files are organized into a structured folder mirroring the repository layout:</p>
            <pre>
Hello-World_files/
├── README.md
├── src/
│   └── main.py
            </pre>
        </div>

        <p style="text-align: center;">
            <a href="https://github.com/Da-Coder-Jr/Ripa" class="btn">Explore the Repository</a>
        </p>
    </div>
</body>
</html>
