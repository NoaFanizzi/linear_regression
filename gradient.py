import csv

def estimate_price(theta0, theta1, mileage):
    return theta0 + (theta1 * mileage)

def perform_gradient():
    with open('data.csv', 'r') as file:
      csvFile = list(csv.DictReader(file))

      mileages = [float(row["km"]) for row in csvFile]
      prices = [float(row["price"]) for row in csvFile]

      theta0 = 0
      theta1 = 0
      learning_rate = 0.1
      m = len(csvFile)
      min_mileage = min(mileages)
      max_mileage = max(mileages)
      normalized_mileages = [(mileage - min_mileage) / (max_mileage - min_mileage) for mileage in mileages]

      for _ in range(1000):
        sum0 = 0
        sum1 = 0
        for mileage, price in zip(normalized_mileages, prices):
          error = estimate_price(theta0, theta1, mileage) - price
          sum0 += error
          sum1 += error * mileage
        
        tmp_th0 = learning_rate * (1/m) * sum0
        tmp_th1 = learning_rate * (1/m) * sum1

        theta0 -= tmp_th0
        theta1 -= tmp_th1
      
        print(theta0, theta1)

def main():
  perform_gradient()

if __name__ == "__main__":
    main()
