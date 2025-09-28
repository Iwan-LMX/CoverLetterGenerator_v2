#!/usr/bin/env python3
"""Browser automation agent with Playwright integration"""

import os
from connectonion import Agent
from playwright.sync_api import sync_playwright
from typing import Optional, Dict, Any

class BrowserTool:
    """Tool for browser automation using Playwright"""
    
    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None
        
    def start_browser(self, headless: bool = False) -> str:
        """Start a new browser instance"""
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=headless)
        self.page = self.browser.new_page()
        return "Browser started successfully"
    
    def navigate(self, url: str) -> str:
        """Navigate to a URL"""
        if not self.page:
            return "Browser not started. Please start browser first."
        self.page.goto(url)
        return f"Navigated to {url}"
    
    def screenshot(self, filename: str = "screenshot.png", full_page: bool = False) -> str:
        """Take a screenshot of the current page"""
        if not self.page:
            return "Browser not started. Please start browser first."
        self.page.screenshot(path=filename, full_page=full_page)
        return f"Screenshot saved to {filename}"
    
    def extract_text(self, selector: str = "body") -> str:
        """Extract text content from the page"""
        if not self.page:
            return "Browser not started. Please start browser first."
        element = self.page.query_selector(selector)
        if element:
            return element.text_content()
        return "No content found"
    
    def click(self, selector: str) -> str:
        """Click an element on the page"""
        if not self.page:
            return "Browser not started. Please start browser first."
        self.page.click(selector)
        return f"Clicked element: {selector}"
    
    def fill(self, selector: str, text: str) -> str:
        """Fill a form field with text"""
        if not self.page:
            return "Browser not started. Please start browser first."
        self.page.fill(selector, text)
        return f"Filled {selector} with text"
    
    def extract_links(self) -> list:
        """Extract all links from the current page"""
        if not self.page:
            return []
        links = self.page.eval_on_selector_all(
            "a[href]", 
            "elements => elements.map(e => ({text: e.textContent, href: e.href}))"
        )
        return links
    
    def close_browser(self) -> str:
        """Close the browser and clean up"""
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()
        return "Browser closed"

# Create the browser tool instance
browser = BrowserTool()

# Create agent with browser tool
agent = Agent(
    "browser-agent",
    tools=[browser],
    system_prompt="""You are a browser automation assistant.
    Help users navigate websites, take screenshots, and extract content.
    Always start the browser before performing actions.
    Be helpful and explain what you're doing."""
)

if __name__ == "__main__":
    # Example usage
    print("🌐 Browser Automation Agent")
    print("=" * 50)
    
    # Start browser
    result = agent.input("Start the browser in headless mode")
    print(f"✅ {result}")
    
    # Navigate to a website
    result = agent.input("Navigate to https://example.com")
    print(f"✅ {result}")
    
    # Take screenshot
    result = agent.input("Take a full page screenshot and save as example.png")
    print(f"✅ {result}")
    
    # Extract content
    result = agent.input("Extract all the links from the page")
    print(f"📋 Links found: {result}")
    
    # Clean up
    result = agent.input("Close the browser")
    print(f"✅ {result}")