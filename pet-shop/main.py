from Item import Item


def main():

    FILENAME = 'items.csv'

    items = list()
    i = Item("bone", 123, 12.5, "white bone")
    items.append(i)

    try:
        with open(FILENAME, mode='w') as file:
            file.write('Category,Name,Code,Price,Details\n')
            for item in items:
                file.write('%s\n' % item)
    except OSError as e:
        print(e)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
