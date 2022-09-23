CREATE TABLE `product_model`(
    `title` CHAR(255) NOT NULL,
    `description` CHAR(255) NOT NULL,
    `price` DECIMAL(8, 2) NOT NULL,
    `inventory_quantity` INT NOT NULL
);
ALTER TABLE
    `product_model` ADD PRIMARY KEY `product_model_title_primary`(`title`);