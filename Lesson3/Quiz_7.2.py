#Funcao qual e o premio
def which_prize(points):
    """Qual e o premio"""

    if 0 <= points <= 50:
        print("Congratulations! You have won a A wooden rabbit!")
    elif 151 <= points <= 180:
        print("Congratulations! You have won a A wafer-thin mint!")
    elif 181 <= points <= 200:
        print("Congratulations! You have won a A penguin!")
    else:
        print("Oh dear, no prize this time.")
    
which_prize(50)
which_prize(150)
which_prize(180)
which_prize(200)