import math
choice = int(input("1) pH -> H\n2) H -> pH\n3) pOH -> OH\n4) OH -> pOH\n"))
if(choice == 1): # pH -> H
	num = float(input("pH를 입력하세요.\n\t> "))
	ans = 10**(-num)
	print("\nH =", ans)
elif(choice == 2): # H -> pH
	num = float(input("H이온의 수를 입력하세요.\n\t> "))
	ans = math.log(num, 10)
	print("\npH =", -ans)
elif(choice == 3): # pOH -> OH
	num = float(input("pOH를 입력하세요.\n\t> "))
	ans = 10**(-num)
	print("\nOH =", ans)
elif(choice == 4): # OH -> pOH
	num = float(input("OH이온의 수를 입력하세요\n\t> "))
	ans = math.log(num, 10)
	print("\npOH =", -ans)

else:
	print("잘못된 값입니다.")