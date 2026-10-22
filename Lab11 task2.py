import json
f = open(r"C:\Users\Nazar\OneDrive\Desktop\cities.json", "r", encoding="utf-8")
cities = json.load(f)
f.close()
print(cities)
city = input("Введіть назву міста: ")
if city in cities:
    print("Населення:", cities[city])
else:
    print("Місто не знайдено")
for city, population in sorted(cities.items(), key=lambda x: x[1], reverse=True):
    print(city, ":", population)
city = input("Назва нового міста: ")
population = int(input("Населення: "))
cities[city] = population
f = open(r"C:\Users\Nazar\OneDrive\Desktop\cities.json", "w", encoding="utf-8")
json.dump(cities, f, ensure_ascii=False, indent=4)
f.close()