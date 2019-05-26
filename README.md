# Experian Code Test

## Test 1 | Pet Shop

### Problem

Using **Python**, **Selenium** and **Beautiful Soup**, get the following info
from the first 20 items of the pet shop section in the Extra supermarket website
(www.extra.com.br):

* name;
* code;
* price;
* details.

### Solution

1. From root webpage, go to most sold pet shop items webpage:
   - Access root webpage, click on *Todos os departamentos* then on *Pet Shop*;
   - On *Produtos mais vendidos* section, click on *Veja mais*.
2. Get the link of the 20 first items.
3. Loop through links:
   - Access each item webpage;
   - Extract and sanitize requested info;
   - Instantiate item object with extracted info and enqueue it on an item list.
4. Write item object list into csv file delimited by semicolon (;) char.

## Test 2 | Test File

### Problem

### Solution
