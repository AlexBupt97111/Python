def create_good(item, price): 
    good = {
      "description": item,
      "price": price  
    } 
    return good 

def calc_new_price(good, sk): 
    percent = 0
    for price in sk.keys(): 
        if good.get("price") > price: 
            percent = sk.get(price) 
    discount = (good.get("price")*percent)//100
    new_price = good.get("price") - discount
    return new_price

def calculate_buy(list_of_goods,sk):
    total_sum = 0
    for good in list_of_goods:
        total_sum = total_sum + calc_new_price(good,sk)
    return total_sum

def print_check_doc(list_of_goods, sk): 
    for good in list_of_goods:
        print(good.get("description"), "\t", calc_new_price(good, sk))
    print("Total = ", calculate_buy(list_of_goods,sk), "UAH")

good_1 = create_good("Chocolate", 218) 
good_2 = create_good("Coffe", 512)
good_3 = create_good("Hamon", 2175)
good_4 = create_good("Bread", 31)
good_5 = create_good("Green tea", 82) #5 times: 5 goods need

list_of_goods = [good_1, good_2, good_3,good_4,good_5]#lst
sk = {
  500:5,
  1000:7,
  2000:10
} 

print_check_doc(list_of_goods, sk) 
