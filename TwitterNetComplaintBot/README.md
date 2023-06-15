# Twitter Net Complaint Bot
This Python script performs a speed test using Ookla Speedtest and tweets a complaint to your internet service provider if the download or upload speeds are below the specified thresholds.

# Setup
1. Clone the repository or download the Python script.
2. Install the necessary dependencies:
- `os`
- `time`
- `selenium`
- `webdriver`
3. Download and install the appropriate ChromeDriver executable for your system and update the driver_path variable in the script.
4. Set up the required environment variables:
- `USERNAME`: Your Twitter username.
- `PASSWORD`: Your Twitter password.
- `PHONE`: Your phone number associated with your Twitter account.
5. Make sure you have Brave Browser installed, or update the chrome_options.binary_location to match the location of your preferred browser.

# Usage
1. Run the Python script in your preferred Python environment.
2. The script will open the Ookla Speedtest website and initiate the speed test.
3. After the test completes, the script will navigate to the Twitter login page and log into your account.
4. If the download or upload speeds are below the specified thresholds, the script will compose a complaint tweet and post it.
5. If the speeds are above the thresholds, the script will print "Speed is up to the mark."

# Note
Ensure that you have a stable internet connection and the necessary permissions and access to perform the speed test and post tweets.

# Tech Stack
Language: Python <br>
Libraries: `os`, `time`, `selenium`

# URL's
<a href="https://www.speedtest.net/">Ookla Speedtest</a><br>
<a href="https://twitter.com/home">Twitter</a>
