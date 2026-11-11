# Website Marketing Quest

A gamified Streamlit application for a hands-on BBA Marketing session on building websites for digital marketing success.

## Features
- 11 preset teams
- Startup profile challenge
- Landing page planning and preview
- Database concepts quiz
- Web technology quiz
- Optional Gemini AI marketing mentor
- Next.js website pitch challenge
- Shared leaderboard backed by SQLite
- Faculty password-protected bonus points, CSV export and reset

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
# .venv\\Scripts\\activate     # Windows

pip install -r requirements.txt
streamlit run app.py
```

## Enable Gemini AI

Create `.streamlit/secrets.toml`:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
FACULTY_PASSWORD = "choose-a-strong-password"
```

The AI mentor uses the `google-genai` package and the `gemini-2.5-flash` model. If no key is configured, the rest of the app still works and displays a configuration message.

## Deploy on Streamlit Community Cloud

1. Push `app.py`, `requirements.txt`, and this README to a GitHub repository.
2. Create a new app at https://share.streamlit.io/
3. Select the repository and `app.py`.
4. In app settings, open **Secrets** and add `GEMINI_API_KEY` and `FACULTY_PASSWORD`.
5. Deploy and share the app URL or QR code with students.

## Important deployment notes

- This starter app uses SQLite for the shared leaderboard. It works for a single Streamlit app process and a classroom demonstration.
- Streamlit Community Cloud local files are not a durable database: the SQLite file can be lost when the app is restarted/redeployed. For repeat use or reliable persistence, migrate the team and submission tables to Supabase or another hosted database.
- Do not commit API keys or `secrets.toml` to GitHub.
- The team selector is for classroom convenience, not secure identity verification. Students should use the same team name on every device.
- For a 65-student session, create teams in advance and display the QR code on screen.
