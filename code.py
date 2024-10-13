

import csv
import matplotlib.pyplot as plt

years = []
population_data = {
    'Tamil Nadu': [],
    'Karnataka': [],
    'Kerala': [],
    'Andhra Pradesh': [],
    'Telangana': []
}

with open(r'Python_mini_project\Population.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        years.append(int(row['Year']))
        for state in population_data.keys():
            population_data[state].append(float(row[state]))

states = list(population_data.keys())
population_2020 = [population_data[state][years.index(2020)] for state in states]  # Data for 2020

plt.bar(states, population_2020, color=['blue', 'green', 'red', 'orange', 'purple'])
plt.title('Population of South Indian States (2020)')
plt.xlabel('State')
plt.ylabel('Population (Millions)')
plt.show()

plt.hist(population_2020, bins=5, edgecolor='black', color='skyblue')
plt.title('Population Distribution in South Indian States (2020)')
plt.xlabel('Population (Millions)')
plt.ylabel('Frequency')
plt.show()


for state, populations in population_data.items():
    plt.plot(years, populations, label=state, marker='o')

plt.title('Population Trends of South Indian States (2010-2025)')
plt.xlabel('Year')
plt.ylabel('Population (Millions)')
plt.legend()
plt.grid(True)
plt.show()


plt.pie(population_2020, labels=states, autopct='%1.1f%%', colors=['blue', 'green', 'red', 'orange', 'purple'])
plt.title('Population Distribution in South Indian States (2020)')
plt.show()
