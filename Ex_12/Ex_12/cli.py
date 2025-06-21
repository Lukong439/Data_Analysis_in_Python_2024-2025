import sys
import numpy as np

def main():
    if len(sys.argv) != 2:
        print("Usage: mycos <number>")
        sys.exit(1)
    
    try:
        x = float(sys.argv[1])
    except ValueError:
        print("Please enter a valid number.")
        sys.exit(1)

    result = np.cos(x)
    print(result,)

if __name__ == "__main__":
    main()