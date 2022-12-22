-- Active: 1668517554814@@127.0.0.1@3306@project
select u.province,c.chip_version,sum(c.price) 
from user AS u, package AS p, chip AS c
where u.user_id=p.user_id
group by c.chip_name;
select c.chip_name as ChipName,sum(p.budget) as revenue
from user AS u, package AS p, chip AS c
where u.user_id=p.user_id and province='Guangdong'
group by c.chip_name
order by sum(p.budget) desc
limit 0,5;