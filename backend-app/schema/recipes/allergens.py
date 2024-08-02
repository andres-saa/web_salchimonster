from pydantic import BaseModel
from typing import Optional
from datetime import time, datetime






# CREATE Or replace  TABLE recipes.allergens (
#    id serial primary KEY,
# 	exist bool default true,
# 	created_at timestamp with time zone default now(),
#   name varchar
# );






# CREATE TABLE recipes.recipe_data_allergens (
#    "id" serial primary KEY,
#   "recipe_data_id" int,
#   "allergen_id" int,
# 	foreign key (recipe_data_id) references recipes.recipe_data_sheet(id) ,
# 	foreign key (allergen_id) references recipes.allergens(id) 
# );

