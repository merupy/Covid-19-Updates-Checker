from apifetch import covid_nepal , covid_international


print ("\t\tCovid-19 Update")
def enter():
    user = input ("\n\nType 1 to get update of Nepal \nType 2 to get update of the world \nType 3 to exit:\n ")
    print (user)
    if user == '1':
        covid_nepal()
        enter()
    elif user == '2':
        covid_international()
        enter()
    elif user == '3':
        print ("Thank you! We will get updated everytime")
    else:
        print("Invalid Input! Please try again")
        enter()
enter()