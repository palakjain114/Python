def is_substring(s1, s2):
     for i in range(len(s1) - len(s2) + 1):
         if s1[i:i+len(s2)] == s2:
             return True
     return False
 
     string1 = input()  
     string2 = input()
     print(is_substring(string1, string2))
