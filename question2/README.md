* For this question, we needed to create a project containing three models

    * A model for products
    * A model for catalogs
    * A model for buyers

** As descripted in the question, the models should have some relationships between them. There is N products, a catalog has N products and products can be in M catalogs, so we have created an N:M table. A buyer has a catalog foreign key. These conditions are represented in the diagram below.

![Relationships](https://raw.githubusercontent.com/lopes05/projectwastenot_challenge/master/question2/db_modeling.jpeg)
    
A product is only shown to an user if its visibility is set as 'default' or the product is in a catalog set in the buyer model.
If we needed to query products that can be shown to an user with a catalog, we can use the following query:

```sql
SELECT DISTINCT (p.id, p.name, p.price, p.visibility) as products_result FROM product p
INNER JOIN catalog_product cp ON cp.product_id = p.id or p.visibility = 'default'
INNER JOIN buyer b on b.catalog_id = cp.catalog_id
WHERE b.id = $1;
```
