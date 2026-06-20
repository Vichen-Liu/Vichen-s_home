#添加商品、删除商品、查询购物车内容、计算总价
class ShoppingCart:
    def __init__(self):
        self.cart={}

    def add_product(self,product,quantity,price):
        if product in self.cart:
            self.cart[product]["quantity"]+=quantity
        else:
            self.cart[product]={"quantity":quantity,"price":price}

    def del_product(self,product,quantity,price):
        if product not in self.cart:
            print("商品不存在！")
            return
        if quantity>=self.cart[product]["quantity"]:
            del self.cart[product]
        else:
            self.cart[product]["quantity"]-=quantity

    def view_shoppingcart(self):
        if not self.cart:
            print("购物车是空的！")
        else:
            for product,detail in self.cart.items():
                print(f"商品：{product}，数量：{detail["quantity"]}，单价：{detail["price"]}元")

    def total_price(self):
        total=0
        if not self.cart:
            print("购物车是空的！")
        else:
            for product,detail in self.cart.items():
                total+=detail["quantity"]*detail["price"]
        print(f"总价是:{total}元")

cart=ShoppingCart()
cart.add_product("薯片",2,9.5)
cart.add_product("泡面",5,3)
cart.add_product("矿泉水",20,2.2)
cart.view_shoppingcart()
cart.total_price()

