use gsb_b3;
ALTER TABLE visiteur
MODIFY mdp CHAR(255);

-- --------------------------------------------
/*
ALTER TABLE visiteur
MODIFY mdp CHAR(32) ;


SET SQL_SAFE_UPDATES=0;

UPDATE visiteur
SET mdp = md5(mdp);

SET SQL_SAFE_UPDATES=1;


*/
select * from visiteur