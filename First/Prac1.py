class Customer():
    def __init__(self, name, age, voter, cityList):
        self.name = name
        self.age = age
        self.voter = voter
        self.cityList = cityList
        print(type(self.cityList))

    def printAttributes(self):
        print(self.name, ' ', self.age, ' ', self.voter)
        for city in cityList:
            print(city, 'is Capital of ', self.state_dictionary(city))

    def state_dictionary(self, city):
        states = {
            "Agra": "Uttar Pradesh",
            "Mathura": "Uttar Pradesh",
            "Bangalore": "Karnataka",
            "Chennai": "Tamilnadu",
            "Kanyakumari": "Kerala"
        }
        return states.get(city, 'No Data')


cityList = ['Agra', 'Mathura', 'Bangalore', 'Kolkata', 'Chennai']
cust1 = Customer('Kapil', 28, 'Yes', cityList)
cust1.printAttributes()
