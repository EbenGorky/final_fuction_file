def quantization_of_charges(e=1.6*10**-19):
	print("formula; Q=±ne")
	print("choice=1if n and e are given,choice=2 if Q and e are given")
	choice=int(input("enter your chice"))
	if choice not in(1,2):
		print("enter a valid choice")
	elif choice==1:
		n=int(input("enter the value of n:"))
		q=n*int(e)
		print("Q=",q)
	elif choice==2:
		q=float(input("enter the value of Q:"))
		n=Q/int(e)
		print("n=",n)

import math
from math import *
#thurmesh
def quantization_of_charge__q(m):
        return("Q=",float(m)*(1.6*10**(-19)),"N\nFormula:Q=±ne")

def number_of_electronsI_in_given_charge__n(m):
        return("n=",float(m)/(1.6*10**(-19)),"N\nFormula:n=Q/e")

def Force_between_two_charges__f(m,n,o):
        return("F=",(float(m)*float(n)/float(o)**2)*9*10**9,"N\nFormula:F=kxq1xq2/r^2")

def distance_between_two_charge__fr(m,n,o):
        return("r=",math.sqrt((float(m)*float(n)*9)*10**9/float(o)),"m\nFormula:r=(q1xq2xk/F)^1/2")

def first_charge__q1(m,n,o):
        return("q1=",float(m)**2*float(o)/(float(n)*9*10**9),"C\nFormula:q1=Fxr^2/q2xk")

def second_charge__q2(m,n,o):
        return("q2=",float(n)**2*float(o)/(float(m)*9*10**9),"C\nFormula:q2=Fxr^2/q1xk")


#eben
def Maximum_amplitude_of_wave_interference__a(a1,a2,fi):
    A = (a1**2 + a2**2 + 2*a1*a2*cos(fi))**(1/2)
    return ('A=',A,'a1**2 + a2**2 + 2*a1*a2*cos(fi)')
