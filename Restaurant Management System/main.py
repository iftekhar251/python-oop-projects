from food_item import FoodItem
from menu import Menu
from orders import Order
from users import Admin,Customer,Employee
from restaurant import Restaurant

mama_hotel=Restaurant("Mama Hotel")

def customer_menu():
    name=input("Enter Your Name :")
    email=input("Enter Your Email :")
    phone=input("Enter Your Phone :")
    adress=input("Enter Your Adress :")

    customer=Customer(name=name,email=email,phone=phone,adress=adress)

    while(True):
        print(f"---------Welcome {customer.name}---------")
        print("1. View Menu")
        print("2. Add item to cart")
        print("3. View Cart")
        print("4. PayBill")
        print("5. Exit")

        choice=int(input("Enter Your choice : "))
        if choice == 1:
            customer.view_menu(mama_hotel)
        elif choice == 2:
            item_name = input("Enter item name : ")
            item_quantity=int(input("Enter item quantity : "))
            customer.add_to_cart(mama_hotel,item_name,item_quantity)
        
        elif choice == 3:
            customer.view_cart()
        elif choice == 4:
            customer.pay_bill()
        elif choice == 5:
            break
        else:
            print("Invalid Choice")
        


def admin_menu():
    name=input("Enter Your Name : ")
    email=input("Enter Your Email : ")
    phone=input("Enter Your Phone : ")
    adress=input("Enter Your Adress :")

    admin=Admin(name=name,email=email,phone=phone,adress=adress)

    while(True):
        print(f"---------Welcome {admin.name}---------")
        print("1. Add New Item")
        print("2. Add New Employee")
        print("3. View Employee")
        print("4. View Item")
        print("5. Delete Item")
        print("6. Exit")

        choice=int(input("Enter Your choice : "))
        if choice == 1:
            item_name=input("Enter Item Name : ")
            item_price=int(input("Enter Item Price : "))
            item_quantity=int(input("Enter Item Quantity : "))
            item=FoodItem(item_name,item_price,item_quantity)
            admin.add_new_item(mama_hotel,item)
            
        elif choice == 2:
            name=input("Enter Employee Name : ")
            email=input("Enter Employee Email : ")
            phone=input("Enter Employee Phone : ")
            adress=input("Enter Employee Adress : ")
            age=input("Enter Employee Age : ")
            designation=input("Enter Employee Designation : ")
            salary=input("Enter Employee Salary : ")

            employee=Employee(name, phone, email, adress,age,designation,salary)

            admin.add_employee(mama_hotel,employee)

        
        elif choice == 3:
            admin.view_employee(mama_hotel)

        elif choice == 4:
            admin.view_menu(mama_hotel)
        elif choice == 5:
            item_name=input("Enter Item Name : ")
            admin.remove_item(mama_hotel,item_name)
        
        elif choice == 6:
            break
        else:
            print("Invalid Input")

while(True):
    print("---------WELCOME---------")
    print("1. CUSTOMER")
    print("2. ADMIN")
    print("3. EXIT")

    choice=int(input("Enter Your Choice : "))

    if choice == 1:
        customer_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else:
         print("Invalid Input")

        
