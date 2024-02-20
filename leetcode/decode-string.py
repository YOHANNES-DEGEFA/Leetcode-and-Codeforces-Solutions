class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s: 
            if c != ']': stack.append(c)
            else:
                    cur_str = []
                    cur_num = []
                    while stack[-1]  != '[':
                            cur_str.append(stack.pop())
                    stack.pop()
                    while stack and stack[-1].isdigit():
                        cur_num.append(stack.pop())

                    cur_str = ''.join(cur_str[::-1])
                    cur_num = ''.join(cur_num[::-1])
                    stack.append(cur_str * int(cur_num))

        return ''.join(stack)
                            
  



                
                

                

        
        

