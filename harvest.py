############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code

#add melon types each with their attributes
muskmelon = MelonType("musk", 1998, "green", True, True, "Muskmellon")
casaba = MelonType("cas", 2003, "orange",False, False, "Casaba")
crenshaw = MelonType("cren", 1996, "green", False, False, "Crenshaw")
yellow_watermelon = MelonType("yw", 2013,"yellow",False, True, "Yellow_Watermelon")

def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    all_melon_types.append(muskmelon.name)
    all_melon_types.append(casaba.name)
    all_melon_types.append(crenshaw.name)
    all_melon_types.append(yellow_watermelon.name)

    print(all_melon_types)

make_melon_types()

#add all pairings
muskmelon.add_pairing('mint')
casaba.add_pairing('mint')
casaba.add_pairing('strawberry')
crenshaw.add_pairing('prosciutto')
yellow_watermelon.add_pairing('ice cream')

def print_pairing_info(all_melon_types):
    """Prints information about each melon type's pairings."""
    for melon in all_melon_types:
        # print melon type
        print(f'Parings for {melon.name} are:')
         #for loop for pairings
        for pairing in melon.pairings:
            print (f'{pairing}')
        
all_melon_types = [muskmelon, casaba, crenshaw, yellow_watermelon]
print_pairing_info(all_melon_types)

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_dict = {}
    for melon in melon_types:
        melon_dict[melon.code] = [melon]




############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, name, type_code, shape, color, field, harvested_by):
        self.name = name
        self.type = type_code
        self.shape = shape
        self.color = color
        self.field = field
        self.harvested_by = harvested_by

    def is_sellable(self, shape, color, field):

        if shape >= 5 and color >= 5 and field != 3:
            self.is_sellable = True
        else: 
            self.is_sellable = False

melon1 = Melon("melon1", yellow_watermelon, 8, 7, 2, "Sheila")
melon2 = Melon("melon2", yellow_watermelon, 3, 4, 2, "Sheila")
melon1.is_sellable(8, 7, 2)
melon2.is_sellable(3, 4, 2)
print(melon1.is_sellable == True)
print(melon2.is_sellable == True)

def make_melons(melon_types):
    """Returns a list of Melon objects."""
    
    melons = []
    for melon in melon_types:
        melons.append(melon)

melons = [melon1, melon2]

print(melons)

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    sellable = []
    for melon in melons:
        if melon.is_sellable == True:
            sellable.append(melon)
            print(f'{melon.name} is sellable')

get_sellability_report(melons)

