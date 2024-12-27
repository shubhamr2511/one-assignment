



### MODELS
Order:
    product
    quantity
    ordered_at

Product:
    name
    price
    description

# Creating necessary flows first, then more features if time permits
place_order:
    trigger > validate > save > payment > status_update
