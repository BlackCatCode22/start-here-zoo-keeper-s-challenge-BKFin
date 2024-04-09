from Animal import Animal
from Hyena import Hyena
from Lion import Lion
from Tiger import Tiger
from Bear import Bear

from datetime import date

# Species lists
list_of_hyenas = []
list_of_lions = []
list_of_tigers = []
list_of_bears = []

# This is needed for the calc birthday stuff.
current_date = date.today()
current_year = current_date.year

def calc_birth_date(the_season, the_years):
    year_of_birthday = int(current_year) - int(the_years)

    the_birth_day = ""

    if "spring" in the_season:
        the_birth_day = str(year_of_birthday) + "-03-21"
    elif "summer" in the_season:
        the_birth_day = str(year_of_birthday) + "-06-21"
    elif "fall" in the_season:
        the_birth_day = str(year_of_birthday) + "-09-21"
    elif "winter" in the_season:
        the_birth_day = str(year_of_birthday) + "-12-21"
    # if the birth season is unknown
    else:
        the_birth_day = str(year_of_birthday) + "-01-01"

    return the_birth_day


def process_one_line(one_line):
    # Create variables to help parse arrivingAnimals.txt
    a_species = ""
    a_sex = ""
    age_in_years = 99
    season = ""
    color = ""
    weight = ""
    origin_01 = ""
    origin_02 = ""

    # print(one_line)
    groups_of_words = one_line.strip().split(",")
    # print(groups_of_words)
    single_words = groups_of_words[0].strip().split(" ")
    age_in_years = single_words[0]
    a_sex = single_words[3]
    a_species = single_words[4]
    single_words = groups_of_words[1].strip().split(" ")
    season = single_words[2]
    color = groups_of_words[2].strip();
    weight = groups_of_words[3].strip();
    origin_01 = groups_of_words[4].strip();
    origin_02 = groups_of_words[5].strip();

    from_zoo = origin_01 + ", " + origin_02

    birth_day = calc_birth_date(season, age_in_years)

    if "hyena" in a_species:
        # Create a hyena object.
        my_hyena = Hyena("aName", "anID", birth_day, color, a_sex, weight, from_zoo, current_date)
        # fill in name and ID
        my_hyena.name = Hyena.get_hyena_name(my_hyena)
        my_hyena.animal_id = "Hy" + str(Hyena.numOfHyenas).zfill(2)
        # add to the hyena list
        list_of_hyenas.append(my_hyena)

    if "lion" in a_species:
        # Create a lion object.
        my_lion = Lion("aName", "anID", birth_day, color, a_sex, weight, from_zoo, current_date)
        # fill in name and ID
        my_lion.name = Lion.get_lion_name(my_lion)
        my_lion.animal_id = "Li" + str(Lion.numOfLions).zfill(2)
        # add to the lion list
        list_of_lions.append(my_lion)

    if "tiger" in a_species:
        # Create a lion object.
        my_tiger = Tiger("aName", "anID", birth_day, color, a_sex, weight, from_zoo, current_date)
        # fill in name and ID
        my_tiger.name = Tiger.get_tiger_name(my_tiger)
        my_tiger.animal_id = "Ti" + str(Tiger.numOfTigers).zfill(2)
        # add to the lion list
        list_of_tigers.append(my_tiger)

    if "bear" in a_species:
        # Create a lion object.
        my_bear = Bear("aName", "anID", birth_day, color, a_sex, weight, from_zoo, current_date)
        # fill in name and ID
        my_bear.name = Bear.get_bear_name(my_bear)
        my_bear.animal_id = "Be" + str(Bear.numOfBears).zfill(2)
        # add to the lion list
        list_of_bears.append(my_bear)

# Open arrivingAnimals.txt and read it one line at a time
# Open the file in read mode
file_path = r".\arrivingAnimals.txt"
with open(file_path, "r") as file:
    # Iterate through the file line by line
    for line in file:
        process_one_line(line)

# output to zooPopulation.txt in overwrite mode

file = open("zooPopulation.txt", "w")

file.write("\n")
file.write("-+- Super snazzy Zoo Population report of arriving animals! -+-")
file.write("\n\n")
file.write(f"Hyenas: {Hyena.numOfHyenas} | Lions: {Lion.numOfLions} | Tigers: {Tiger.numOfTigers} | Bears: {Bear.numOfBears}")
file.write("\n\n")
file.write(f"Total number of animals arriving: {Animal.numOfAnimals}")
file.write("\n\n")
file.write("Hyena Habitat:")
file.write("\n")
for hyena in list_of_hyenas:
    file.write("\n" + hyena.animal_id + ", " + hyena.name + "; birthdate: " + str(hyena.birth_date) + "; " + hyena.color +
          "; " + hyena.sex + "; " + hyena.weight + "; " + hyena.originating_zoo + "; arrived: " +
          str(hyena.date_arrival))
file.write("\n\n")
file.write("Lion Habitat:")
file.write("\n")
for lion in list_of_lions:
    file.write("\n" + lion.animal_id + ", " + lion.name + "; birthdate: " + str(lion.birth_date) + "; " + lion.color +
          "; " + lion.sex + "; " + lion.weight + "; " + lion.originating_zoo + "; arrived: " +
          str(lion.date_arrival))
file.write("\n\n")
file.write("Tiger Habitat:")
file.write("\n")
for tiger in list_of_tigers:
    file.write("\n" + tiger.animal_id + ", " + tiger.name + "; birthdate: " + str(tiger.birth_date) + "; " + tiger.color +
          "; " + tiger.sex + "; " + tiger.weight + "; " + tiger.originating_zoo + "; arrived: " +
          str(tiger.date_arrival))
file.write("\n\n")
file.write("Bear Habitat:")
file.write("\n")
for bear in list_of_bears:
    file.write("\n" + bear.animal_id + ", " + bear.name + "; birthdate: " + str(bear.birth_date) + "; " + bear.color +
          "; " + bear.sex + "; " + bear.weight + "; " + bear.originating_zoo + "; arrived: " +
          str(bear.date_arrival))
file.close()
