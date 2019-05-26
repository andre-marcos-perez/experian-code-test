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
  1. Access root webpage, click on *Todos os departamentos* then on *Pet Shop*;
  1. On *Produtos mais vendidos* section, click on *Veja mais*.
1. Get the link of the 20 first items.
1. Loop through links:
  1. Access each item webpage;
  1. Extract and sanitize requested info;
  1. Instantiate item object with extracted info and enqueue it on an item list.
1. Write item object list into csv file delimited by semicolon (;) char.

## Test 2 | Test File

### Problem

### Solution
