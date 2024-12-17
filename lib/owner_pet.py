class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __repr__(self):
        return self.name
    
    def __init__(self,name,pet_type,owner=None):
        self.name = name
        self.pet_type = pet_type
        self._owner = owner
        self.__class__.all.append(self)

    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self,value):
        if value in self.PET_TYPES:
            self._pet_type = value
        else:
            raise Exception
    
    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self,value):
        if isinstance(value, Owner):
            self._owner = value
        else:
            raise Exception
        
class Owner:
    def __repr__(self):
        return self._name
    
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
        #if type(pet) == Pet:
            pet.owner = self
        else:
            raise Exception
    
    def get_sorted_pets(self):
        return sorted(Pet.all, key=lambda n: n.name)


# import ipdb 
# pet_1 = Pet("centipede", "rodent")
# pet_2 = Pet("mouse", "rodent")
# pet_3 = Pet("yuck", "rodent")
# owner = Owner("Me")

# print(pet_1._pet_type)

# #ipdb.set_trace()