import csv
def main():
    #write your code below this line
    nameFile = input("Name of the file:")
    with open(nameFile) as f:
      reader = csv.reader(f,delimiter=',')
      for row in reader:
        if(int(row[1])==1):
          print("%s, age: %s year"%(row[0],row[1]))
        else:
          print("%s, age: %s years"%(row[0],row[1]))

if __name__ == '__main__':
    main()
