##########################
#Format specification
#replacement_field ::=  "{" [field_name] ["!" conversion] [":" format_spec] "}"
#format_spec     ::=  [[fill]align][sign][#][0][width][grouping_option][.precision][type]
#fill            ::=  <any character>
#align           ::=  "<" | ">" | "=" | "^"
#sign            ::=  "+" | "-" | " "
#width           ::=  digit+
#grouping_option ::=  "_" | ","
#precision       ::=  digit+
#type            ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
#
###################
#Conversion flags 
###################
print("repr() shows quotes: {!r}; str() doesn't: {!s}".format('test1', 'test2'))
#repr() shows quotes: 'test1'; str() doesn't: test2
print('{!a}'.format('a'))  #same as !r but escapes non ascii characters
###################
#Alignment
###################
fill = '*'
width=30
align='<' #left alignment
text='PYTHON'
print('{:<30}'.format('left aligned')) 
print('{:*<19}'.format('left aligned')) #left aligned with fill character '*' with width w
print('This is {0:{fill}{align}{width}} program'.format(text,fill=fill,align=align,width=width))
align ='>' # right alignment
print('This is {0:{fill}{align}{width}} program'.format(text,fill=fill,align=align,width=width))
align='^' #center alignment
print('This is {0:{fill}{align}{width}} program'.format(text,fill=fill,align=align,width=width))
align='=' #numerical prefix  '+00000120'
fill=0
n=123
print('This is {0:{fill}{align}{width}} program'.format(n,fill=fill,align=align,width=width))

######################
#Output signs for NUMERICALS
###################
print('{:+f}; {:+f}'.format(3.14, -3.14) )   #+3.140000; -3.140000
print('{:+}; {:+}'.format(3.14, -3.14) )     #+3.14; -3.14
print('{: }; {: }'.format(3.14, -3.14) )     # 3.14; -3.14
print('{:-}; {:-}'.format(3.14, -3.14) )     #3.14; -3.14
print('{:}; {:}'.format(3.14, -3.14) )       #3.14; -3.14
#print('{:+}'.format('a')) #Error

########################
#Precision
print('{:.3g}'.format(238834) )    #'2.39e+05'
print('{:.3G}'.format(238834))     #'2.39E+05'
print('{:.2G}'.format(2.38434))    #'2.4'
print('{:.3G}'.format(2.38434))    #'2.38'
print('{:.2F}'.format(2.38434))    #'2.38'
print('{:.2f}'.format(2.3434))     #'2.34'
print('{:.3f}'.format(238834))     #'238834.000'
print('{:f}'.format(238834) )      #'238834.000000'

########################
#Output different bases
###################
n=42
print("int: {0:d}; hex: {0:x}; HEX: {0:X} oct: {0:o};  bin: {0:b} ; unicode: {0:c}".format(n))     
#int: 42; hex: 2a; HEX: 2A oct: 52;  bin: 101010 UNICoDE: *
print("int: {0:#d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(n))
#int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010
octets = [192, 168, 0, 1]
print('{:02X}{:02X}{:02X}{:02X}'.format(*octets))     #C0A80001
print('{:X}{:X}{:X}{:X}'.format(*octets))             #C0A801 

########################
#Thousands Seperator
###################
print( '{:,}'.format(1234567890))  #1,234,567,890
print( '{:_}'.format(1234567890))  #1_234_567_890
print( '{:_b}'.format(256))        #1_0000_0000
print( '{:_x}'.format(102400))     #1_9000

##########################
#Percentage
###################
points=39
total=77
print('Correct answers: {:.2%}'.format(points/total))   #Correct answers: 50.65%
print('Correct answers: {:10.2%}'.format(points/total)) #Correct answers:     50.65%
print('Correct answers: {:.4%}'.format(points/total))   #Correct answers: 50.6494%
print('Correct answers: {:%}'.format(points/total))     #Correct answers: 50.649351%

############################
#Type specific formating
###################
import datetime
d = datetime.datetime(2010, 7, 4, 12, 15, 58)
print('{:%Y-%m-%d %H:%M:%S}'.format(d))


#####################################
#f' or F' strings
#######################################
text='PYTHON'
num=78
value=3948324
x =3424.00
y=-198
################
#base n  {:[width][#][seperator][b|o|x|X|d|c|n]}
print(f'the num is {num:#b}')         #the num is 0b1001110
print(f'the num is {num:b}')          #the num is 1001110
print(f'the num is {num:c}')          #the num is N
print(f'the num is {num:x}')          #the num is 4e
print(f'the num is {num:10X}')        #the num is         4E
print(f'the num is {num:o}')          #the num is 116
print(f'the value is {value:#_b}')    #the value is 0b11_1100_0011_1111_0010_0100
#print(f'the num is {x:b}') #error float cannot be converted
#print(f'the value is {value:10#}' )
#print(f'the value is {value:10c}')

#################
#signs {:[+|-(default)|=]}
print(f'the x is {x:+f}' )            #the x is +3424.000000
print(f'the x is {x:+}')              #the x is +3424.0
print(f'the x is {x:-}')              #the x is 3424.0
print(f'the x is {x: }')              #the x is  3424.0
print(f'the y is {y:+f}' )            #the y is -198.000000
print(f'the y is {y:+}')              #the y is -198
print(f'the y is {y:-}')              #the y is -198
print(f'the y is {y: }')              #the y is -198
print(f'{x:+10_.2f}')                 # +3_424.00
print(f'{x: 10_}')                    #  3_424.0

###################
#Alignment
print(f'the value is {value:*<19}')     #the value is 3948324************
print(f'the value is {value:$>19}')     #the value is $$$$$$$$$$$$3948324
print(f'the value is {value:^^19}')     #the value is ^^^^^^3948324^^^^^^
print(f'the y is {y:$=19}')             #the y is -$$$$$$$$$$$$$$$198
print(f'the y is {y:0=19}')             #the y is -000000000000000198

#############################
#precision and percentage
print(f'the value is {value:10_.2f}')
print(f'the value is {value:10_}')
print(f'the value is {num:2.2%}' )

############################
#float presentation
print(f'the value is {value:10g}')
print(f'the value is {value:G}')
print(f'the value is {value:e}')
print(f'the value is {value:E}')
print(f'the value is {value:F}')
print(f'the value is {value:f}')
print(f'the value is {value:n}')





    