import random

LETTER_SCORES = {
    'А': 1, 'Б': 2, 'В': 1, 'Г': 3, 'Д': 2, 'Е': 3, 'Ё': 3, 'Ж': 5, 'З': 5, 'И': 1, 'Й': 4, 'К': 2, 'Л': 2, 'М': 2,
    'Н': 1, 'О': 1, 'П': 2, 'Р': 1, 'С': 2, 'Т': 2, 'У': 2, 'Ф': 10, 'Х': 2, 'Ц': 5, 'Ч': 5, 'Ш': 8, 'Щ': 10, 'Ъ': 10,
    'Ы': 4, 'Ь': 3, 'Э': 8, 'Ю': 8, 'Я': 3
}


def get_random_letter():
    letters = LETTER_SCORES.keys()
    converted_dictionary = list(letters)
    random_letter = random.choice(converted_dictionary)
    return random_letter


def get_word_with_letter(random_letter):
    print('Начальная буква:', random_letter)
    while True:
        answer = input(f'Введите слово на букву {random_letter}: ')
        word = answer.upper()
        if word[0] == random_letter:
            return word
        else:
            print(f"Слово должно начинаться с буквы '{random_letter}', попробуйте снова.")


def calculate_score(word):
    all_scores = []
    for i in word:
        upper_letter = i.upper()
        scores = LETTER_SCORES.get(upper_letter, 0)
        all_scores.append(scores)
    sum_score = sum(all_scores)
    return sum_score

def main():
    player_scores = [0, 0]
    count = 0
    while player_scores[0] <= 100 and player_scores[1] <= 100:
        print('Игрок', count + 1)
        letter = get_random_letter()
        word = get_word_with_letter(letter)
        scores = calculate_score(word)
        player_scores[count] += scores
        print(player_scores)
        if count == 1:
            count = 0
        else:
            count += 1
    if player_scores[0] >= player_scores[1]:
        print('Игрок 1 - победитель!')
    elif player_scores[1] >= player_scores[0]:
        print('Игрок 2 - победитель!')
    else:
        print('Ничья')


if __name__ == '__main__':
    main()