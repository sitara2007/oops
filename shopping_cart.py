#online shopping application create a class called shopping cart requirements are platform 
# name , define a constructor, inside that write costumer name , product list, total amount  , 
# create a method to add products , create  another to remove products ,. create a class method to change platform name and create a static method to display the shopping rules
class ShoppingCart:#creating a class called shopping cart
    platform_name = "flipkart"#class member
    @staticmethod#static method to display the shopping rules
    def display_shopping_rules():#method to display the shopping rules
        return "1. All sales are final. 2. No returns or exchanges. 3" \
        ". Payment must be made at the time of purchase."#displaying the shopping rules
    def __init__(self, customer_name):#defining a constructor
        self.customer_name = customer_name#object member
        self.product_list = []#object member
        self.total_amount = 0#object member
    def add_product(self, product_name, price):#method to add products
        self.product_list.append(product_name)#adding product to the product list
        self.total_amount += price#adding price to the total amount
    def remove_product(self, product_name, price):#method to remove products
        if product_name in self.product_list:#checking if the product is in the product list
            self.product_list.remove(product_name)#removing product from the product list
            self.total_amount -= price#subtracting price from the total amount
        else:
            print("Product not found in the cart.")
    @classmethod#class method to change platform name
    def change_platform_name(cls, new_platform_name):#method to change platform name
        cls.platform_name = new_platform_name#  changing the platform name
    
    #displaying the shopping cart details
    def display_cart_details(self):
        return f"Customer Name: {self.customer_name}, Product List: {self.product_list}, \
            Total Amount: {self.total_amount}, Platform Name: {self.platform_name}"#displaying the shopping cart details
#creating an object of the shopping cart class
cart1 = ShoppingCart("Alice")#creating an object of the shopping cart class 
cart1.add_product("Laptop", 1000)#adding a product to the cart
cart1.add_product("Smartphone", 500)#adding a product to the cart
print(cart1.display_cart_details())#displaying the shopping cart details
cart1.remove_product("Laptop", 1000)#removing a product from the cart
print(cart1.display_cart_details())#displaying the shopping cart details
ShoppingCart.change_platform_name("Amazon")#changing the platform name using class method
print(cart1.display_cart_details())#displaying the shopping cart details
print(ShoppingCart.display_shopping_rules())#displaying the shopping rules using static method