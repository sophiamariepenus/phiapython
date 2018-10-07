import sys

#(sys.argv)
num = float(sys.argv[1])
#print(num)
if(num > 220.9):
    print("SUPER TYPHOON")
elif(num >= 118.0 and num <= 220.9):
    print("TYPHOON")
elif(num >= 89.0 and num <= 117.9):
    print("SEVERE TROPICAL STORM")
elif(num >= 62.0 and num <= 88.9):
    print("TROPICAL STORM")
elif(num <= 61.9):
    print("TROPICAL DEPRESSION")