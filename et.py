#!/usr/bin/env python

import media
import fresh_tomatoes
print("Content-type:text/html \n")
Avg = media.Movie("Avengers", "Fantasy",
                  "https://bit.ly/2IB8NDM",
                  "https://www.youtube.com/embed/QwievZ1Tx-8")

HDHM = media.Movie("Hey Dil Hai Mushkil", "Romantic Drama",
                   "https://bit.ly/2Iv371Y",
                   "https://www.youtube.com/embed/Z_PODraXg4E")
Gravity = media.Movie("Gravity", "Space thriller",
                      "https://bit.ly/2Izbk0Z",
                      "https://www.youtube.com/embed/OiTiKOy59o4")
BAN = media.Movie("Bharat Ane Nenu", "Political",
                  "https://bit.ly/2rVcTQK",
                  "https://www.youtube.com/embed/KMWS5y2gZ6E")


IT = media.Movie("IT", "Horror",
                 "https://bit.ly/2wfWg6KN",
                 "https://www.youtube.com/embed/FnCdOQsX5kc")
Bang = media.Movie("Banglore ", "Friendship",
                   "https://bit.ly/2IC7R23",
                   "https://www.youtube.com/embed/Gdzif0Px_qY")
movies = [Avg, HDHM, Gravity, BAN, IT, Bang]
fresh_tomatoes.open_movies_page(movies)
