-- Problem 1.a
--SELECT count(*) from frequency where docid = '10398_txt_earn';

-- Problem 1.b
--select count(term) from frequency where docid = '10398_txt_earn' and count = 1;

-- Problem 1.c
/*
select count(*) from 
    (select term from frequency where docid = '10398_txt_earn' and count = 1
    union
    select term from frequency where docid = '925_txt_trade' and count = 1);
*/


-- Problem 1.d
--select count(docid) from frequency where term = 'parliament';


-- Problem 1.e
/*
select count(*) from 
    (select docid, sum(count) as N from frequency 
        group by docid 
        having N > 300);
*/


-- Problem 1.f
/*
select count(*) from 
(select docid from frequency where term = 'world') as tabw
inner join
(select docid from frequency where term = 'transactions') as tabt
on tabw.docid = tabt.docid;
*/


-- Problem 2
/*
select sum(A.value*B.value)
from A inner join B on A.col_num = B.row_num
where A.row_num = 2 and B.col_num = 3;
*/


-- Problem 3.h
/*
select sum(f1.count * f2.count)
from frequency f1 inner join frequency f2 on f1.term = f2.term 
where f1.docid = '10080_txt_crude' and f2.docid = '17035_txt_earn';
*/


-- Problem 3.i
/*
create view freq_plus_q as
select * from frequency
union 
select 'q' as docid, 'washington' as term, 1 as count 
union 
select 'q' as docid, 'taxes' as term, 1 as count
union 
select 'q' as docid, 'treasury' as term, 1 as count;
*/
/*
select max(similarity) 
from (select f2.docid, sum(f1.count * f2.count) as similarity
    from freq_plus_q f1 inner join freq_plus_q f2 on f1.term = f2.term 
    where f1.docid = 'q'
    group by f2.docid);
*/
