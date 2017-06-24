#Funcao qual e o premio
def cylinder_surface_area(radius, height, has_top_and_bottom):
    """
    Retorna a area do cilindro

    radius: float, o raio do cilindro.
    height: float, a altura do cilindro.
    has_top_and_bottom: bool, define o tipo do cilindro
                        "True", "False" caso verdadeiro solido, caso falso oco.
    """

    if has_top_and_bottom:
        top_area = 3.14 * radius ** 2
        return (height * 6.28 * radius) + 2 * top_area
    else:
        return height * 6.28 * radius
        
print(cylinder_surface_area(2,3,True))
print(cylinder_surface_area(2,3,False))
