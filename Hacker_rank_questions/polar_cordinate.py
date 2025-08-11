import cmath,math

z= complex(input("Enter a complex number (e.g., 3+4j): "))  
result=(z.real**2)+(z.imag**2)
radius=math.sqrt(result)
ans=round(radius,3)
print(ans)
# same but in help of built in 
r=abs(z)
print(r)

# z = complex(1, 2)  
theta = cmath.phase(z)  
tan_theta = cmath.tan(theta)

print("Complex number:", z)
print("Theta (in radians):", theta)
print("Theta (in degrees):", math.degrees(theta))
print("tan(Theta):", tan_theta)



# z = complex(1,2)
# theta = cmath.phase(z)  # in radians
# print(theta)