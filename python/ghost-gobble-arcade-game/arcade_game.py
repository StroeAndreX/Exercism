def eat_ghost(power_pellet_active, touching_ghost):
    return True if (power_pellet_active and touching_ghost) else False

def score(touching_power_pellet, touching_dot):
    return True if(touching_power_pellet or touching_dot) else False

def lose(power_pellet_active, touching_ghost):
    return True if(power_pellet_active == False and touching_ghost) else False

def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    return True if(has_eaten_all_dots and lose(power_pellet_active, touching_ghost) == False) else False
