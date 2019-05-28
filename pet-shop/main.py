from Item import Item
from bs4 import BeautifulSoup
from selenium import webdriver


def main():

    FILENAME = 'items.csv'

    try:
        chrome = webdriver.Chrome("C:\chromedriver.exe")
        """ 1. From root webpage, go to most sold pet shop items webpage. """
        chrome.get("https://www.extra.com.br/")
        chrome.find_element_by_class_name("nav-item-todos").click()
        chrome.find_element_by_link_text("Pet Shop").click()
        chrome.find_element_by_xpath("//*[contains(text(), " +
            "'Produtos Mais Vendidos')]/following-sibling::a").click()
        """ 2. Get the link of the 20 first items. """
        elements = chrome.find_element_by_class_name("vitrineProdutos")
        elements = elements.find_elements_by_class_name("link")
        links = list()
        for element in elements[:2]:
            links.append(element.get_attribute("href"))
        """ 3. Loop through links. """
        items = list()
        for link in links:
            chrome.get(link)
            element = chrome.find_element_by_class_name("area-root")
            element = element.get_attribute('innerHTML')
            soup = BeautifulSoup(element, 'html.parser')
            name = soup.find_all("b", attrs={"itemprop": "name"})[0].getText()
            name = clean_string(name)
            code = soup.find_all(attrs={"itemprop": "productID"})[0].getText()
            code = code.split("Item", 1)[1].split(")", 1)[0]
            code = clean_string(code)
            price = soup.find_all(attrs={"class": "sale price"})[0].getText()
            price = clean_string(price)
            details = soup.find_all(attrs={"id": "descricao"})[0].getText()
            details = clean_string(details)
            item = Item("Pet Shop", name, code, price, details)
            items.append(item)
        chrome.quit()
        """ 4. Write item object list into csv file delimited by ';' char. """
        with open(FILENAME, mode="w", encoding="utf-8") as file:
                file.write("Category;Name;Code;Price;Details\n")
                for item in items:
                    file.write("%s\n" % item)
    except OSError as e:
        print(e)
    except Exception as e:
        print(e)


def clean_string(string):
    return string.strip().replace("\n", " ").replace(";", ", ")

if __name__ == "__main__":
    main()
