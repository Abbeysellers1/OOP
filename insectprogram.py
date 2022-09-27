import insectclass as i

#i is fromt the file insectclass and insect is from the name of the class fromt the other file

housefly= i.insect(2,4)

mosquito=i.insect(6,8)

housefly.flight_length()

mosquito.flight_length()

print('the housefly can fly up to', housefly.get_flight(), 'miles')
print('the mosquito can fly up to', mosquito.get_flight(), 'miles')
