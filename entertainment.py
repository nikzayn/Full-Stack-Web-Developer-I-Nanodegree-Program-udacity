import fresh_tomatoes
import media

due_date = media.Movie("Due Date",
                        "Peter Highman must reach Los Angeles to make it in time for his child's birth. However, he is forced to ride with Ethan, who frequently lands him in trouble.",
                        "https://upload.wikimedia.org/wikipedia/en/5/53/Due_Date_Poster.jpg",
                        "https://www.youtube.com/watch?v=0iCFi14Glbk&t=4s")

avatar = media.Movie("Good Will Hunting",
                        "Will Hunting, a genius in mathematics, solves all the difficult mathematical problems. When he faces an emotional crisis, he takes help from psychiatrist Dr Sean Maguireto, who helps him recover.",
                        "https://upload.wikimedia.org/wikipedia/en/5/52/Good_Will_Hunting.png",
                        "https://www.youtube.com/watch?v=7TSLzPu2no4")

lucy = media.Movie("Lucy",
                   "A woman's strength and thinking power grow exponentially after the effects of a performance-enhancing drug set in.",
                   "https://upload.wikimedia.org/wikipedia/en/1/14/Lucy_%282014_film%29_poster.jpg",
                   "https://www.youtube.com/watch?v=2tI7w1ffWrs")

interstellar = media.Movie("Interstellar",
                        "In the future, Earth is slowly becoming uninhabitable. Ex-NASA pilot Cooper, along with a team of researchers, is sent on a planet exploration mission to report which planet can sustain life",
                        "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                        "https://www.youtube.com/watch?v=zSWdZVtXT7E")

theory_of_everything = media.Movie("The Theory of Everything",
                        "Stephen Hawking, an excellent astrophysics student working on his research, learns that he suffers from motor neurone disease and has around two years to live.",
                        "https://upload.wikimedia.org/wikipedia/en/6/67/The_Theory_of_Everything_%282014%29.jpg",
                        "https://www.youtube.com/watch?v=-rwIE4SUxQA")

coco = media.Movie("Coco",
                   "Despite his family's generations-old ban on music, young Miguel dreams of becoming an accomplished musician like his idol Ernesto de la Cruz. Desperate to prove his talent, Miguel finds himself in the stunning and colorful Land of the Dead.",
                   "https://upload.wikimedia.org/wikipedia/en/9/98/Coco_%282017_film%29_poster.jpg",
                   "https://www.youtube.com/watch?v=X0ZHeNn1Kt4")

movies = [due_date, avatar, lucy, theory_of_everything, interstellar, coco]
fresh_tomatoes.open_movies_page(movies)
