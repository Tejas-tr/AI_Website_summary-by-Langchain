# 🔎 AI Website Summarizer (LangChain Edition)

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/Framework-LangChain-1C3C3C?logo=langchain&logoColor=white)
![Gradio](https://img.shields.io/badge/UI-Gradio-orange?logo=gradio&logoColor=white)
![OpenAI](https://img.shields.io/badge/API-OpenAI-412991?logo=openai&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

Run 'app.py' to get url of the app, friendly summary — powered by **LangChain**, **OpenAI**, and a simple **Gradio** UI.

This is an upgraded version of my original summarizer, refactored to use LangChain's composable chain syntax (`prompt | model | parser`) instead of calling the OpenAI API directly.

## 📋 Table of Contents

- [What it does](#-what-it-does)
- [Tech Stack](#️-tech-stack)
- [Project Structure](#-project-structure)
- [How it works](#️-how-it-works)
- [Getting Started](#-getting-started)
- [Notes](#-notes)
- [License](#-license)

## ✨ What it does

- Enter any website URL into a simple web UI
- The page is scraped and cleaned of navigation, ads, scripts, and other noise
- The cleaned text is passed through a LangChain chain to an OpenAI model
- A short, friendly summary is returned and displayed in the UI

## 🛠️ Tech Stack

- **Python**
- **LangChain** (`langchain-openai`, `langchain-core`) — for prompt templating, model invocation, and output parsing via a composable chain
- **OpenAI API** (`gpt-4o-mini`) — the underlying summarization model
- **Requests** — to fetch raw HTML from the target website
- **BeautifulSoup4** — to parse and clean the HTML into readable text
- **Gradio** — for the interactive web UI
- **python-dotenv** — for loading the API key from a `.env` file

## 📂 Project Structure

```
├── app.py         # Gradio UI — entry point for the app
├── lc.py          # LangChain chain: prompt → model → parser
├── scraper.py     # Fetches and cleans website content
└── .env           # Your API keys (not committed)
```

## ⚙️ How it works

1. **`scraper.py`** — `fetch_website_contents(url)` sends an HTTP GET request (with browser-like headers to avoid being blocked), parses the HTML with BeautifulSoup, strips out scripts/styles/nav/footer/images, and returns the page title plus clean visible text.
2. **`lc.py`** — Builds a LangChain chain:
   - A `ChatPromptTemplate` wraps the scraped text into a summarization prompt
   - `ChatOpenAI` (`gpt-4o-mini`) generates the summary
   - `StrOutputParser` extracts the plain text response
   - `summarize(url)` runs the full chain: scrape → prompt → model → parse
3. **`app.py`** — Wraps `summarize()` in a Gradio `Interface` so users can paste a URL into a textbox and see the summary rendered as Markdown.

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

### 2. Install dependencies
```bash
pip install gradio requests beautifulsoup4 python-dotenv langchain-openai langchain-core
```

### 3. Add your API key
Create a `.env` file in the project root:
```
OPENAI_API_KEY=your_openai_api_key
```

### 4. Run the app
```bash
python app.py
```

The app will launch locally and also generate a public shareable link (via `launch(share=True)`).

## 📌 Notes

- The scraper mimics a real browser via request headers to reduce the chance of being blocked by target sites.
- Some websites (heavy JavaScript rendering, bot protection, paywalls) may not scrape cleanly with `requests` + `BeautifulSoup` alone — a headless browser (e.g. Playwright/Selenium) would be needed for those cases.
- Swap `gpt-4o-mini` for any other LangChain-supported chat model with minimal code changes.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to check the [issues page](../../issues) or open a pull request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Your Name**
- GitHub: [@your-username](https://github.com/your-username)
- LinkedIn: [Your LinkedIn Profile](https://linkedin.com/in/your-profile)

---

⭐️ If you found this project useful, consider giving it a star!
