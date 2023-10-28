
def team_lineup(*players):
    national_teams = dict()

    for data in players:
        player = data[0]
        country = data[1]

        if country not in national_teams:
            national_teams[country] = []

        national_teams[country].append(player)

    sorted_teams = sorted(national_teams.items(),
                          key=lambda x: (-len(x[1]), x[0]))

    result = ""

    for country, players in sorted_teams:
        result += f"{country}:\n"
        result += "\n".join([f"  -{player}" for player in players]) + "\n"

    return result


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))

def team_lineup(*players):
    national_teams = dict()

    for data in players:
        player = data[0]
        country = data[1]

        if country not in national_teams:
            national_teams[country] = []

        national_teams[country].append(player)

    sorted_teams = sorted(national_teams.items(),
                          key=lambda x: (-len(x[1]), x[0]))

    result = ""

    for country, players in sorted_teams:
        result += f"{country}:\n"
        result += "\n".join([f"  -{player}" for player in players]) + "\n"

    return result


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))
