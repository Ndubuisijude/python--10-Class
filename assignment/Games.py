"""
creating a class game called sport and no in a teams and team constructor
"""
class Games:
    # constructor
    def __init__(self, name, num_teams, num_in_team):
        self.name = name
        self.num_teams = num_teams
        self.num_in_team = num_in_team

    def display_info(self):
        print(f"Sport: {self.name}")
        print(f"Number of Teams: {self.num_teams}")
        print(f"Number of Players in each Team: {self.num_in_team}")
        print("-" * 30)


# Creating objects
football = Games("Football", 2, 11)
basketball = Games("Basketball", 2, 5)
rugby = Games("Rugby", 2, 15)
table_tennis = Games("Table Tennis", 2, 1)

# Displaying info
football.display_info()
basketball.display_info()
rugby.display_info()
table_tennis.display_info()