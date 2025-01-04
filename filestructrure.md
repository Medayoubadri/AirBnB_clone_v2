# AirBnB Clone V2 File Structure

```
AirBnB_clone_V2
├── console.py
├── AUTHORS
├── README.md
├── filestructure.md
├── requirements.txt
├── setup_mysql_dev.sql
├── setup_mysql_test.sql
├── models
│   ├── engine
│   │   ├── db_storage.py
│   │   └── file_storage.py
│   ├── __init__.py
│   ├── amenity.py
│   ├── base_model.py
│   ├── place.py
│   ├── review.py
│   ├── state.py
│   ├── user.py
│   └── city.py
│
└── tests
    ├── test_console.py
    ├── __init__.py
    └── test_models
        ├── test_engine
        │   ├── test_db_storage.py
        │   └── test_file_storage.py
        ├── __init__.py
        ├── test_base_model.py
        ├── test_city.py
        ├── test_file_storage.py
        ├── test_amenity.py
        ├── test_place.py
        ├── test_review.py
        ├── test_state.py
        └── test_user.py
```
