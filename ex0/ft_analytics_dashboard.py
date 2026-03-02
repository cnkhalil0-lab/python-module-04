

def get_sample_data() -> list[dict]:
    return [
        {
            "name": "alice",
            "score": 2300,
            "achievements": [
                "boss_slayer",
                "first_kill",
                "level_10",
                "boss_slayer",
                "first_kill",
            ],
            "region": "north",
            "actif": True,
        },
        {
            "name": "bob",
            "score": 1800,
            "achievements": [
                "first_kill",
                "boss_slayer",
                "level_10",
            ],
            "region": "east",
            "actif": True,
        },
        {
            "name": "charlie",
            "score": 2150,
            "achievements": [
                "level_10",
                "boss_slayer",
                "first_kill",
            ],
            "region": "central",
            "actif": True,
        },
        {
            "name": "diana",
            "score": 2050,
            "achievements": [
                "first_kill",
            ],
            "region": "south",
            "actif": False,
        },
    ]


def list_comprehensions(data: list[dict]) -> None:
    """Démontre l'utilisation des list comprehensions"""
    """ pour filtrer et transformer."""
    print("=== List Comprehension Examples ===")
    high_scorers = [p['name'] for p in data if p['score'] > 2000]
    print(f"High scorers (>2000): {high_scorers}")
    scores_doubles = [p['score'] * 2 for p in data]
    print(f"Scores doubled: {scores_doubles}")
    active_players = [p['name'] for p in data if p['actif']]
    print(f"Active players: {active_players}")


def dict_comprehensions(data: list[dict]) -> None:
    """Démontre la création de dictionnaires via les dict comprehensions."""
    print("\n=== Dict Comprehension Examples ===")
    player_scores = {p['name']: p['score'] for p in data if p['actif']}
    print(f"Player scores: {player_scores}")
    categories = {
     "high": len([p for p in data if p['score'] > 2000]),
     "medium": len([p for p in data if 1500 < p['score'] <= 2000]),
     "low": len([p for p in data if p['score'] <= 1500]),
    }
    print(f"Score categories: {categories}")
    ach_counts = {
     p['name']: len(p['achievements'])
     for p in data
     if p['actif']
    }
    print(f"Achievement counts: {ach_counts}")


def set_comprehensions(data: list[dict]) -> None:
    """Extraction de valeurs uniques (Dédoublonnage)."""
    print("\n=== Set Comprehension Examples ===")
    regions = {p['region'] for p in data if p['actif']}
    unique_players = {p['name'] for p in data}
    unique_ach = {ach for p in data for ach in p['achievements']}
    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_ach}")
    print(f"Active regions: {regions}")


def combined_analysis(data: list[dict]) -> None:
    print("\n=== Combined Analysis ===")
    all_scores = [p['score'] for p in data]
    unique_ach = {ach for p in data for ach in p['achievements']}
    total_unique = len(unique_ach)
    print(f"Total players: {len(data)}")
    print(f"Total unique achievements: {total_unique}")
    average_score = sum(all_scores) / len(data)
    print(f"Average score: {average_score:.1f}")
    top = max(data, key=lambda x: x['score'])
    print(
     f"Top performer: {top['name']} "
     f"({top['score']} points, "
     f"{len(top['achievements'])} achievements)"
    )


def fonction() -> None:
    print("=== Game Analytics Dashboard ===")
    data = get_sample_data()
    list_comprehensions(data)
    dict_comprehensions(data)
    set_comprehensions(data)
    combined_analysis(data)


if __name__ == "__main__":
    fonction()
