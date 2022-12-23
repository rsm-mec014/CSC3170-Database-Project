-- Active: 1668517554814@@127.0.0.1@3306@project

select u.province, c.chip_name as ChipName,sum(p.budget) as revenue
from user AS u natural join package AS p, chip AS c
where p.package_id=c.package_id and province in ('Guangdong','Hubei')
group by c.chip_name
order by sum(p.budget) desc
limit 1,6;
---该省销量top 6的芯片产品

select sum(p.budget) as revenue, p.create_time
from user as u, package as p
where u.province in ('Guangdong','Hubei')
GROUP BY DATE(p.create_time)
ORDER BY p.create_time asc;
---该省收入的时间序列折线图
