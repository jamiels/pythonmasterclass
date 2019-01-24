USE myfirstdb;
CREATE TABLE orders (
    order_id int,
    description varchar(255)
);
SELECT * FROM orders;
INSERT INTO orders (order_id, description) values (1,'hello!');
INSERT INTO orders (order_id, description) values (2,'sky!');
INSERT INTO orders (order_id, description) values (2,'sky!');
INSERT INTO orders (order_id, description) values (3,'fly!');
INSERT INTO orders (order_id, description) values (4,'bye!');
SELECT ORDER_ID FROM ORDERS;
SELECT description FROM ORDERS;
select * from orders where order_id = 1;
select * from orders where order_id > 2;
select * from orders where order_id > 2 AND description='bye!'
CREATE DATABASE TRADING;
USE TRADING;
DROP TABLE BLOTTER;
CREATE TABLE BLOTTER (BLOTTER_ID int, SIDE varchar(6), TICKER varchar(6), QUANTITY varchar(6), CUSTOMER_ID int, TRADE_DATE datetime);
use myfirstdb;
desc orders;
drop table orders;
create table orders (
	order_id int,
    product_id int,
    description_tx varchar(255)
);

create table products (
	product_id int,
    description_tx varchar(255)
);

insert into products (product_id, description_tx) values (1,'M&Ms');
insert into products (product_id, description_tx) values (2,'Kit Kats');

select * from products;

insert into orders (order_id, product_id, description_tx) values (1,2,'Holiday purchase');
insert into orders (order_id, product_id, description_tx) values (2,2,'Still more');
insert into orders (order_id, product_id, description_tx) values (3,1,'Lunch');

select order_id, products.description_tx 
from orders, products where orders.product_id = products.product_id;

insert into orders (order_id, product_id, description_tx) values (3,3,'Wrong');

select order_id, products.description_tx from orders, products where orders.product_id = products.product_id;

truncate orders;
select * from orders;

delete from orders;

update orders set order_id=5;
select * from orders;

drop  table products;
create table products (
	product_id int,
    description_tx varchar(255)
);

insert into products (product_id, description_tx) values (1,'M&Ms');
insert into products (product_id, description_tx) values (2,'Kit Kats');
select * from products;
drop table orders;
create table orders (
	order_id int,
    product_id int,
    description_tx varchar(255)
);

insert into orders (order_id, product_id, description_tx) values (1,2,'Holiday purchase');
insert into orders (order_id, product_id, description_tx) values (2,2,'Still more');
insert into orders (order_id, product_id, description_tx) values (3,1,'Lunch');
select * from orders;
SET SQL_SAFE_UPDATES=0;
update orders set description_tx='changed' where order_id=1;
select * from orders;
update products set product_id = 100;
select * from products;
select * from orders;

select order_id, products.description_tx from orders, products where orders.product_id = products.product_id;



