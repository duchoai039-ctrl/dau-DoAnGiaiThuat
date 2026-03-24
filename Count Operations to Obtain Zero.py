class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        dem = 0
        if num1 == 0 or num2 == 0: #Neu nums1 = 0 hoac num2 = 0 thi tra ve 0
            return 0
        if num1 == num2:
            return 1
        
        while num1 != num2:
            if num1 > num2:
                num1 -= num2
                dem+=1   #moi lan thuc hien xong se cong them 1 lan chay
            else:
                num2 -= num1
                dem+=1
        return dem + 1 #tra ve so lan chay + 1 vi con mot lan so sanh num = 0
 


        