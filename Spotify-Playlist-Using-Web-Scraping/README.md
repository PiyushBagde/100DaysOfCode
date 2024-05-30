## **Spotify Time Travel Playlist Maker 🔮: Relive Billboard's Top 100!**
It create a Spotify playlist based on Billboard's Hot 100 chart for a specific date, transporting you back in musical time!

Imagine instantly creating a playlist filled with the top hits from your favorite year, decade, or even a specific day. This script leverages web scraping and the Spotify API to make it happen.

### **How it Works:**

1. Specify Your Time Travel Destination: Enter the date (YYYY-MM-DD) you want to explore in the Billboard charts.
2. Web Scraping with Beautiful Soup: The script scrapes the Billboard website for the chosen date, extracting song titles.
3. Top Song List Creation: It compiles a list of the top 100 songs (adjust slicing as needed based on website structure).
4. Spotify Authentication: You'll need to obtain credentials (Client ID and Client Secret) from your Spotify developer account (https://developer.spotify.com/) and set up environment variables to store them securely.
5. Song Search and URI Collection: The script searches for each song on Spotify and, if found, obtains its unique URI (identifier).
6. Playlist Creation: A new private playlist is created on your Spotify account with a descriptive name reflecting the chosen date.
7. Time Travel Complete! The script populates the playlist with the top songs from your chosen date, ready for you to enjoy.



![image](https://github.com/PiyushBagde/100-days-of-python/assets/100503136/7028ab51-50bc-4b4e-a4fe-374516113e9c)
