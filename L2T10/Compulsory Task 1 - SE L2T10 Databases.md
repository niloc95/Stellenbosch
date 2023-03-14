# SE L2T10 Databases

Normalization is a process used in database design to organize data in a way that reduces redundancy and improves data integrity. It involves breaking down a large table into smaller, more manageable tables, and defining relationships between them. The goal of normalization is to minimize data duplication, reduce the likelihood of data anomalies (e.g. inconsistencies or contradictions), and make it easier to maintain and update the database.

First Normal Form (1NF) is a property of a relational database table that ensures that each column contains only atomic values (indivisible values) and that there are no repeating groups or arrays of values in any column. In other words, each column of a table must contain only a single value, and each row in the table must be unique.

To achieve 1NF, a table must be designed so that:

1. Each column should have a unique name.
2. Each column should contain only atomic values, that is, values that cannot be further divided.
3. The values in each column must be of the same data type.
4. Each row in the table must be unique, and there should be a primary key to identify each row.

Second Normal Form (2NF) is a database normalization technique that helps to reduce data redundancy and improve data integrity. It is based on the concept of functional dependencies, which describes the relationship between two attributes in a table.

A table is said to be in 2NF if it is already in First Normal Form (1NF) and no non-prime attribute (an attribute that is not part of any candidate key) is dependent on only a part of a candidate key. In other words, every non-prime attribute must be fully dependent on the entire candidate key.

To achieve 2NF, we need to identify the functional dependencies that exist in a table and then decompose the table into smaller tables based on those dependencies. The resulting tables should have only one candidate key and every non-prime attribute should be fully dependent on that key.

By decomposing the table in this way, we eliminate the redundancy caused by repeating the same product name for each order, and we ensure that each table has only one candidate key and every non-prime attribute is fully dependent on that key.

Third Normal Form (3NF) is a database normalization technique that helps to eliminate data redundancy and inconsistency. It is an advanced form of normalization, which builds upon the first two normal forms (1NF and 2NF).

In 3NF, a table is said to be in third normal form if it satisfies the following conditions:

1. It is in second normal form (2NF).
2. All non-key attributes in the table are dependent on the primary key.

Overall, 3NF is important because it helps to improve the efficiency of database operations, reduces data redundancy, and ensures data consistency.

To draw the dependency diagram of the INVOICE table, we first identify the functional dependencies in the table. Here are the dependencies:

- INV_NUM → SALE_DATE
- INV_NUM, PROD_NUM → PROD_DESC, PROD_PRICE, VEND_CODE, VEND_NAME
- PROD_NUM → PROD_DESC

The first dependency is a simple dependency where the invoice number determines the sale date.

The second dependency is a composite dependency, where the combination of invoice number and product number determines the product description, product price, vendor code, and vendor name.

The third dependency is a simple dependency where the product number determines the product description.

Using these dependencies, we can draw the dependency diagram as follows:

INV_NUM → SALE_DATE
    ↘
PROD_NUM → PROD_DESC
    ↘
INV_NUM, PROD_NUM → PROD_PRICE, VEND_CODE, VEND_NAME

In this diagram, the arrows represent the dependencies, and the circles represent the attributes. The circles that are not connected by arrows represent attributes that are not involved in any dependencies.

There are no partial dependencies in this table, but there is a transitive dependency from INV_NUM to PROD_PRICE, VEND_CODE, and VEND_NAME through PROD_NUM. To remove this transitive dependency, we could create a separate table for products and their details, and reference it in the INVOICE table using foreign keys.

To remove the partial dependencies, we need to break down the table into smaller tables. Here are the tables we can create:

1. INVOICE table (INV_NUM → SALE_DATE)

INV_NUM (PK) | SALE_DATE

This table is in 1st Normal Form (1NF) because it has no repeating groups or multi-valued attributes.

1. PRODUCT table (PROD_NUM → PROD_DESC)

PROD_NUM (PK) | PROD_DESC

This table is also in 1NF because it has no repeating groups or multi-valued attributes.

3. INVOICE_ITEM table (INV_NUM, PROD_NUM → PROD_PRICE, VEND_CODE, VEND_NAME)

INV_NUM (PK) | PROD_NUM (PK) | PROD_PRICE | VEND_CODE | VEND_NAME

This table is in 2nd Normal Form (2NF) because all non-key attributes depend on the composite key (INV_NUM, PROD_NUM). There are no partial dependencies.

Here is the new dependency diagram:

INVOICE         PRODUCT         INVOICE_ITEM
-------         -------         ------------
INV_NUM (PK)    PROD_NUM (PK)    INV_NUM (PK, FK)
SALE_DATE       PROD_DESC        PROD_NUM (PK, FK)
                ^                PROD_PRICE
                |                VEND_CODE
                +----------------VEND_NAME

In this diagram, the arrows represent the foreign key relationships between the tables. The circles with a PK label represent the primary keys of each table.

We have normalized the original table to 2NF.

To remove the transitive dependency, we need to create a separate table for the product details. Here are the tables we can create:

1. INVOICE table (INV_NUM → SALE_DATE)

INV_NUM (PK) | SALE_DATE

This table is in 1st Normal Form (1NF) because it has no repeating groups or multi-valued attributes.

2. PRODUCT table (PROD_NUM → PROD_DESC, PROD_PRICE, VEND_CODE, VEND_NAME)

PROD_NUM (PK) | PROD_DESC | PROD_PRICE | VEND_CODE | VEND_NAME

This table is in 2nd Normal Form (2NF) because all non-key attributes depend on the entire primary key (PROD_NUM). There are no partial dependencies.
3. INVOICE_ITEM table (INV_NUM, PROD_NUM → QUANTITY_SOLD)

INV_NUM (PK, FK) | PROD_NUM (PK, FK) | QUANTITY_SOLD

This table is in 3rd Normal Form (3NF) because all non-key attributes depend only on the primary key (INV_NUM, PROD_NUM). There are no transitive dependencies.

Here is the new dependency diagram:

INVOICE         PRODUCT         INVOICE_ITEM

---

INV_NUM (PK)    PROD_NUM (PK)    INV_NUM (PK, FK)
SALE_DATE       PROD_DESC        PROD_NUM (PK, FK)
                PROD_PRICE       QUANTITY_SOLD
                VEND_CODE
                VEND_NAME

In this diagram, the arrows represent the foreign key relationships between the tables. The circles with a PK label represent the primary keys of each table.

We have normalized the original table to 3NF.