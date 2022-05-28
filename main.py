def find_anagrams(string_1, string_2):
      return sorted(string_1) == sorted(string_2) and len(string_1) == len(string_2)
   
    
string_1 = input(f"first string: ")
string_2 = input(f" Second String: ")

print(find_anagrams((string_1),(string_2)))