"""
License: Apache
Organization: UNIR
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False
DEFAULT_OUTPUT_FILENAME = "sorted_words.txt"
DEFAULT_LANGUAGE = "es"  # Idioma predeterminado (español)

# Diccionarios de mensajes
MESSAGES = {
    "es": {
        "file_required": "Se debe indicar el fichero como primer argumento",
        "duplicates_option": "El segundo argumento indica si se quieren eliminar duplicados",
        "reading_file": "Se leerán las palabras del fichero",
        "file_not_exist": "El fichero no existe",
    },
    "en": {
        "file_required": "The file must be specified as the first argument",
        "duplicates_option": "The second argument indicates whether to remove duplicates",
        "reading_file": "The words from the file will be read",
        "file_not_exist": "The file does not exist",
    }
}
#este comentario lo puso Camilo
def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"Cannot sort {type(items)}")

    return sorted(items, reverse=(not ascending))


def remove_duplicates_from_list(items):
    return list(set(items))


def save_to_file(filename, items):
    with open(filename, "w") as file:
        for item in items:
            file.write(f"{item}\n")


if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    language = DEFAULT_LANGUAGE

    # Comprobamos si se han pasado 4 argumentos (incluyendo el idioma)
    if len(sys.argv) == 4:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
        language = sys.argv[3].lower()  # Idioma seleccionado (es/en)
    else:
        print(MESSAGES[language]["file_required"])
        print(MESSAGES[language]["duplicates_option"])
        sys.exit(1)

    print(f"{MESSAGES[language]['reading_file']} {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"{MESSAGES[language]['file_not_exist']} {filename}")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    sorted_list = sort_list(word_list)
    print(sorted_list)

    output_filename = DEFAULT_OUTPUT_FILENAME
    save_to_file(output_filename, sorted_list)
    print(f"Las palabras ordenadas se han guardado en el archivo {output_filename}")
    print(f"Esto es una prueba de Camilo Rojas")
