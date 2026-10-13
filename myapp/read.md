№	URL дар браузер	Барои чӣ
1	http://127.0.0.1:8000/api/users/	Ҳамаи User-ҳо
2	http://127.0.0.1:8000/api/users/1/	User бо ID = 1
3	http://127.0.0.1:8000/api/users/most-active/	User-ҳои фаъол
4	http://127.0.0.1:8000/api/users/statistics/	Статистикаи User
5	http://127.0.0.1:8000/api/profiles/	Ҳамаи Profile-ҳо
6	http://127.0.0.1:8000/api/profiles/city-statistics/	Статистика аз рӯйи шаҳр
7	http://127.0.0.1:8000/api/posts/	Ҳамаи Post-ҳо
8	http://127.0.0.1:8000/api/posts/1/	Post бо ID = 1
9	http://127.0.0.1:8000/api/users/1/posts/	Post-ҳои User-и 1
10	http://127.0.0.1:8000/api/posts/popular/	Post-ҳои машҳур
11	http://127.0.0.1:8000/api/posts/search/?q=django	Ҷустуҷӯи Post
12	http://127.0.0.1:8000/api/posts/filter/?min_views=100&max_views=2000&user_id=1	Филтр кардани Post
13	http://127.0.0.1:8000/api/posts/statistics/	Статистикаи Post
14	http://127.0.0.1:8000/api/posts/author-statistics/	Статистикаи муаллифон
15	http://127.0.0.1:8000/api/likes/	Ҳамаи Like-ҳо
16	http://127.0.0.1:8000/api/posts/1/likes/	Like-ҳои Post-и 1
17	http://127.0.0.1:8000/api/likes/top-posts/	Top 10 Post аз рӯйи Like
18	http://127.0.0.1:8000/api/favorites/	Ҳамаи Favorite-ҳо
19	http://127.0.0.1:8000/api/users/2/favorites/	Favorite-ҳои User-и 2
20	http://127.0.0.1:8000/api/users/1/analytics/	Аналитикаи User-и 1
21	http://127.0.0.1:8000/api/dashboard/	Статистикаи умумӣ
Муҳим: ин URL-ҳо танҳо вақте кор мекунанд, ки онҳоро дар urls.py илова карда бошӣ.