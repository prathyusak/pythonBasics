import re
#SEARCH  re.search(<regex>,<string>)
print(re.search('123','foo123'))         #<re.Match object; span=(3, 6), match='123'>
#SPLIT  re.split(pattern,string,maxsplit=0,flags=0)
print(re.split(r'\W+','Words,words.'))    #['Words', 'words', '']
print(re.split(r'(\W+)','Words,words.'))  #['Words', ',', 'words', '.', '']
#FINDALL re.findall(pattern,strings,flags=0)
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))   #['foot', 'fell', 'fastest']
print(re.findall(r'(.+) \1','yy kedjdf 11 aa aa kdfjde kdfjde kdfjde 22 ab ab abc abc sdfjk'))  #['aa', 'kdfjde', 'ab', 'abc']
#SUB   re.sub(pattern,repl,string,count=0,flags=0)
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the the hat'))  #cat in the the hat
print(re.sub(r'\sAND\s',' & ','Beans and Spam',flags=re.I))    #Beans & Spam
print('tea for too'.replace('too', 'two'))     #tea for two


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

print(re.search('[0-9][0-9][0-9]', 'foo456bar'))   #<_sre.SRE_Match object; span=(3, 6), match='456'>
print(re.search('[0-9][0-9][0-9]', '12foo34'))   #None
print(re.search('1.3', 'foo123bar'))             #<re.Match object; span=(3, 6), match='123'>        
print(re.search('ba[artz]', 'foobarqux'))       #<re.Match object; span=(3, 6), match='bar'>
print(re.search('[0-9a-fA-f]', '--- a0 ---'))   #<re.Match object; span=(4, 5), match='a'>
print(re.search('[^0-9]', '12345foo'))        #<re.Match object; span=(5, 6), match='f'>
print(re.search('[]]', 'foo[1]'))             #<re.Match object; span=(5, 6), match=']'>
print(re.search('[ab\]cd]', 'foo[1]'))      #<re.Match object; span=(5, 6), match=']'>   
print(re.search('foo.bar', 'fooxbar'))      #<re.Match object; span=(0, 7), match='fooxbar'>   
print(re.search('foo.bar', 'foobar'))       #None
print(re.search('foo.bar', 'foo\nbar'))     #None
print(re.search('\w', '#(.a$@&'))           #<re.Match object; span=(3, 4), match='a'>
print(re.search('\W', 'a_1*3Qb'))           #<re.Match object; span=(3, 4), match='*'>
print(re.search('\d', 'abc4def'))           #<re.Match object; span=(3, 4), match='4'>
print(re.search('\D', '234Q678'))           #<re.Match object; span=(3, 4), match='Q'>
print(re.search('\s', 'foo\nbar baz'))      #<re.Match object; span=(3, 4), match='\n'>
print(re.search('\S', '  \n foo  \n  '))    #<re.Match object; span=(4, 5), match='f'>
print(re.search('[\d\w\s]', '--- ---'))     #<re.Match object; span=(3, 4), match=' '>
print(re.search('\.', 'foo.bar'))           #<re.Match object; span=(3, 4), match='.'>
print(re.search('^foo', 'foobar'))          #<re.Match object; span=(0, 3), match='foo'>
print(re.search('\Afoo', 'foobar'))         #"
print(re.search('bar$', 'foobar'))          #<re.Match object; span=(0, 3), match='bar'>
print(re.search('bar\Z', 'foobar'))         #"
print(re.search(r'\bbar', 'foobar'))        #None
print(re.search(r'foo\b', 'foo bar'))       #<re.Match object; span=(0, 3), match='foo'>
print(re.search(r'\Bfoo\B', 'barfoobaz'))   #<re.Match object; span=(3, 6), match='foo'>
#quantifiers
print(re.search('foo-*bar', 'foo--bar'))    #<re.Match object; span=(0, 8), match='foo--bar'>
print(re.search('foo-+bar', 'foobar'))      #None
print(re.search('foo-?bar', 'foobar'))      #<re.Match object; span=(0, 6), match='foobar'>  
print(re.search('<.*>', '%<foo> <bar> <baz>%'))   #<re.Match object; span=(1, 18), match='<foo> <bar> <baz>'>
print(re.search('<.*?>', '%<foo> <bar> <baz>%'))  #<re.Match object; span=(1, 6), match='<foo>'>
print(re.search('x-{3}x', 'x---x')    )           #<re.Match object; span=(0, 5), match='x---x'>
print(re.search('a{3,5}', 'aaaaaaaa'))            #<re.Match object; span=(0, 5), match='aaaaa'>
print(re.search('a{3,5}?', 'aaaaaaaa'))           #<re.Match object; span=(0, 3), match='aaa'>
#grouping and capturing
print(re.search('(bar)', 'foo bar baz'))          #<re.Match object; span=(4, 7), match='bar'>
print(re.search('(bar)+', 'foo barbar baz'))      #<re.Match object; span=(4, 10), match='barbar'>
print(re.search(r'([a-z])#\1', 'd#d'))            #<re.Match object; span=(0, 3), match='d#d'>
print(re.search('(\w+),(\w+),(\w+)', 'foo,quux,baz'))  #<re.Match object; span=(0, 12), match='foo,quux,baz'>
print(re.search('(?P<w1>\w+),(?P<w2>\w+),(?P<w3>\w+)', 'foo,quux,baz')) #<re.Match object; span=(0, 12), match='foo,quux,baz'>
print(re.search(r'(?P<word>\w+),(?P=word)', 'foo,foo'))    #<re.Match object; span=(0, 7), match='foo,foo'>
print(re.search('(\w+),(?:\w+),(\w+)', 'foo,quux,baz'))    #<re.Match object; span=(0, 12), match='foo,quux,baz'>, no grouping for quux
regex = r'^(###)?foo(?(1)bar|baz)'
print(re.search(regex, '###foobar'))          #<re.Match object; span=(0, 9), match='###foobar'>
regex = r'^(?P<ch>\W)?foo(?(ch)(?P=ch)|)$'
print(re.search(regex, '@foo@'))           #<re.Match object; span=(0, 5), match='@foo@'>
print(re.search(r'(<)?(\w+@\w+(?:\.\w+)+)(?(1)>|$)','<a@gd.com>'))   #<re.Match object; span=(0, 10), match='<a@gd.com>'>
print(re.search('foo(?=[a-z])', 'foobar'))   #<_sre.SRE_Match object; span=(0, 3), match='foo'>
print(re.search('foo(?=[a-z])', 'foo123'))   #None
print(re.search('foo(?![a-z])', 'foobar'))   #None
print(re.search('foo(?![a-z])', 'foo123'))   #<_sre.SRE_Match object; span=(0, 3), match='foo'>
print(re.search('(?<=foo)bar', 'foobar'))    #<_sre.SRE_Match object; span=(3, 6), match='bar'>
print(re.search('(?<=qux)bar', 'foobar'))    #None
print(re.search('(?<!foo)bar', 'foobar'))    #None
print(re.search('(?<!qux)bar', 'foobar'))    #<_sre.SRE_Match object; span=(3, 6), match='bar'>
print(re.search('bar(?#This is a comment) *baz', 'foo bar baz qux'))  #<_sre.SRE_Match object; span=(4, 11), match='bar baz'>

# (...)                                matches inside , and later can be accessed by \1
# (?P<name>...)                        pattern matching with group name
# (?P=name)                            Backreference
# (?=...)                              Lookahead
# (?!...)                              Negativelookahead
# (?<=...)                             Lookbehind assersion
# (?<!...)                             Negative lookbehind 
# (?(id/name)yes_pattern|no_pattern)   id or name exists yes_pattern else no_pattern
# (?#...)                              Comment
