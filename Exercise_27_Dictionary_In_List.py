# Travel Log

my_travel_log = [
    {
        "country" : "Nepal",
        "cities_visited" : ["Kathmandu", "Pokhara", "Bardibas"],
        "times_visited" : 100,
        "Review" : "Excellent"
    },
    {
        "country" : "India",
        "cities_visited" : ["Delhi", "Banglore", "Sikkim"],
        "times_visited" : 2,
        "Review" : "Good"
    }
]


country_name = input("Enter the name of the country you recently visited:\n>> ")
times_visited = input("Enter your number of times of visit:\n>> ")
cities_visited = input("Enter the name of cities you visited (separate city with comma & space):\n>> ")
cities_visited_list = cities_visited.split(", ")
user_experience = {
    1 : "Excellent",
    2 : "Good",
    3 : "Satisfying",
    4 : "Poor"
}
user_review = int(input('''How was your experience ?
1. Excellent
2. Good
3. Satisfying
4. Poor
>> '''))


def add_new_country(name_of_the_country, number_of_times_visited, list_of_cities_visited, experience_of_the_user):
    temp = {}
    temp["country"] = name_of_the_country
    temp["times_visited"] = number_of_times_visited
    temp["cities_visited"] = list_of_cities_visited
    temp["Review"] = experience_of_the_user
    my_travel_log.append(temp)

add_new_country(country_name, times_visited, cities_visited_list, user_experience[user_review])

print(my_travel_log)