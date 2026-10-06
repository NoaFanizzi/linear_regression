import csv

name = input("Enter value: ")

def estimate_price(theta0, theta1, mileage):
  return theta0 + (theta1 * mileage)

def main():
    print(estimate_price(10, 15, 3000))

if __name__ == "__main__":
    main()
