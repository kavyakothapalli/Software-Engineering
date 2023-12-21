print("Welcome to weather prediction")
T = float(input("Enter the temperature:"))
H = float(input("Enter Humidity:"))
wind =float(input("Enter wind speed:"))
W=0.5*(T*T)-0.2*(H)+(0.1*wind)-15
if W>300:
    print("prediction:Sunny")
elif W<=300 and W>200:
    print("prediction:Cloudy")
elif W<=200 and W>100:
    print("prediction:Rainy")
elif W<=100:
    print("prediction:Stormy")
print(W)
a = open("weather.txt","r")
print(a.read())
