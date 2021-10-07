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


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = ['Muskmellon', 'Casaba', "Crenshaw", "Yellow_Watermelon"]
    print(all_melon_types)  

    return all_melon_types

#call all_melon_types
our_melons = make_melon_types()


#add melon types each with their attributes
muskmellon = MelonType("musk", 1998, "green", True, True, "Muskmellon")
casaba = MelonType("cas", 2003, "orange",False, False, "Casaba")
crenshaw = MelonType("cren", 1996, "green", False, False, "Crenshaw")
yellow_watermelon = MelonType("yw", 2013,"yellow",False, True, "Yellow_Watermelon")

print(muskmellon.color)

#add all pairings
muskmellon.add_pairing('mint')


def print_pairing_info(all_melon_types):
    """Prints information about each melon type's pairings."""
    for melon_type in all_melon_types:
        # print melon type
        print(f"For {melon_type}, it's pairings are:")
         #for loop for pairings
        for pair in {melon_type}.lower().pairings:
            print(pair)
        
        # pairings doesn't change so it's outside of the {}


print_pairing_info(our_melons)

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



