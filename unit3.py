# first ========================================
print ("First")
print ("=" * 50)

fib1 = 1
fib2 = 1
n =input ("Number element of Fibonachi order: ")
n = int(n)
i = 0
fibn = 0
stepforward = lambda x, y: x + y
while i < n-2:
   # fibn = fib1 + fib2
   fibn = stepforward(fib1, fib2)
   fib1 = fib2
   fib2 = fibn
   i = i + 1
   # print (fibn)

print (n, "th element from Fibbonachi order is:  ", fibn)

# Second ========================================
print ("Second")
print ("=" * 50)
# #Create file
nk = input('Input numbers string of creating file : ')
nk = int(nk)
import random, os
homdir = os.path.abspath(__file__)
homdir = os.path.join(*homdir.split('/')[0:-1])
homdir = '/' + homdir + '/number.txt'
f = open(homdir, 'w')
for i in range(nk):
  f.write(str(random.randint(0,1000)) + '\n')
f.close()
#task =======================================
print ("File including these numbers")
f = open(homdir)
print (f.read())
f.seek(0)
a =[]
for line in f:
   a.append(int(line))
f.close()
b = []
for i in a:
   if (i % 2) != 0:
       b.append(i)
print ("All is not ever number :", b)
f = open(homdir, 'w')

for i in b:
   f.write(str(i) + '\n')
f.close()
# Check =======================================
f = open(homdir)
print ('Check write to file' )
print (f.read())
f.close()
keyy = input ('press any key to continue')
# Third ========================================
print ("=" * 50)
print ("Third")
homdir = os.path.abspath(__file__)
homdir = os.path.join(*homdir.split('/')[0:-1])
newfile = '/' + homdir + '/tolstoy_rev.txt'
homdir = '/' + homdir + '/tolstoy.txt'

fl = open(homdir, 'r')
fll = open(newfile, 'w')

def revers(str):
   a = str.split()
   # print (a)
   a.reverse()
   # print(a)
   return ' '.join(a)
print ('sourse >>>>>>>>>>')
print (fl.read())
fl.seek(0)
print ('result >>>>>>>>>>>')
for line in fl:
   print (revers(line))
fl.close()
fll.close()

# Fourth ========================================
print ("=" * 50)
print ("Fourth")

def counter_word(str):
   flags = 1
   ff = '/'
   flags = str.find(ff)
   counter_w = 0
   # print (flags)
   if flags == 0:
       fl = open(str, 'r')
       for line in fl:
           a = line.split()
           cn = len(a)
           counter_w = counter_w + cn
   else:
       a = str.split()
       cn = len(a)
       counter_w = counter_w + cn
   return counter_w

print ('if input -2- then use path :' , homdir)

zuka = input('Input string or path to file : ')

if zuka == '2':
   zuka = homdir
   print ('word number in file : ', counter_word(zuka))
else:
   # print (zuka)
   print('word number in string :', counter_word(zuka))
