DROP TABLE IF EXISTS users;
CREATE TABLE IF NOT EXISTS users(
          user_id INT,
          username VARCHAR(50),
          password VARCHAR(50),
          PRIMARY KEY(user_id)
        );

DROP TABLE IF EXISTS accounts;

DROP TABLE IF EXISTS transactions;
CREATE TABLE IF NOT EXISTS transactions(
   account_id_orig INT,
   account_id_dest INT,
   user_id INT,
   transaction_id INT,
   step INT,
   type VARCHAR(50),
   amount DECIMAL(15,2),
   isFraud INT,
   PRIMARY KEY(transaction_id),
   FOREIGN KEY(account_id_orig) REFERENCES origin(account_id),
   FOREIGN KEY(account_id_dest) REFERENCES dest(account_id),
   FOREIGN KEY(user_id) REFERENCES users(user_id)
);
