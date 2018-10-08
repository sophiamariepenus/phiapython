import sys

numwind = float(sys.argv[1])

if numwind >= 220:
    print("SUPER TYPHOON")
elif numwind >= 118:
    print("TYPHOON")
elif numwind >= 89:
    print("SEVERE TROPICAL STORM")
elif numwind >= 62:
    print("TROPICAL STORM")
elif numwind <= 61:
    print("TROPICAL DEPRESSION")