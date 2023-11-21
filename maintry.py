class User:
    def __init__(self, name, interests):
        self.name = name
        self.interests = interests


class Mentor(User):
    def __init__(self, name, interests):
        super().__init__(name, interests)


class Mentee(User):
    def __init__(self, name, interests):
        super().__init__(name, interests)


class Match:
    def __init__(self, mentor, mentee):
        self.mentor = mentor
        self.mentee = mentee


class MatchMaker:
    def __init__(self, mentors, mentee):
        self.matches = []

        for mentor in mentors:
            for interest in mentor.interests:
                if interest in mentee.interests:
                    match = Match(mentor, mentee)
                    self.matches.append(match)
                    break


def register_mentee():
    mentee_name = input("Enter the name of the mentee: ")
    mentee_interests = []

    print("Enter the interests of the mentee (enter q to stop): ")
    while True:
        mentee_interest = input()
        if mentee_interest == "q":
            break
        mentee_interests.append(mentee_interest)

    with open("mentees.txt", "a") as mentee_file:
        mentee_file.write(f"{mentee_name} {' '.join(mentee_interests)}\n")
        print("Mentee details saved successfully!")


def register_mentor():
    mentor_name = input("Enter the name of the mentor: ")
    mentor_interests = []

    print("Enter the interests of the mentor (enter q to stop): ")
    while True:
        mentor_interest = input()
        if mentor_interest == "q":
            break
        mentor_interests.append(mentor_interest)

    with open("mentors.txt", "a") as mentor_file:
        mentor_file.write(f"{mentor_name} {' '.join(mentor_interests)}\n")
        print("Mentor details saved successfully!")


def display_mentor_list(mentors):
    for mentor in mentors:
        print(f"Mentor: {mentor.name}, Interests: {' '.join(mentor.interests)}")


def find_suitable_mentor(mentors, mentee):
    with open("mentees.txt") as mentee_file:
        mentee_names = [line.split()[0] for line in mentee_file]

    if mentee.name not in mentee_names:
        print("Kindly register first!")
        return

    suitable_mentors = []
    max_interest_matches = 0

    for mentor in mentors:
        interest_matches = sum(interest in mentee.interests for interest in mentor.interests)

        if interest_matches > 0:
            if interest_matches > max_interest_matches:
                max_interest_matches = interest_matches
                suitable_mentors = [Match(mentor, mentee)]
            elif interest_matches == max_interest_matches:
                suitable_mentors.append(Match(mentor, mentee))

    if not suitable_mentors:
        print("No suitable mentors found for the given mentee.")
    else:
        print(f"Suitable mentors for {mentee.name} based on matching interests are:")
        for match in suitable_mentors:
            print(match.mentor.name)


def upcoming_journals():
    print("IJAC 2023: International Journal of Advances in Chemistry")
    print("BCP 2022: Journal of Biochemistry and Physiology")
    print("AET 8/2 2022: CfP: Acta Economica Et Turistica journal (8/2, 2022), including special thematic interests")
    print("Paladyn, Journal of Behavioral Robotics 2022: Recent Advancements in the Role of Robotics in Smart Industries and Manufacturing Units")
    print("Spring 2022: Call for Paper: Innovative Computing (ICR) international journal1")


def main():
    print("Welcome to the Mentor-Mentee Matching Chat Bot!")

    mentors = []

    with open("mentors.txt") as file:
        for line in file:
            data = line.split()
            name = data[0]
            interests = data[1:]
            mentor = Mentor(name, interests)
            mentors.append(mentor)

    if not mentors:
        print("No mentors found!")

    while True:
        print("\nMenu Options:")
        print("1. Register Mentee")
        print("2. Register Mentor")
        print("3. Display Available Mentors")
        print("4. Find Suitable Mentor for a Mentee")
        print("5. Display Upcoming Journals")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_mentee()
        elif choice == "2":
            register_mentor()
        elif choice == "3":
            display_mentor_list(mentors)
        elif choice == "4":
            mentee_name = input("Enter the name of the mentee: ")
            mentee_interests = []

            print("Enter the interests of the mentee (enter q to stop): ")
            while True:
                mentee_interest = input()
                if mentee_interest == "q":
                    break
                mentee_interests.append(mentee_interest)

            mentee = Mentee(mentee_name, mentee_interests)
            find_suitable_mentor(mentors, mentee)
        elif choice == "5":
            upcoming_journals()
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
