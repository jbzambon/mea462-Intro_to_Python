#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Exercise 2: ex2_simplecalc.py
#
# Program to demonstrate usage of Modules, Variables, Calculations,
# Assignments, and Arrays
#
# Joseph B. Zambon
#  jbzambon@ncsu.edu
#  31 March 2021


# In[17]:


# Included modules
import numpy  # conda install numpy
              # Imported to express various data types
import math   # Installed typically by default
              # Imported to play with pi to double precision
import sys    # Installed typically by default
              # Imported to demonstrate memory usage


# In[1]:


print('This is a "Hello World" message.')


# In[8]:


helloworld = 'This is also a "Hello World" message, but first we assigned it as a string variable called "helloworld"'
print(helloworld)


# In[4]:


longline = 'This is a really, really long string variable but we\'re going to break it up\nover 3 lines with a continuation character in the code and a newline character\nin the variable.'
print(longline)


# In[6]:


longerline = 'But hey, what if I want to actually pring any of these special characters?\nEasy!  Just escape it with a backslash (\\) like this... \\n'
print(longerline)


# In[9]:


concatenated_string = 'This is another really long string but I\'m going to format it\n' +                       'such that my variables are easily readable by someone scanning\n' +                       'through my code.'
print(concatenated_string)


# In[10]:


type(concatenated_string)


# In[13]:


print(math.pi)


# In[14]:


precise_pi = math.pi
print(precise_pi)
int8_pi = numpy.int8(precise_pi)
print(int8_pi)


# In[18]:


# Various precisions of pi and memory usage
#Signed integers (positive or negative)
print('Signed integers')
int8_pi = numpy.int8(math.pi * 10**1) #(-128 to 127)
print('int8_pi   consumes ' + str(sys.getsizeof(int8_pi)) + ' bytes ' +       'and represents pi as: ' + str(int8_pi / 10**1))
int16_pi = numpy.int16(math.pi * 10**4) #(-32768 to 32767)
print('int16_pi  consumes ' + str(sys.getsizeof(int16_pi)) + ' bytes ' +       'and represents pi as: ' + str(int16_pi / 10**4))
int32_pi = numpy.int32(math.pi * 10**8) #(-2147483648 to 2147483647)
print('int32_pi  consumes ' + str(sys.getsizeof(int32_pi)) + ' bytes ' +       'and represents pi as: ' + str(int32_pi/10**8))
int64_pi = numpy.int64(math.pi * 10**16) #(-9223372036854775808 to 9223372036854775807)
print('int64_pi  consumes ' + str(sys.getsizeof(int64_pi)) + ' bytes ' +       'and represents pi as: ' + str(int64_pi / 10**16))

#Unsigned integers (positive-only)
print('\nUnsigned integers')
uint8_pi = numpy.uint8(math.pi * 10**1) #(0 to 255)
print('uint8_pi  consumes ' + str(sys.getsizeof(uint8_pi)) + ' bytes ' +       'and represents pi as: ' + str(uint8_pi / 10**1))
uint16_pi = numpy.uint16(math.pi * 10**4) #(0 to 65535)
print('uint16_pi consumes ' + str(sys.getsizeof(uint16_pi)) + ' bytes ' +       'and represents pi as: ' + str(uint16_pi / 10**4))
uint32_pi = numpy.uint32(math.pi * 10**9) #(0 to 4294967295)
print('uint32_pi consumes ' + str(sys.getsizeof(uint32_pi)) + ' bytes ' +       'and represents pi as: ' + str(uint32_pi / 10**9))
uint64_pi = numpy.uint64(math.pi * 10**16) #(0 to 18446744073709551615)
print('uint64_pi consumes ' + str(sys.getsizeof(uint64_pi)) + ' bytes ' +       'and represents pi as: ' + str(uint64_pi / 10**16))


# In[19]:


# Extend beyond allowable range of int8

int8_extended = numpy.int8(math.pi * 10**2) #(-128 to 127)
print(int8_extended)
print('int8_pi   consumes ' + str(sys.getsizeof(int8_extended)) + ' bytes ' +       'and represents pi as: ' + str((int8_extended + 256) / 10**2))


