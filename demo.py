#!/usr/bin/env python3
"""Interactive demo of the browser agent"""

from agent import agent, browser

print("🌐 Browser Automation Demo")
print("=" * 50)

# Step 1: Start browser
print("Step 1: Starting browser...")
result = agent.input("Start the browser (not headless so we can see it)")
print(f"✅ {result}\n")

# Step 2: Navigate to documentation
print("Step 2: Navigating to ConnectOnion docs...")
result = agent.input(
    "Navigate to https://docs.connectonion.com and tell me the page title"
)
print(f"✅ {result}\n")

# Step 3: Take screenshot
print("Step 3: Taking a screenshot...")
result = agent.input("Take a screenshot and save it as docs_homepage.png")
print(f"✅ {result}\n")

# Step 4: Extract navigation links
print("Step 4: Extracting navigation links...")
result = agent.input(
    "Extract all navigation links and tell me what sections are available"
)
print(f"📋 {result}\n")

# Step 5: Navigate to examples
print("Step 5: Going to examples section...")
result = agent.input(
    "Click on the Examples link if available and tell me what you see"
)
print(f"✅ {result}\n")

# Step 6: Full page screenshot
print("Step 6: Taking full page screenshot...")
result = agent.input(
    "Take a full page screenshot of the examples and save as examples_full.png"
)
print(f"✅ {result}\n")

# Clean up
print("Cleaning up...")
result = agent.input("Close the browser")
print(f"✅ {result}")

print("\n" + "=" * 50)
print("Demo complete! Check out:")
print("  - docs_homepage.png")
print("  - examples_full.png")