<p align="center">
  <img src="/assets/HBNB.png" alt="AirBnb Clone">
</p>

# AirBnB Clone - MySQL

This project is an extension of the AirBnB clone, integrating MySQL database storage and adding new features.

---

### How to Start It

1. Clone this repository:

   ```bash
   git clone https://github.com/medayoubadri/AirBnB_clone_v2.git
   cd AirBnB_clone_v2
   ```

2. Start the console:

   ```bash
   ./console.py
   ```

---

## How to Use

1. Set up your MySQL database using the provided scripts.
2. Set the necessary environment variables.
3. Run the console or specific test commands as shown in the task descriptions.

For more detailed information on each task, please refer to the project documentation.

## Environment Variables

- `HBNB_ENV`: running environment. It can be "dev" or "test"
- `HBNB_MYSQL_USER`: the username of your MySQL
- `HBNB_MYSQL_PWD`: the password of your MySQL
- `HBNB_MYSQL_HOST`: the hostname of your MySQL
- `HBNB_MYSQL_DB`: the database name of your MySQL
- `HBNB_TYPE_STORAGE`: the type of storage used. It can be "file" (using FileStorage) or "db" (using DBStorage)

---

### New Features and Tasks

1. **Fork me if you can!**
   - Update the repository name to AirBnB_clone_v2
   - Update the README.md with your information

2. **Bug free!**
   - Ensure all unittests pass without errors
   - Test command: `python3 -m unittest discover tests`

3. **Console improvements**
   - Update `do_create` function to allow object creation with parameters
   - Test command: `echo 'create State name="California"' | ./console.py`

4. **MySQL setup development**
   - Create a script to set up MySQL for development
   - Test command: `cat setup_mysql_dev.sql | mysql -hlocalhost -uroot -p`

5. **MySQL setup test**
   - Create a script to set up MySQL for testing
   - Test command: `cat setup_mysql_test.sql | mysql -hlocalhost -uroot -p`

6. **DBStorage - States and Cities**
   - Implement DBStorage engine using SQLAlchemy
   - Update BaseModel, State, and City classes
   - Test command: `HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py`

7. **DBStorage - User**
   - Update User class to work with DBStorage
   - Test command: `echo 'create User email="gui@hbtn.io" password="guipwd" first_name="Guillaume" last_name="Snow"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py`

8. **DBStorage - Place**
   - Update Place, User, and City classes for DBStorage
   - Test command: `echo 'create Place city_id="..." user_id="..." name="My_house"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py`

9. **DBStorage - Review**
   - Update Review, User, and Place classes for DBStorage
   - Test command: `echo 'create Review place_id="..." user_id="..." text="Great_place"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py`

10. **DBStorage - Amenity... and BOOM!**
    - Update Amenity and Place classes, implementing Many-to-Many relationship
    - Test command: `HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./main_place_amenities.py`
