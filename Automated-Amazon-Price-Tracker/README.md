## **Automated Amazon Price Tracker with Email Notifications**
It automates price tracking for a product on Amazon and sends email notifications when the price drops below your desired threshold.

### **How it Works:**

1. **Target Product**: Specify the URL of the Amazon product you want to track.
2. **Web Scraping**: The script uses requests and beautifulsoup4 to retrieve the product's HTML content from Amazon.
3. **Price Extraction**: It navigates the HTML structure to locate and extract the current price information.
4. **Price Comparison**: It compares the current price with the predefined target price.
5. **Email Notification**: If the current price is lower than or equal to the target price, the script sends an email notification to your Gmail address using smtplib. The email contains the current price and a link to the product page.
