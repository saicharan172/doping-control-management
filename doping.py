from datetime import datetime

class Athlete:
    def __init__(self, name, sport):
        self.name = name
        self.sport = sport
        self.tests = []

    def add_test(self, test):
        self.tests.append(test)

    def __str__(self):
        return f'Athlete: {self.name}\nSport: {self.sport}\nTests: {len(self.tests)}'


class Test:
    def __init__(self, date, result):
        self.date = date.strftime('%Y-%m-%d')  
        self.result = result

    def __str__(self):
        return f'Test Date: {self.date}\nResult: {self.result}'


class DopingControl:
    def __init__(self):
        self.athletes = {}

    def add_athlete(self, name, sport):
        if name not in self.athletes:
            self.athletes[name] = Athlete(name, sport)
            print(f'Athlete {name} added successfully.')
        else:
            print(f'Athlete {name} already exists.')

    def record_test(self, name):
        if name in self.athletes:
            while True:
                date_str = input("Enter test date (YYYY-MM-DD): ")
                try:
                   
                    date = datetime.strptime(date_str, '%Y-%m-%d')
                    break  
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")

            while True:
                result = input("Enter test result (Positive/Negative): ").strip().lower()
                if result in ['positive', 'negative']:
                    test = Test(date, result.capitalize())  
                    self.athletes[name].add_test(test)
                    print(f'Test recorded for {name}.')
                    break  
                else:
                    print("Invalid result. Please enter 'Positive' or 'Negative'.")
        else:
            print(f'Athlete {name} not found.')

    def view_results(self, name):
        if name in self.athletes:
            athlete = self.athletes[name]
            print(athlete)
            for test in athlete.tests:
                print(test)
        else:
            print(f'Athlete {name} not found.')


def main():
    control_system = DopingControl()

    while True:
        print("\nDoping Control Management System")
        print("1. Add Athlete")
        print("2. Record Test")
        print("3. View Results")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")

        if choice == '1':
            name = input("Enter athlete's name: ")
            sport = input("Enter athlete's sport: ")
            control_system.add_athlete(name, sport)

        elif choice == '2':
            name = input("Enter athlete's name: ")
            control_system.record_test(name)

        elif choice == '3':
            name = input("Enter athlete's name: ")
            control_system.view_results(name)

        elif choice == '4':
            print("Exiting the system.")
            break

        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()



