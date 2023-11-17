class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate(self, quantity):
        total_price = self.price * quantity
        return total_price
menu = {
    "커피": Beverage("커피", 3000),
    "녹차": Beverage("녹차", 2500),
    "아이스티": Beverage("아이스티", 3000)
}
order = input("주문할 음료를 선택하세요 (커피, 녹차, 아이스티): ")
selected_beverage = menu.get(order)
if selected_beverage:
    quantity = int(input("수량을 입력하세요: "))
    total_price = selected_beverage.calculate(quantity)
    print(f"{order} {quantity}잔의 가격은 {total_price}원 입니다.")
else:
    print("잘못된 음료를 선택하셨습니다.")
