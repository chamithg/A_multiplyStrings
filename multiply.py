class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        # define a 0 array to expected maximum count
        if num1 == "0" or num2 =="0":
            return "0"
        
        output =[0] * (len(num1)+ len(num2))
        
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
            
                tempVal = (int(num1[i1]) * int(num2[i2])) + output[i1+i2]
                if tempVal< 10:    
                    output[i1+i2] = tempVal
                else:
                    output[i1+i2] =tempVal%10
                    output[i1+i2+1] += tempVal//10
                
                print(output)
        
        output = output[::-1]
        
        outStr = ""
        
        for i in range(len(output)):
            if output[i] ==0 and outStr =="":
                continue
            else:
                outStr += str(output[i])
        return outStr
        
        
        
        
    
            
num1 = "123"
num2 = "456"      
obj = Solution()       
print(obj.multiply(num1,num2))       