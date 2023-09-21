class Stack:
    def valid_paranthesis(self, s: str) -> bool:
        """
        Check if string of paranthesis is valid. https://leetcode.com/problems/valid-parentheses/description/

        param s: String of paranthesis
        return: True or False
        """
        stack = []
        
        for i in range(len(s)):
            if s[i] in '({[':
                stack.append(s[i])
            else:
                if s[i] in ']})':
                    if len(stack) == 0:
                        return False
                    else:
                        p = stack.pop()
                        if p + s[i] == '()' or p + s[i] == '{}' or p + s[i] == '[]':
                            continue
                        else:
                            return False
        # if paranthesis valid, stack will be emptied by end of loop. not stack will be true. 
        # If not matched, stack will not be emptied, return false
        return not stack
