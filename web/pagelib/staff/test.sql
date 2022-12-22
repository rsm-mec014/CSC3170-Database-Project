-- Active: 1668517554814@@127.0.0.1@3306@project
select u.province, c.chip_name as ChipName,sum(p.budget) as revenue
from user AS u natural join package AS p, chip AS c
where p.package_id=c.package_id and province in ('Guangdong','Hubei')
group by c.chip_name
order by sum(p.budget) desc;