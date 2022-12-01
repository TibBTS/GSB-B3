use gsb_b3;

ALTER TABLE visiteur ADD email TEXT NULL;
UPDATE visiteur SET email = CONCAT(login,"@swiss-galaxy.com");
ALTER TABLE visiteur ADD codea2f CHAR(4);
select * from visiteur;


SET SQL_SAFE_UPDATES=0;
SET SQL_SAFE_UPDATES=1;