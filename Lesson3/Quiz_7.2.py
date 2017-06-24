#Funcao qual e o premio
def which_prize(points):
    """Qual e o premio"""

    if 0 <= points <= 50:
        message = "Congratulations! You have won a wooden rabbit!"
    elif 151 <= points <= 180:
        message = "Congratulations! You have won a wafer-thin mint!"
    elif 181 <= points <= 200:
        message = "Congratulations! You have won a penguin!"
    else:
        message = "Oh dear, no prize this time."

    return message

#tests
print(which_prize(12))
print(which_prize(149))
print(which_prize(164))
print(which_prize(194))

#-----------------------------------------------------------------------------------

#Funcao qual e o premio
def which_prize2(points):
    """Retorna a mensagem do prêmio adquirido, dado um número de pontos
    """
    if points <= 50:
        return "Congratulations! You have won a wooden rabbit!"
    elif points <= 150:
        return "Oh dear, no prize this time."
    elif points <= 180:
        return "Congratulations! You have won a wafer-thin mint!"
    else:
        return "Congratulations! You have won a penguin!"
#tests
print(which_prize2(12))
print(which_prize2(149))
print(which_prize2(164))
print(which_prize2(194))