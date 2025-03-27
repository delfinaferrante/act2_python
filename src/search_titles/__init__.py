def title_large(titles):
    """ Recibe una lista de titulos y retorna la lista con mas palabras """

    words_max = -1
    title_max = " "

    for one_title in titles:
        words = len(one_title.split())
        title = one_title
        if words > words_max:
            words_max = words
            title_max = title

    return title_max