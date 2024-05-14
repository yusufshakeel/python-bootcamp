from functools import reduce


class GroceryTotal:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        self.items.append({'name': name, 'price': price})

    def total(self):
        return reduce(lambda acc, curr: acc + curr['price'], self.items, 0)

    def total_using_sum(self):
        return sum([item['price'] for item in self.items])


def main():
    grocery_total = GroceryTotal()
    grocery_total.add_item('apple', 10)
    grocery_total.add_item('mango', 20)
    grocery_total.add_item('banana', 30)
    print('total', grocery_total.total())
    print('total_using_sum', grocery_total.total_using_sum())


if __name__ == '__main__':
    main()
