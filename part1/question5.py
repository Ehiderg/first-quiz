################################################################################
#     ____                          __     _                           ______
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____           / ____/
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \         /___ \  
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ____/ /  
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /_____/   
#                                                                            
#  Question 5
################################################################################
#
# Instructions:
# This questions continues to use the database we worked with in Question 4. In 
# this question, we will made some modifications ot the table.

# Part 5.A:
# Create a new table, 'favorite_foods.' It should have the columns:
# food_id integer
# name text
# vegetarian integer

sql_create_favorite_foods = """

Create table favorite_foods (
	food_id integer not NULL,
	name text not NULL,
	vegetarian integer NOT NULL
);

"""

# Part 5.B:
# Alter the animals and people tables by adding a new column to each called 'favorite_food_id'
# The test suite will verify the new changes by inserting some new rows. 

sql_alter_tables_with_favorite_food = """

Alter table animals 
add favorite_food_id;

Alter table people 
add favorite_food_id;

"""

# Part 5.C:
# Write a query to select all pets that are vegetarian.
# THe output should be a list of tuples in the format: (<pet name>, <food name>)

sql_select_all_vegetarian_pets = """

with vege (food_id, name, vegetarian) as (
 SELECT * FROM favorite_foods f
  WHERE f.vegetarian == '1'
)

select DISTINCT a.name, v.name FROM vege v
JOIN animals a on a.favorite_food_id = v.food_id 


"""