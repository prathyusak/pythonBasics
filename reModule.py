import re
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the the hat'))
print(re.findall(r'(.+) \1','yy kedjdf 11 aa aa kdfjde kdfjde kdfjde 22 ab ab abc abc sdfjk'))
print('tea for too'.replace('too', 'two'))
# .   -> anycharacter   |  {m}    ->  m repetetions                
# ^   -> start          |  {m,n}  ->  mto n repetions           
# $   -> end            |  {m,n}? ->  nongreedy {m,n}
# *   -> 0 or more      |  \ ,|   ->  escape , or A|B   
# +   -> 1 or more      |  [amz]  -> [a-z][A-Z][0-9][0-9A-Fa-f][aeiou]        
# ?   -> 0 or 1         |  [^]    -> not [] [^3]=>other than 3
# \Z  -> End of Str     |  \A     -> Start of Str
# \s  -> whitespace     |  \b     -> empty string b/w \w & \W
# \S  -> Non-whitespace |  \B     -> empty string not at begining or end of word
# \d  -> [0-9]          |  \w     -> word characters [a-zA-Z0-9_] 
# \D  -> [^0-9]         |  \W     -> not word Characters                    
# re.I-> Ignore case Flag
# re.M-> Multiline
# re.X-> Verbose