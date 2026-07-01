import asyncio
from playwright.async_api import async_playwright
import subprocess
import time
import os

async def run_test():
    # Start the server
    server = subprocess.Popen(["python3", "-m", "http.server", "8002"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(2) # Wait for server to start

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={'width': 1280, 'height': 800})
        page = await context.new_page()

        # Navigate to 3D Lab
        print("Navigating to 3D Lab...")
        await page.goto("http://localhost:8002/lab3d.html")

        # Give WebGL some time to render
        await page.wait_for_timeout(2000)

        # Take screenshot
        await page.screenshot(path="verification_3d.png")
        print("Screenshot saved to verification_3d.png")

        # Check if the canvas exists
        canvas_exists = await page.evaluate("() => !!document.querySelector('canvas')")
        print(f"Canvas exists: {canvas_exists}")

        await browser.close()

    # Stop the server
    server.terminate()

if __name__ == "__main__":
    asyncio.run(run_test())
