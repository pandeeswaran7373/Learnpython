travel_log = [

]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country_visited,visits_count,cities_visited):
    new_country={}
    new_country["country"]=country_visited
    new_country["visits"]=visits_count
    new_country["cities"]=cities_visited
    travel_log.append(new_country)

#🚨 Do not change the code below
print("Welcome to travel Log Dictionary\n")
country_name=input("Enter the name of you visited the country: ")
num_of_visit=input("Enter the count of visit the country: ")
cities_name=input("Enter the cities visted the country: ").split(",")

add_new_country(country_visited=country_name, visits_count=num_of_visit,cities_visited=cities_name)
print(travel_log)