# In[20]:


# Extend beyond allowable range of int8

int8_extended = numpy.int8(math.pi * 10**2) #(-128 to 127)
print(int8_extended + 256)
print('int8_pi   consumes ' + str(sys.getsizeof(int8_extended)) + ' bytes ' +       'and represents pi as: ' + str((int8_extended + 256) / 10**2))


# In[23]:


#Floats (decimal precision)
print('Floats')
float16_pi = numpy.float16(math.pi) #(0 to 255)
print('float16_pi consumes ' + str(sys.getsizeof(float16_pi)) + ' bytes ' +       'and represents pi as: ' + str(float16_pi))
float32_pi = numpy.float32(math.pi) #(0 to 65535)
print('float32_pi consumes ' + str(sys.getsizeof(float32_pi)) + ' bytes ' +       'and represents pi as: ' + str(float32_pi))
float64_pi = numpy.float64(math.pi) #(0 to 4294967295)
print('float64_pi consumes ' + str(sys.getsizeof(float64_pi)) + ' bytes ' +       'and represents pi as: ' + str(float64_pi))


# In[24]:


# Efficiently calculate the circumference of the Earth using
#  different precisions of pi

earth_radii = numpy.array([6353,6384])  #The earth is an oblate-spheroid, its
                                        #radius actually increases from pole to
                                        #equator.  Define an array with the
                                        #minimum (pole) and maximum (equator) radii
print('The range of radii for the oblate-spheroid Earth is between:\n' +       '                                                             ' +       str(earth_radii[0]) + 'km and ' + str(earth_radii[1]) + 'km')
earth_radius = numpy.mean(earth_radii)  #Simply use the mean of the radii
print('The calculated mean radius of the earth is:\n' +       '                                                             ' +       str(earth_radius) + 'km')
#Floats (decimal precision)
float16_pi = numpy.float16(math.pi) #(0 to 255)
float16_circ = 2 * float16_pi * earth_radius
print('Using ' + str(float16_pi) + ', the calculated mean circumference of the earth is:\n' +       '                                                             ' +       str(float16_circ) + 'km')
float32_pi = numpy.float32(math.pi) #(0 to 65535)
float32_circ = 2 * float32_pi * earth_radius
print('Using ' + str(float32_pi) + ', the calculated mean circumference of the earth is:\n' +       '                                                             ' +       str(float32_circ) + 'km')
float64_pi = numpy.float64(math.pi) #(0 to 4294967295)
float64_circ = 2 * float64_pi * earth_radius
print('Using ' + str(float64_pi) + ', the calculated mean circumference of the earth is:\n' +       '                                                             ' +       str(float64_circ) + 'km')


# In[25]:


print('The difference between float16 and float32 is: ' + str(abs(float16_circ-float32_circ)))
print('The difference between float16 and float64 is: ' + str(abs(float16_circ-float64_circ)))
print('The difference between float32 and float64 is: ' + str(abs(float32_circ-float64_circ)))


# In[26]:


# Included modules (shortened version)
import numpy as np         # conda install numpy
                           # Imported to express various data types
import math                # Installed typically by default
                           # Imported to play with pi to double precision
from sys import getsizeof  # Installed typically by default
                           # Imported to demonstrate memory usage


# In[27]:


#Floats (decimal precision)
print('Floats')
float16_pi = np.float16(math.pi) #(0 to 255)
print('float16_pi consumes ' + str(getsizeof(float16_pi)) + ' bytes ' +       'and represents pi as: ' + str(float16_pi))
float32_pi = np.float32(math.pi) #(0 to 65535)
print('float32_pi consumes ' + str(getsizeof(float32_pi)) + ' bytes ' +       'and represents pi as: ' + str(float32_pi))
float64_pi = np.float64(math.pi) #(0 to 4294967295)
print('float64_pi consumes ' + str(getsizeof(float64_pi)) + ' bytes ' +       'and represents pi as: ' + str(float64_pi))


# In[ ]:




