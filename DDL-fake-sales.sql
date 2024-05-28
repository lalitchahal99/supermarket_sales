create schema `fake`;

create table `fake`.`sales` (
	txn_id bigint auto_increment,
    product_line varchar(25),
    city varchar(15),
    customer_type varchar(10),
    gender char(1),
    payment_mode varchar(15),
    dt varchar(20),
    unit_price decimal(10, 2),
    quantity tinyint,
    tax decimal(10, 2),
    total decimal(10, 2),
    constraint `PK_sales_txn_id` primary key (`txn_id`)
);

alter table `fake`.`sales` auto_increment=100;

