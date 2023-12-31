## Jerrys Quick Mart solution in Python

### Problem

Jerry's Quick Mart in Orlando, FL is having its grand opening in 3 days. His previously hired software team lost all their files, and Jerry needs a solution for his grand opening.

Jerrys has hired you for a quick solution to his problem. For the day of the Grand Opening, he has put out marketing noting that all transactions must be in cash.

The basic functionalities that needs for his grand opening are the following:
* Select whether customer is a Rewards member or Regular customer
* Add items to cart
* Remove individual items from cast, with empty cart option
* View cart (including totals)
* Checkout and Print receipt
* Cancel Transaction

Inventory is passed into the application in a text file, with item information on each line. The receipt is printed as a .txt file, with the transaction number and date included in the file name. Inventory is updated after checkout to avoid customers buying items that are out of stock.

**&lt;SAMPLE INVENTORY INPUT FORMAT&gt;**

&lt;item&gt;: &lt;quantity&gt;, &lt;regular price&gt;, &lt;member price&gt;, &lt;tax status&gt;

**&lt;SAMPLE INVENTORY INPUT&gt;**

Milk: 5, $3.75, $3.50, Tax-Exempt

Red Bull: 10, $4.30, $4.00, Taxable

Flour: 1, $3.10, $2.75, Tax-Exempt

[...]

**&lt;SAMPLE OUTPUT&gt;**

&lt;transaction_000001_12082016.txt&gt;

December 8, 2016

TRANSACTION: 0000001

ITEM            QUANTITY                UNIT PRICE      TOTAL

Milk                2                     $3.50         $7.00

Red Bull            3                     $4.00         $8.00

Flour               1                     $2.75         $2.75

***************************

TOTAL NUMBER OF ITEMS SOLD: 6

SUB-TOTAL: $17.75

TAX(6.5%): $0.52

TOTAL: $18.27

CASH: $20.00

CHANGE: $1.73

***************************

YOU SAVED: $1.75!


&lt;inventory.txt&gt;

Milk: 3, $3.75, $3.50, Tax-Exempt

Red Bull: 7, $4.30, $4.00, Taxable

Flour: 0, $3.10, $2.75, Tax-Exempt

[...]

### Solution

#### Instalation
Firstly you must download and install Python 3.10.6 on your machine according to your operating system. The download link is as follows:

[Python 3.10.6](https://www.python.org/downloads/release/python-3106/).

#### Virtual Environment for Python 3.10.6

Subsequently, the venv package for Python 3.10.6 must be installed (For guidance refer to the link [venv](https://docs.python.org/3/library/venv.html)). For example for Debian-based distributions:

`sudo apt install python3.10-venv`

The virtual environment should be created using venv `python3.10 -m venv /path/to/new/virtual/environment`. For example:

`python3.10 -m venv myvenv`

Then the virtual environment should be set up using venv `source /path/to/directory`. For example:

`source myvenv/bin/activate`

#### Running the application
Run the `main.py` to use the application

#### Testing
To run the tests use the following command:
`python3 -m tests/test_store.py`



