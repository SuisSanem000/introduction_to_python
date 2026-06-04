def cat(food, state='still hungry', action='meow', breed='Siamese'):
    print(f"-- This cat wouldn't {action}", end=' ')
    print(f"if you gave it {food}")
    print(f"-- Lovely fur, the {breed}")
    print(f"-- It's {state}!")


# -- This cat wouldn't growl if you gave it soup
# -- Lovely fur, the Sphinx
# -- It's still hungry!
cat(action='growl', food='soup', breed='Sphinx')
