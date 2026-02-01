class Pet:
    # Allowed pet types
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    # Class-level list of all pets
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

        # If an owner is provided, register this pet with them
        if owner is not None:
            owner.add_pet(self)

    def __repr__(self):
        return f"<Pet name={self.name}, type={self.pet_type}, owner={self.owner.name if self.owner else None}>"


class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        """Return all pets belonging to this owner"""
        return self._pets

    def add_pet(self, pet):
        """Validate and add a Pet instance to this owner"""
        if not isinstance(pet, Pet):
            raise Exception("Can only add Pet instances")
        pet.owner = self
        self._pets.append(pet)

    def get_sorted_pets(self):
        """Return pets sorted by name"""
        return sorted(self._pets, key=lambda pet: pet.name)

    def __repr__(self):
        return f"<Owner name={self.name}>"

