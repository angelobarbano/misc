import media
import fresh_tomatoes


dr_strangelove = media.Movie("Dr. Strangelove",
                        "A dark satire of the Cold War",
                        "http://www.gstatic.com/tv/thumb/movieposters/1816/p1816_p_v7_aa.jpg",
                        "https://www.youtube.com/watch?v=pgd_aJBBRfs")

kung_pow = media.Movie("Kung Pow",
                    "A hillarious martial arts parody",
                    "http://images.moviepostershop.com/kung-pow-enter-the-fist-movie-poster-2002-1020234277.jpg",
                    "https://www.youtube.com/watch?v=GXrAYdSeWY8")

goodfellas = media.Movie("Goodfellas",
                    "Classic mafia tale based on a true story",
                    "http://newshour-tc.pbs.org/newshour/wp-content/uploads/2014/01/Goodfellas.jpg",
                    "https://www.youtube.com/watch?v=qo5jJpHtI1Y")

movies = [dr_strangelove, kung_pow, goodfellas]

fresh_tomatoes.open_movies_page(movies)
                    
