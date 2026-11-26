# SQL - More queries

MySQL users and privileges, table constraints (`NOT NULL`, `DEFAULT`, `UNIQUE`, primary and foreign keys), subqueries and `JOIN`s.

| File | Description |
|------|-------------|
| `0-privileges.sql` | Lists the privileges of `user_0d_1` and `user_0d_2` |
| `1-create_user.sql` | Creates `user_0d_1` with all privileges |
| `2-create_read_user.sql` | Creates `hbtn_0d_2` and the read-only `user_0d_2` |
| `3-force_name.sql` | Creates `force_name` with a required `name` |
| `4-never_empty.sql` | Creates `id_not_null` with `id` defaulting to 1 |
| `5-unique_id.sql` | Creates `unique_id` with a unique `id` |
| `6-states.sql` | Creates `hbtn_0d_usa.states` |
| `7-cities.sql` | Creates `hbtn_0d_usa.cities` with a foreign key to `states` |
| `8-cities_of_california_subquery.sql` | Cities of California, using a subquery |
| `9-cities_by_state_join.sql` | All cities with their state, using a `JOIN` |
| `10-genre_id_by_show.sql` | Shows with at least one genre id |
| `11-genre_id_all_shows.sql` | All shows with their genre id or `NULL` |
| `12-no_genre.sql` | Shows without a genre |
| `13-count_shows_by_genre.sql` | Number of shows per genre |
| `14-my_genres.sql` | Genres of Dexter |
| `15-comedy_only.sql` | Comedy shows |
| `16-shows_by_genre.sql` | All shows with their genre names |
