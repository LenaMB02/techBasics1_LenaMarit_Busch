# calculator.py: calculation logic for the Tennis LK Calculator
# Rules based on the official DTB regulations:
# https://www.tennis.de/spielen/ranglisten-und-leistungsklasse/infos-faq.html

WEEKLY_DECAY_VALUE = 0.025  # weekly "motivation surcharge" (applies to everyone)
                            # independent of match results


def calculate_hurdle(winner_lk: float) -> float:
    """
    Calculates the hurdle H.
    H always depends on the winner's LK, never on the loser's LK.

    H = 10 * (30 - LK)                                          if LK >= 10
    H = 10*(30-LK) + (6435/289) * ((20*(5-LK)) / LK^2 + 1)      if LK < 10
    """
    if winner_lk >= 10.0:
        hurdle = 10.0 * (30.0 - winner_lk)
    else:
        hurdle = 10.0 * (30.0 - winner_lk) + (6435.0 / 289.0) * (
            (20.0 * (5.0 - winner_lk)) / (winner_lk ** 2) + 1.0
        )
    return hurdle


def calculate_points(d: float) -> float:
    """
    Calculates the points P earned for a win.
    d = LK difference from winner to loser (d = winner_lk - loser_lk)

    P = 10                              if d <= -4
    P = 1.25*d^3 + 15*d^2 + 60*d + 90   if -4 < d <= -2
    P = 15*d + 50                       if -2 < d <= 4
    P = -3.75*d^2 + 45*d - 10           if 4 < d <= 6
    P = 125                             if d > 6
    """
    if d <= -4.0:
        points = 10.0
    elif d <= -2.0:
        points = 1.25 * (d ** 3) + 15.0 * (d ** 2) + 60.0 * d + 90.0
    elif d <= 4.0:
        points = 15.0 * d + 50.0
    elif d <= 6.0:
        points = -3.75 * (d ** 2) + 45.0 * d - 10.0
    else:
        points = 125.0
    return points


def calculate_modifier(match_type: str) -> float:
    """Calculates the modifier G depending on the match type."""
    if match_type == "Team Match (League)":
        g = 1.1
    else:
        g = 1.0
    return g


def calculate_new_lk(own_lk: float, opponent_lk: float, won: bool, match_type: str, weekly_decay: bool) -> tuple[float, float]:
    """
    Calculates the new LK for the player with the value 'own_lk'.

    - Only the winner's LK improves after a match.
    - The loser's LK does not change because of the match itself.
    - The weekly "motivation surcharge" (+0.025) is the only thing that
      worsens everyone's LK over time, independent of match results.
    """
    if won:
        winner_lk = own_lk
        loser_lk = opponent_lk

        d = winner_lk - loser_lk
        p = calculate_points(d)
        g = calculate_modifier(match_type)
        h = calculate_hurdle(winner_lk)  # H uses the winner's LK
        v = g * (p / h)

        new_lk = own_lk - v
    else:
        # A loss does not change the LK by itself
        v = 0.0
        new_lk = own_lk

    if weekly_decay:
        new_lk += WEEKLY_DECAY_VALUE

    return new_lk, v
