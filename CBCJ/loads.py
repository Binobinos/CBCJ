def load(file):
    # TODO: Сделать функцию выгрузки из файла .CBCJ
    # TODO: Написать документацию для функции
    lines = list(i.strip() for i in file.readlines())
    versions = lines[0].split(" ")[1][:-1]
    cry = False if lines[1].split("-")[1][:-1] == "F" else True
    print(versions)
    print(cry)
    if not cry:
        lines = lines[2:]
        if lines[0].startswith("dict"):
            data = dict()
        elif lines[0].startswith("list"):
            data = list()
        else:
            raise IndexError("Incorrect format")
        if type(data) == dict:
            # TODO: Написать конвертации в словарь, лист и выделить рекурсивность в строку
            print("".join(lines)[6:][:-2].split())


def dump(dict: dict):
    # TODO: Сделать функцию загрузки в файл .CBCJ
    pass


def cbcj_to_json(file):
    # TODO: Сделать функцию конвертации файла .CBCJ в .JSON
    pass


def parse_csv(str: str):
    # TODO: Сделать функцию парсинга вложенных csv форматов
    pass


def parse_json(str: str):
    # TODO: Сделать функцию парсинга вложенных json форматов
    pass


def parse_binary(str: str):
    # TODO: Сделать функцию парсинга бинарных форматов
    pass


def encryption(str: str):
    # TODO: Сделать функцию шифрования
    pass


def decryption(str: str):
    # TODO: Сделать функцию дешифрования
    pass


# пример использования
with open("example.CBCJ", "r") as file:
    a = load(file)
