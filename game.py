import time


class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 20
        self.energy = 50
        self.is_alive = True

    def feed(self):
        print(f"\n🍖You feed {self.name}")
        self.hunger = max(0, self.hunger - 25)
        self.energy = min(100, self.energy + 5)
        self._pass_time()

    def play(self):
        if self.energy >= 0:
            print(f"\n⚽You play with {self.name} ")
            self.happiness = min(100, self.happiness + 20)
            self.energy = max(0, self.energy - 15)
            self.hunger = min(100, self.hunger + 10)
            self._pass_time()
        else:
            print(f"{self.name} is tired and don\'t want to play")

    def rest(self):
        print(f"\n💤{self.name} is resting")
        self.energy = min(100, self.energy + 30)
        self.hunger = min(100, self.hunger + 5)
        self._pass_time()

    def _pass_time(self):

        self.happiness = max(0, self.happiness - 5)
        self._check_vital_signs()

    def _check_vital_signs(self):

        if self.hunger >= 100:
            print(f"💀{self.name} is starving...")
            self.is_alive = False
        elif self.happiness <= 0:
            print(f"📉{self.name} feel boring and it left...")
            self.is_alive = False
        elif self.energy <= 0:
            print(f"🛌{self.name} is exhausted and gets sick...")
            self.is_alive = False

    def __str__(self):
        separator = "-" * 25
        return (
        f'{separator}\n'
        f'The status of {self.name}\n'
        f"🍴hunger_value      :{self.hunger}/100\n"
        f"😊happiness_value   :{self.happiness}/100\n"
        f"🔥energy_value      :{self.energy}/100\n"
        f'{separator}'
        )



def main():
    pet_name = input("Give your pet a name: ")
    pet = VirtualPet(pet_name)

    while pet.is_alive:
        print(pet)
        print("\nselecting operation:")
        print("1. 🍖FEED")
        print("2. ⚽PLAY")
        print("3. 💤REST")
        print("4. EXIT")

        choice = input("Please enter the options (1-4): ")

        if choice == "1":
            pet.feed()
        elif choice == "2":
            pet.play()
        elif choice == "3":
            pet.rest()
        elif choice == "4":
            print("GAME OVER!")
            break
        else:
            print("Invalid inputs")

    print("\n--- GAME OVER ---")


if __name__ == "__main__":
    main()
