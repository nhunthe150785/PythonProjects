
#số tờ tiền kèm mệnh giá cần trả lại cho khách:
def money_return_detail(money):
    count_500 = int(money/500)
    money -= 500*count_500
    if count_500 != 0:
        print("500k: " + str(count_500))
    
    count_200 = int(money/200)
    money -= 200*count_200
    if count_200 != 0:
        print("200k: " + str(count_200))
    
    count_100 = int(money/100)
    money -= 100*count_100
    if count_100 != 0:
        print("100k: " + str(count_100))
    
    count_50 = int(money/50)
    money -= 50*count_50
    if count_50 != 0:
        print("50k = " + str(count_50))

    count_20 = int(money/20)
    money -= 20*count_20
    if count_20 != 0:
        print("20k: " + str(count_20))

    count_10 = int(money/10)
    money -= 10*count_10
    if count_10 != 0:
        print("10k: " + str(count_10))
    
    count_1 = money
    if count_1 != 0:
        print("1k: " + str(int(count_1)))


def main():
    APPLE_PRICE = 21  #20k/1kg
    weight = float(input("Enter weight = "))
    money_given = float(input("Enter money customer give you = "))
    total = APPLE_PRICE * weight
    print("Total price = " + str(round(total,2)))
    if money_given < total:
        print("Not enough money !")
    else:    
        money_return = money_given - total
        print("================ Screen ================")
        print("Money to return for customer = " + str(round(money_return,2)))
        money_return_detail(money_return)
main()

