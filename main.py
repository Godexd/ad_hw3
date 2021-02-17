import hashlib
import json

from Decorator import decorator_parametrized_logger, decorator_default_logger

if __name__ == '__main__':

    @decorator_default_logger
    def CountryReaderIter_for_json(json_filename: str):
        with open(json_filename, 'r', encoding='utf8') as file:
            countries = json.load(file)
            for country in countries:
                yield country['name']['common']

    @decorator_parametrized_logger(filename='parametrized_logs.txt')
    def CountryReaderIter_for_text(text_filename: str):
        with open(text_filename, 'r', encoding='utf8') as file:
            for line in file:
                yield hashlib.md5(line.encode()).hexdigest()


    with open('output.txt', 'w', encoding='utf8') as countries_file:
        for country in CountryReaderIter_for_json('countries.json'):
            countries_file.write(f'{country}\n')

    with open('hash_logs.txt', 'w', encoding='utf8') as hash_file:
        for country in CountryReaderIter_for_text('output.txt'):
            hash_file.write(f'{country}\n')

    print('Check parametrized_logs.txt and default_logs.txt')