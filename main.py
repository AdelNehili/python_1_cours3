def exo_rappel():
    my_int = 9
    my_float = 3.5

    is_spicy = True
    is_sweet = True
    is_sour = False

    do_you_like_v1 = (is_spicy and is_sweet) or is_sour
    do_you_like_v2 = (is_spicy * is_sweet) + is_sour

    pretty_sentence = f"""En résumé:
        -my_int : {my_int}
        -my_float : {my_float}
        Sachant que mon repas est:
            -is_spicy : {is_spicy}
            -is_sour : {is_sour}
            -is_sweet : {is_sweet}
            -do_you_like_v1 : {do_you_like_v1}
            -do_you_like_v2 : {do_you_like_v2}
    """+"_"*50

    print(pretty_sentence)


    is_spicy = False
    is_sweet = False
    is_sour = False

    if is_spicy==True:
        print("╰(*°▽°*)╯ : UMAI!!")
    elif is_sweet==True:
        print("(*￣3￣)╭ : Miam miam")
    elif is_sour==True:
        print("(* ￣︿￣) : beurk")
    else:
        print("(╯‵□′)╯︵┻━┻ : JE SAIS PAS!!")
exo_rappel()