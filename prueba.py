def run():
    #for i in range(1000):
     #   if i % 2 != 0:
      #      continue
       # print(i)
    #name = input("what are you name: ")
    #for i in name:
        #if i == "o":
         #   break
        #print(i)
    LIMITE = 1000
    count = 0
    while count < 100:
        count += 1
        if count % 2 != 0:
            print("este numero es impar " + str(count))
            continue
        else:
            print("este numero es par " + str(count))
        


if __name__ == "__main__":
    run()