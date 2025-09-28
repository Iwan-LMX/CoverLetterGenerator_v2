from connectonion import Agent
from custom_tools import BrowserTool

browser = BrowserTool()
# Create agent with the tool
agent = Agent(
    name="CLGenerator", 
    tools=[browser],
    system_prompt="""You are a browser automation assistant.
    Help users navigate websites, take screenshots, and extract content.
    Always start the browser before performing actions.
    Be helpful and explain what you're doing.""",
)

# Use the agent
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
