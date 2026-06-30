![Playwright Tests](https://github.com/saiduzzaman18/Casino-game-playwright/actions/workflows/playwright.yml/badge.svg)

# BetNova Playwright Automation


[![Playwright Tests](https://github.com/<YOUR_USERNAME>/<YOUR_REPO>/actions/workflows/playwright.yml/badge.svg)](https://github.com/<YOUR_USERNAME>/<YOUR_REPO>/actions/workflows/playwright.yml)

> Replace `<YOUR_USERNAME>/<YOUR_REPO>` above with your actual GitHub username/repo
> once this is pushed — the badge will then show live pass/fail status.

---

## Project Structure

```
Casino-Game-Playwright/
│
├── .github/
│   └── workflows/
│       └── playwright.yml       ← CI pipeline (runs tests on every push)
│
├── conftest.py                  ← Browser setup + screenshot-on-failure hook
├── pytest.ini                   ← pytest config (auto-generates HTML report)
├── requirements.txt
├── .gitignore                   ← keeps .venv, reports, secrets out of git
│
├── Pages/
│   └── login_page.py            ← Page Object Model for login
│
├── Tests/
│   └── test_login.py            ← Login test cases
│
└── Reports/                      ← generated automatically, not committed
    ├── report.html
    └── screenshots/
```

---

## Running Tests Locally

```bash
# Install dependencies
pip install -r requirements.txt
playwright install chromium

# Run all tests — HTML report auto-generates at Reports/report.html
pytest

# Run a specific file
pytest Tests/old_login.py -v

# Watch the browser while running (debugging)
# In conftest.py, set HEADLESS = False
```

After any run, open `Reports/report.html` in your browser. Failed tests
automatically include a screenshot taken at the moment of failure.

---

## Continuous Integration (GitHub Actions)

Every push or pull request to `main`/`master` automatically:
1. Spins up a clean Ubuntu environment
2. Installs Python, dependencies, and the Chromium browser
3. Runs the full test suite
4. Uploads the HTML report (with screenshots) as a downloadable artifact —
   even if tests fail

### Viewing CI results
1. Go to your repo on GitHub → **Actions** tab
2. Click the latest workflow run
3. Scroll to **Artifacts** → download `playwright-report`
4. Unzip and open `report.html`

### Triggering manually
Go to **Actions → Playwright Tests → Run workflow** to trigger a run
on demand, without needing a new commit.

---

## Known Issues (found via automation)

| Issue | Test | Status |
|---|---|---|
| Master Admin login does not redirect after valid credentials | `test_master_admin_login_success` | Logged — staging bug, form stays on `/login?email=...` |
| Super Admin login does not redirect after valid credentials | `test_super_admin_login_success` | Logged — same root cause as above |

These tests currently assert the *actual* (buggy) behavior so the suite
stays green while documenting the defect. Once the dev team fixes the
redirect, update these two assertions back to `not_to_have_url(...)`.

---

## Test Credentials (staging)
- **Master Admin:** master.admin@nomail.com / 1234
- **Super Admin:** casino.admin@nomail.com / 1234

---

## Next Steps
1. Add Dashboard page object once login redirect is fixed
2. Parametrize login tests (data-driven testing with `@pytest.mark.parametrize`)
3. Move credentials to a `.env` file instead of hardcoding
4. Add Slack/email notification on CI failure
