-- Import the database dump from hbtn_0d_tvshows
-- cat 10-genre_id_by_show.sql | sudo mysql -hlocalhost -uroot -p hbtn_0d_tvshows
SELECT C.title, S.genre_id FROM tv_shows C
JOIN tv_show_genres S ON C.id = S.show_id
ORDER BY C.title, S.genre_id ASC;
