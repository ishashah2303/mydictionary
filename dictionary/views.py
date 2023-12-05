from django.shortcuts import render
import requests
import bs4

def HomeView(request):
    return render(request, 'dictionary/home.html')

# def SearchView(request):
#     word = request.GET['word']

#     response = requests.get('https://www.dictionary.com/browse/'+word)
#     response2 = requests.get('https://www.thesaurus.com/browse/'+word)

#     if response:
#         soup_1 = bs4.BeautifulSoup(response.text, 'lxml')
#         meaning = soup_1.find_all('div', {'value': '1'})
#         if meaning:
#             meaning_1 = meaning[0].getText()
#         else:
#             word = f"Sorry we couldn't find your word {word} in our records."
#             meaning_1 = ''
#     else:
#         word = f"Sorry we couldn't find your word {word} in our records."
#         meaning_1 = ''

#     if response2:
#         soup_2 = bs4.BeautifulSoup(response2.text, 'lxml')
#         synonyms = soup_2.find_all('a', {'class': 'css-1kg1yv8 eh475bn0'})
#         main_synonym_list = [b.text.strip() for b in synonyms]

#         antonyms = soup_2.find_all('a', {'class': 'css-15bafsg eh475bn0'})
#         main_antonym_list = [c.text.strip() for c in antonyms]
#     else:
#         main_synonym_list = []
#         main_antonym_list = []

#     results = {
#         'word': word,
#         'meaning': meaning_1,
#     }

#     return render(request, 'dictionary/search.html', {'main_synonym_list': main_synonym_list, 'main_antonym_list': main_antonym_list, 'results': results})
from django.shortcuts import render
import requests
from django.shortcuts import render
import requests
import requests
from django.shortcuts import render
import requests
from django.shortcuts import render
def SearchView(request):
    word = request.GET.get('word')

    if not word:
        return render(request, 'dictionary/search.html', {'results': None})

    api_url = f'https://words-definitions-dictionary-and-data-api.p.rapidapi.com/en/{word}'
    headers = {
        'X-RapidAPI-Key': '682d0337cemshd966d21fce23698p19ef72jsn6d730c813e9f',
        'X-RapidAPI-Host': 'words-definitions-dictionary-and-data-api.p.rapidapi.com'
    }
    response = requests.get(api_url, headers=headers)

    if response.ok:
        data = response.json()
        if data:
            formatted_data = process_data(data)
            return render(request, 'dictionary/search.html', {'results': formatted_data})
    return render(request, 'dictionary/search.html', {'results': None})

def process_data(data):
    formatted_data = {
        'word': data[0]['word'].title(),
        'phonetic': data[0]['phonetic'],
        'phonetics': data[0].get('phonetics', []),
        'meanings': data[0].get('meanings', []),
        'license': data[0]['license'],
        'source_urls': data[0].get('sourceUrls', []),
    }
    return [formatted_data]
