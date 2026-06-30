"""
conftest.py — Shared fixtures for all tests.
This file is auto-loaded by pytest before any test runs.
Think of it as your "test environment setup" file.
"""

import pytest
from playwright.sync_api import sync_playwright

# ──────────────────────────────────────────────
# CONFIGURATION — change these in one place
# ──────────────────────────────────────────────
BASE_URL = "https://staging-backend.betnova.world"
HEADLESS   = True   # Set False to watch the browser while tests run (great for debugging)
SLOW_MO    = 1     # Milliseconds to slow down each action (e.g. 500 makes it human-speed)
TIMEOUT    = 30000 # Default timeout in ms (30 seconds)


@pytest.fixture(scope="session")
def browser_context():
    """
    Launches ONE browser for the entire test session.
    'scope=session' means it starts once and closes at the very end.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS, slow_mo=SLOW_MO)
        context = browser.new_context(
            base_url=BASE_URL,
            viewport={"width": 1280, "height": 720},
        )
        context.set_default_timeout(TIMEOUT)
        yield context
        browser.close()


@pytest.fixture(scope="function")
def page(browser_context):
    """
    Creates a FRESH page (tab) for each individual test.
    'scope=function' means every test gets a clean slate.
    """
    page = browser_context.new_page()
    yield page
    page.close()
