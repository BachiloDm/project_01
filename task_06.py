# Задача 6
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.


my_favorite_songs = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
# Решение
# import random 
from random import sample
data=list(my_favorite_songs.items())
songs=sample(data,3)
print(songs)
total_time=0
for song, time in songs:
    print(song,time)
    total_time+=time
print('Время звучания трех песен =',round(total_time,2))