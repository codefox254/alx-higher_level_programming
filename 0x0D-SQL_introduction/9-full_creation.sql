-- Create a table named 'second_table' with columns 'id', 'name', and 'score'
-- if it doesn't already exist, and fill it with multiple rows
CREATE TABLE IF NOT EXISTS `second_table` (
    `id` INT,
    `name` VARCHAR(256),
    `score` INT
);

-- Insert rows into the 'second_table' with specified values for id, name, and score
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (1, 'John', 10);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (2, 'Alex', 3);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (3, 'Bob', 14);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (4, 'George', 8);
