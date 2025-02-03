"""This script serves as a skeleton template for synchronous AgentQL scripts for scraping multiple pages."""
import logging
import os
import agentql
import time
from agentql.ext.playwright.sync_api import Page
from playwright.sync_api import sync_playwright

# Set up logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

# Set the base URL
BASE_URL = "https://www.cars.com/shopping/results/"

def main():
    with sync_playwright() as p, p.chromium.launch(headless=False) as browser:
        # Create a new page in the browser and wrap it to get access to the AgentQL's querying API
        page = agentql.wrap(browser.new_page())
        
        # Scrape 200 pages
        for page_num in range(481, 501):
            try:
                # Construct URL for current page
                current_url = f"{BASE_URL}?page={page_num}&zip=60606" if page_num > 1 else BASE_URL
                
                # Log current page being processed
                log.info(f"Processing page {page_num} of 500")
                
                # Navigate to the current page
                page.goto(current_url)
                
                # Add a small delay to prevent overwhelming the server
                time.sleep(2)
                
                # Get and process data from current page
                get_response(page, page_num)
                
            except Exception as e:
                log.error(f"Error processing page {page_num}: {str(e)}")
                continue

def get_response(page: Page, page_num: int):
    query = """
    {
        cars[]{
            stocktype
            title
            mileage
            price
            monthlypayment
            vehicledealer
        }
    }
    """
    
    try:
        response = page.query_elements(query)
        
        # Log success and save the response
        log.info(f"Successfully scraped data from page {page_num}")
        
        # Here you can add code to save the response to a file or database
        # For example, saving to a file:
        save_response(response, page_num)
        
    except Exception as e:
        log.error(f"Error querying elements on page {page_num}: {str(e)}")

def save_response(response, page_num):
    """Save the response data to a file"""
    try:
        # Create a 'data' directory if it doesn't exist
        os.makedirs('data', exist_ok=True)
        
        # Save the response to a file named by page number
        with open(f'data/cars_page_{page_num}.txt', 'w', encoding='utf-8') as f:
            f.write(str(response))
            
        log.info(f"Saved data from page {page_num} to file")
        
    except Exception as e:
        log.error(f"Error saving data from page {page_num}: {str(e)}")

if __name__ == "__main__":
    main()