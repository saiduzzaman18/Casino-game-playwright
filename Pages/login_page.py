"""
pages/login_page.py — Page Object Model (POM) for the Login page.

WHY PAGE OBJECTS?
  Instead of writing locators (selectors) in every test,
  we put them here ONCE. If the HTML changes, you fix it
  in one place instead of hunting through 20 test files.

  Manual testing analogy: think of this as your "test script template"
  that describes where every element on the page lives.
"""

from playwright.sync_api import Page


class LoginPage:
    URL = "/login"

    def __init__(self, page: Page):
        self.page = page

        # ── Locators ────────────────────────────────────────
        # These are how Playwright "finds" elements on the page.
        # We prefer role/label selectors — they match what users see,
        # just like a manual tester would.
        self.email_input    = page.get_by_placeholder("Enter your email")
        self.password_input = page.get_by_placeholder("Enter your password")
        self.sign_in_button = page.get_by_role("button", name="Sign In")

        # Success / failure indicators
        self.error_message  = page.locator("text=Invalid") # adjust if needed
        self.page_heading   = page.get_by_role("heading")

    # ── Actions ─────────────────────────────────────────────
    # Each method = one user action. Keep them small and reusable.

    def navigate(self):
        """Open the login page."""
        self.page.goto(self.URL)

    def fill_email(self, email: str):
        self.email_input.fill(email)

    def fill_password(self, password: str):
        self.password_input.fill(password)

    def click_sign_in(self):
        self.sign_in_button.click()

    def login(self, email: str, password: str):
        """
        Full login flow in one call.
        Usage: login_page.login("user@example.com", "secret")
        """
        self.navigate()
        self.fill_email(email)
        self.fill_password(password)
        self.click_sign_in()

    # ── Assertions (state checks) ────────────────────────────
    def is_login_page_loaded(self) -> bool:
        return self.sign_in_button.is_visible()

    def get_current_url(self) -> str:
        return self.page.url
