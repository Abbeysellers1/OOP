import insectclass as i

#i is fromt the file insectclass and insect is from the name of the class fromt the other file

housefly= i.insect()

mosquito=i.insect()

housefly.flight_length()

mosquito.flight_length()

print('the housefly can fly up to ', housefly.get_flight())
print('the mosquito can fly up to ', mosquito.get_flight())
