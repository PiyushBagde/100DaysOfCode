## **Automate Your Job Search on LinkedIn 🤖**

  1. **apply_jobs.py:** Automates applying for a specific job listing.
  2. **save_jobs.py:** Saves all listed jobs on a LinkedIn search page.

**Important Note:**

* These scripts are for educational purposes only and may violate LinkedIn's terms of service. Use them responsibly!
* Entering your actual login credentials in the code is not recommended due to security concerns.

**Getting Started:**

1. Download and install the appropriate WebDriver for your browser (e.g., ChromeDriver for Chrome).
2. Place the WebDriver in a directory accessible to your Python scripts.

### **apply_jobs.py**

This script automates applying for a single job listing. It leverages Selenium to:

* Open the desired job listing on LinkedIn.
* Locate and click the "Easy Apply" button.
* Fill out the application form (pre-filled with sample data in this example).
* Submit the application.

**Key Considerations:**

* The script bypasses the login window using a pre-configured Chrome profile (modify the `user-data-dir` path accordingly).
* Update the script with the target job listing URL.
* Replace sample data in the application form with your actual information.

### **save_jobs.py**

This script iterates through all listed jobs on a LinkedIn search page and saves them. It uses Selenium to:

* Open the LinkedIn search page with your desired filters.
* Locate all job listing elements on the page.
* Click on each job listing to open the details page.
* Find and click the "Save" button for each job.

**Things to Remember:**

* Similar to `apply_jobs.py`, the script uses a pre-configured Chrome profile for login persistence.
* Modify the script with the base URL for your LinkedIn job search.
* Be mindful that rerunning `save_jobs.py` might un-save previously saved jobs.

**CSS Selectors**

Both scripts utilize CSS selectors to locate specific elements on the LinkedIn webpages. You can learn more about CSS selectors at [https://www.w3schools.com/css/css_selectors.asp](https://www.w3schools.com/css/css_selectors.asp).

**Disclaimer:**

These scripts are provided as a basic example and might require adjustments for future changes in LinkedIn's website structure.
