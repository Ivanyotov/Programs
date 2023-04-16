# Programs
# Broken Link Detector

This is a Python script that uses Selenium to detect broken links on a web page.

## Description

The Broken Link Detector is a command-line tool that automates the process of checking for broken links on a webpage. It uses Selenium, a popular web testing library, to interact with a web page in a real web browser and identify any links that return a non-200 HTTP status code, indicating a broken link.

The script performs the following steps:

1. Opens a web browser (Firefox by default, but can be configured to use other browsers).
2. Navigates to the specified URL.
3. Extracts all the 'a' (anchor) elements from the page, which represent links.
4. Iterates through each link and sends an HTTP GET request to check its status code.
5. If the status code is 200, the link is considered active and a success message is printed.
6. If the status code is not 200, the link is considered broken and an error message is printed, along with the status code.

The script can be easily configured to specify a different web browser, URL, or customize the behavior based on specific needs.

## Dependencies

The following dependencies are required to run the Broken Link Detector:

- Python 3.x
- Selenium library (installed via pip)
- Web driver for the chosen web browser (e.g., geckodriver for Firefox, chromedriver for Chrome)

## Usage

1. Install Python 3.x on your machine, if not already installed.
2. Install the Selenium library using pip: `pip install selenium`
3. Download the appropriate web driver for your preferred web browser and operating system, and make sure it is in your system's PATH.
4. Clone or download the Broken Link Detector script to your local machine.
5. Open the script in a text editor and customize the variables at the top of the script, such as `browser_type`, `url`, and `ignored_extensions`, to suit your needs.
6. Open a command prompt or terminal window and navigate to the directory where the script is located.
7. Run the script using Python: `python broken_link_detector.py`
8. The script will start checking for broken links on the specified web page and display the results in the command prompt or terminal window.

## Customization

The Broken Link Detector script can be customized to suit your specific requirements. Here are some options that you can modify:

- `browser_type`: You can change the web browser to be used by updating this variable to the appropriate value, such as "firefox", "chrome", or "edge".
- `url`: You can specify the URL of the web page to be checked by updating this variable with the desired URL.
- `ignored_extensions`: You can specify a list of file extensions to be ignored when checking for broken links. For example, if you want to ignore PDF files, you can add ".pdf" to the list.
- `ignored_domains`: You can specify a list of domain names to be ignored when checking for broken links. For example, if you want to ignore links pointing to external websites, you can add the domain names to the list.

## License

This project is licensed under the [MIT License](LICENSE), which allows for personal and commercial use, modification, and distribution.

## Disclaimer

This script is intended for educational and testing purposes only. Use it responsibly and at your own risk. The authors are not responsible for any misuse or damage caused by this script.

## Contact

If you have any questions or suggestions,
please feel free to contact the authors of this script:

[Ivan Atanasov Panayotov] - [ivan.panayotov93@gmail.com]
[Doncho Atanasov Panayotov] - [doncho.ap@gmail.com]
We appreciate any feedback or contributions to improve the Broken Link Detector script.

Happy link checking!
