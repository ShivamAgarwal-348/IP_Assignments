def show_menu():
    print("==================================================")
    print("                  MY BAZAAR")
    print("==================================================")
    print("Hello Welcome to my Grocery Store!")
    print("Following are the available in the shop:")
    print()
    print("--------------------------------------------------")
    print(" CODE | DESCRIPTION |   CATEGORY  | COST (Rs)")
    print("--------------------------------------------------")
    print("  0   | TShirt      | Apparels    | 500")
    print("  1   | Trousers    | Apparels    | 600")
    print("  2   | Scarf       | Apparels    | 250")
    print("  3   | Smartphone  | Electronics | 20,000")
    print("  4   | iPad        | Electronics | 30,000")
    print("  5   | Laptop      | Electronics | 50,000")
    print("  6   | Eggs        | Eatables    | 5")
    print("  7   | Chocolate   | Eatables    | 10")
    print("  8   | Juice       | Eatables    | 100")
    print("  9   | Milk        | Eatables    | 45")
    print("-------------------------------------------------")

def get_regular_input():
    print("\n-------------------------------------------------")
    print("Enter Items You Wish To Buy ") 
    print("-------------------------------------------------")
    lst=list(map(int,input("Enter the item codes (space generated) : ").split()))
    order_lst=[0]*10
    for i in lst:
        if i in range(10):
            order_lst[i] += 1
        else:
            print("Incorrect Code",i)

    return order_lst

def get_bulk_input():
    print("\n-------------------------------------------------")
    print("Enter Items And Quantities ") 
    print("-------------------------------------------------")
    order_lst=[0]*10
    
    while(True):
        lst=list(map(int,input("Enter Code and Quantity(leave blank to stop) : ").split()))
        if(len(lst)==0):
            print("Your order has been finalized")
            break
        if lst[0] in range(10):
            if(lst[1]>=0):
                order_lst[lst[0]] += lst[1]
                print("You added",lst[1],Entries[lst[0]])
            else:
                print("Invalid Quantity, Try Again")
        else:
            if(lst[1]>=0):
                print("Invalid Code, Try Again")
            else:
                print("Invalid Code and Quantity, Try Again")

    return order_lst

def print_order_details(quantities):

    print("\n-------------------------------------------------")
    print("Order Details : ") 
    print("-------------------------------------------------")
    s_no=1

    for i in range(10):
        if(quantities[i]>0):
            print('['+ str(s_no) + ']',Entries[i],'x',quantities[i],'= Rs', Cost_Price[i],'*',quantities[i],'= Rs',Cost_Price[i]*quantities[i])
            s_no+=1

def calculate_category_wise_cost(quantities):
    print("\n-------------------------------------------------")
    print("Category wise Cost") 
    print("-------------------------------------------------")
    apparels_cost=0
    electronics_cost=0
    eatables_cost=0

    for i in range(10):
        if i in range(3):
            apparels_cost += Cost_Price[i] * quantities[i]
        elif i in [3,4,5]:
            electronics_cost += Cost_Price[i] * quantities[i]
        elif i in [6,7,8,9]:
            eatables_cost += Cost_Price[i] * quantities[i]
    print("Apparels = Rs",apparels_cost)
    print("Electronics = Rs",electronics_cost)
    print("Eatables = Rs",eatables_cost)
    return (apparels_cost,electronics_cost,eatables_cost)

def get_discount(cost, discount_rate):

    	return int(cost * discount_rate)

def calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost):
    print("\n-------------------------------------------------")
    print("Discounts") 
    print("-------------------------------------------------")    
    apparels_discount = 0
    electronics_discount=0
    eatables_discount=0

    if(apparels_cost>=2000):
        apparels_discount=get_discount(apparels_cost,0.1)         
        print("[Apparel] Rs",apparels_cost,'-',apparels_discount,'=',apparels_cost - apparels_discount)
        apparels_cost -= apparels_discount

    if(electronics_cost>=25000):
        electronics_discount=get_discount(electronics_cost,0.1)         
        print("[Electronics] Rs",electronics_cost,'-',electronics_discount,'=',electronics_cost - electronics_discount)
        electronics_cost -= electronics_discount
    
    if(eatables_cost>=500):
        eatables_discount=get_discount(eatables_cost,0.1)         
        print("[Eatables] Rs",eatables_cost,'-',eatables_discount,'=',eatables_cost - eatables_discount)
        eatables_cost -= eatables_discount

    print()
    print("Total Discount = Rs",apparels_discount + electronics_discount + eatables_discount)
    print("Total Cost = Rs",apparels_cost + electronics_cost + eatables_cost)

    return (apparels_cost,electronics_cost,eatables_cost)

def get_tax(cost, tax):

	return int(cost * tax)

def calculate_tax(apparels_cost, electronics_cost, eatables_cost):

    print("\n-------------------------------------------------")
    print("Tax") 
    print("-------------------------------------------------") 
    print("[Apparel]",apparels_cost,"* 0.10 = Rs",get_tax(apparels_cost,0.10))
    print("[Electronics]",electronics_cost,"* 0.15 = Rs",get_tax(electronics_cost,0.15))
    print("[Eatables]",eatables_cost,"* 0.05 = Rs",get_tax(eatables_cost,0.05))

    Total_tax = get_tax(apparels_cost,0.10) + get_tax(electronics_cost,0.15) + get_tax(eatables_cost,0.05)
    Total_cost = apparels_cost + electronics_cost + eatables_cost + Total_tax

    print()
    print("Total tax = Rs",Total_tax)
    print("Total cost = Rs",Total_cost)

    return (Total_cost,Total_tax)

def apply_coupon_code(total_cost):

    print("\n-------------------------------------------------")
    print("Coupon Code") 
    print("-------------------------------------------------") 
    coupon=""
    Coupon_discount=0

    while(True):

        coupon = input("Enter Coupon Code(else leave blank) : ")
        
        if(len(coupon)==0):
            print("No Coupon code applied")
            break
        elif(coupon == "HELLE25"):
            if(total_cost >= 25000):
                print("[HELLE25] min(5000 , Rs",total_cost ,"* 0.25) = 5000")
                Coupon_discount += 5000 
                total_cost -= 5000
                break
            else:
                print("Coupon conditions not met as cost is less than 25000, Try again")

        elif(coupon == "CHILL50"):
            if(total_cost >= 50000):
                print("[CHILL50] min(10000 , Rs",total_cost ,"* 0.50) = 10000")
                Coupon_discount += 10000
                total_cost -= 10000
                break
            else:
                print("Coupon conditions not met as cost is less than 50000, Try again")

        else:
            print("Invalid coupon code, Try Again")

    print()
    print("Total Coupon Discount = Rs",Coupon_discount)
    print("Total Cost = Rs",total_cost)

    return (total_cost,Coupon_discount)

show_menu()
choice='a'
Entries=['Tshirt','Trousers','Scarf','Smartphone','iPad','Laptop','Eggs','Chocolate','Juice','Milk']
Categories=['Apparels','Apparels','Apparels','Electronics','Electronics','Electronics','Eatables','Eatables','Eatables','Eatables']
Cost_Price=[500,600,250,20000,30000,50000,5,10,100,45]

orders=[0]*10
while(choice != 'y' and choice != 'n' and choice != 'Y' and choice != 'N'):
    choice=input("Would you like to buy in bulk (Y or y/N or n) : ")
    if(choice == 'Y' or choice == 'y'):
        orders=get_bulk_input()
    elif(choice == 'N' or choice == 'n'):
        orders=get_regular_input()

print_order_details(orders)
Cat_wise_cost = calculate_category_wise_cost(orders)
Cat_wise_cost = calculate_discounted_prices(Cat_wise_cost[0],Cat_wise_cost[1],Cat_wise_cost[2])

Cost_inc_tax = calculate_tax(Cat_wise_cost[0],Cat_wise_cost[1],Cat_wise_cost[2])

Cost_after_discount = apply_coupon_code(Cost_inc_tax[0])

print("\nThank you for visiting!")
