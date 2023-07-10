a=float(input("height(m): "))
b=float(input("weight(kg): "))
c=b/a**2
if c<18.5:
    print("thin")
elif 18.5<=c<=24.9:
      print("normal")
elif 25<=c<=29.9:
     print("fat")
else:
     print("pro fat")            
