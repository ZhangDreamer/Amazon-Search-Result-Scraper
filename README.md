# Amazon Product Scraper

This is a simple Python script that uses web scraping techniques to extract product information from Amazon search results. The script extracts the product name, price, and rating for each product in the search results.

## Installation

Before running the script, you need to install the following packages:

- pandas
- requests
- BeautifulSoup4
- lxml

You can install these packages using pip by running the following command:

pip install pandas requests BeautifulSoup4 fuzzywuzzy


## Usage

To use the script, simply run the `amazon_scraper.py` file and enter the search query when prompted. The script will then extract the product information from the search results and save it to a CSV file named `products.csv` in the same directory as the script.
python main.py


## Example Output

Here is an example of what the output CSV file might look like if you searched for **Iphone 13**:

| Product Name               | Price      | Rating |
|----------------------------|------------|--------|
| iPhone 12 Pro Max          | $1,099.00 | 4.8    |
| iPhone 13, 128GB, Pink - Unlocked (Renewed Premium)   | $999.99  | 4.7    |
| iPhone 13 Mini, 256GB, Pink - Unlocked (Renewed Premium)  | $620.00  | 4.5    |
| Apple iPhone 13, 128GB, Blue - Unlocked (Renewed)       | $609.99 | 4.9    |
| Apple iPhone 13 Mini, 256GB, Pink - Unlocked (Renewed) | $548.26  | 4.9    |

## Disclaimer

This project is provided "as is" without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.

This project is licensed under the terms of the MIT license.
