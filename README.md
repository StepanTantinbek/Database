# Database
database prototype for social media


file descriptions
dbase_func — package of programms to work with database
    *creation.py — includes functions to create database
        **create_db — creates database
        **load_dbase — loads database to the code to work with it
        **save_dbase — uploads database to the main file
        **fill_db — if database is empty, it will add superviser, database ready
        **checkbase — checks if database is exist or damaged
    *data_work.py — includes functions to modify database
        **identification — adds new user to database
        **user_delete — deletes user from database
        **user_reg — menu of what user is able to do
interaction_funcs — package of programms to interaxt with user
    *base.py — includes functions to format data input by user for obtainment
        **perfect_dt — removes space chars and lowers all capital letters
        **read_row — makes a list of data that user has to input
        **list_to_strtab — makes string with data types for user to put fot the database file
    *user.py — includes functions to interract with user
        **notification — prints negative or positive comment depending on statement status
        **user_answer — asks user a question and returns result depending on answer
localise_func — package of programms
    *interact_user.py —

    *translator.py — Includes localised function of translator function
        **lang_print_gen — Generator of localisation translator function
            ***lang_print — Prints phrase in chosen language
verification_funcs — package of programms
    *auxiliary.py — includes functions to work with users personal data
        **hash — encrypts data
        **lencheck — checks string length
    *login.py — (BEING DEVELOPED)includes functions to work with users login
    *password.py — includes functions to create a strong password
        **checkpssw — checks the password
            ***repeat_check — checks if any symbol is repeated to many times
            ***charcheck — checks for types of chars needed in password
            ***checkreg — checks is password uses upper and lower register
            ***forblistcheck — checks if password has popular char combos