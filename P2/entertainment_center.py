# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes

dotaWtf256 = media.Movie('Dota 2 WTF Moments 256', 
    'https://i.ytimg.com/vi/nOW-0zw3Wjk/hqdefault.jpg',
    'https://www.youtube.com/watch?v=nOW-0zw3Wjk')

dotaWtf257 = media.Movie('Dota 2 WTF Moments 257', 
    'https://i.ytimg.com/vi/whITMl1Vzu8/hqdefault.jpg',
    'https://www.youtube.com/watch?v=whITMl1Vzu8')

dotaWtf258 = media.Movie('Dota 2 WTF Moments 258',
    'https://i.ytimg.com/vi/nOW-0zw3Wjk/hqdefault.jpg', 
    'https://www.youtube.com/watch?v=z3bLm1LJFzk')

dotaWtf259 = media.Movie('Dota 2 WTF Moments 259',
    'https://i.ytimg.com/vi/wtAjAyjUx98/hqdefault.jpg',
    'https://www.youtube.com/watch?v=wtAjAyjUx98')

movies = [dotaWtf256, dotaWtf257, dotaWtf258, dotaWtf259]
fresh_tomatoes.open_movies_page(movies)
