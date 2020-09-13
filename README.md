# FlipkartClone
DB Tables

User
user_addresses
Categories (multilevel)
products
products_meta
Orders
Cart
Payment
Comments on a product with votes
Wishlist Make the relationship tables as well
Functionality

Clone of Flipkart
Three types of users (user, owner, admin)
only owner can edit, delete, add products owned by the same person
admin can edit/delete any item or remove any user/owner
categories can be nested as tree structure (use closure tables)
user can view all the products
user can use search and filters with categories and Sub-categories
user can add the item to Wishlist
user can add products to cart and order
users can comment on the item and other users can upvote or downvote the comment
products_meta should contain image urls of the product and other relevant key-value pairs
Note

use JWT for session
code should be PEP-8 coding style
use MVC structure and ORM to connect to SQL
proper comments and variable names in each python script
