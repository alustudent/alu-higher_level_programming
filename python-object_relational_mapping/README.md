# Python - Object-relational mapping

Querying MySQL from Python, first with raw SQL through `MySQLdb` (including SQL injection and how to prevent it), then with the SQLAlchemy ORM.

| File | Description |
|------|-------------|
| `0-select_states.py` | Lists all states |
| `1-filter_states.py` | Lists states starting with `N` |
| `2-my_filter_states.py` | Lists states matching an argument (query built with `format`) |
| `3-my_safe_filter_states.py` | Same, safe from SQL injection |
| `4-cities_by_state.py` | Lists all cities with their state |
| `5-filter_cities.py` | Lists the cities of a given state |
| `model_state.py` | `State` model and declarative `Base` |
| `7-model_state_fetch_all.py` | Lists all `State` objects |
| `8-model_state_fetch_first.py` | Prints the first `State` |
| `9-model_state_filter_a.py` | Lists states containing `a` |
| `10-model_state_my_get.py` | Prints the id of a state by name |
| `11-model_state_insert.py` | Adds Louisiana |
| `12-model_state_update_id_2.py` | Renames state 2 to New Mexico |
| `13-model_state_delete_a.py` | Deletes states containing `a` |
| `model_city.py` | `City` model linked to `states` |
| `14-model_city_fetch_by_state.py` | Lists all cities with their state |
