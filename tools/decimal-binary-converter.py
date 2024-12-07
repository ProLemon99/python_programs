while True:
  try:
    num = input("Enter Any Number: ")
    break
  except ValueError:
    print("INVALID NUMBER. PLEASE TRY AGAIN.")

print(bin(int(num)))