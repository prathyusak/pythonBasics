with open('../temp') as f:
    read_data=f.read()
print(f.closed)   

f = open('../temp','r+') # file object f

# r  --> only for reading
# w  --> only for write (deletes the file if exits)
# a  --> appends to the existing file at end
# r+ --> read and write
# b  --> binary mode for JPEG and EXE files

print(f.read())  # entire file is printed
print(f.read())  # '' --> EOF

f.seek(0)

print(f.readline()) # reads line by line
print(f.readline()) #'' when EOF has reached, empty lines return '\n'
print('--------------')
f.write('This is a test\n')
f.seek(0)       #
print(list(f))  #['0123456789abcdef2)This is a test\n', 'This is a test\n']
f.seek(0)
print(f.readlines())  #['0123456789abcdef2)This is a test\n', 'This is a test\n', 'This is a test\n', 'This is a test\n']
value = ('the answer', 42)
#f.write(value)   #Error only strings can be written
print(f.write(str(value)))  # returns number of characters written
f.close()
#########
#f.seek(offset,whence)
#  whence --> 0 => offset from begining of file
#             1 => current file position
#             2 => end of file as reference
# for text files offset is valid only for 0 begining of files
#               whence of 1,2 other than offset of 0,f.tell() gives undefined behaviour
f = open('../temp', 'wb')
f.write(b'0123456789abcdef')
f.close()
f = open('../temp','rb')
f.seek(5)  #go to 6th byte in file
print(f.read(1))
f.seek(-3,2)  # 3rd byte before end of the file
print(f.read(1))
print(f.tell())   #14
f.close()


#######
#f.tell() => file objects current position
f=open('../temp')
f.seek(8)
print(f.tell()) #=>8