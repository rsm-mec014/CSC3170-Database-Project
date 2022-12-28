-- Active: 1668517554814@@127.0.0.1@3306@project

---页面1. 地区分析：界面支持select box选择省份地区
select u.province, c.chip_name as ChipName,sum(p.budget) as revenue
from user AS u natural join package AS p, chip AS c
where p.package_id=c.package_id and province in ('Guangdong','Hubei')
group by c.chip_name
order by sum(p.budget) desc
;
--- province需要用户自选，本语句仅做例子
--- 用户选完省份后，大屏上该省销量top 6的芯片产品。展示为竖版的条形图，label: Chip name, value: Revenue

select sum(p.budget) as revenue, DATE_FORMAT(p.create_time,'%Y-%m-%d') as create_time
from user as u, package as p
where u.province in ('Guangdong','Hubei')
GROUP BY DATE(p.create_time)
ORDER BY p.create_time asc;
--- province需要用户自选，本语句仅做例子
--- 该省revenue的时间序列折线图，x_axis: create_time, y_axis: revenue
--- 最好能支持光标定位，鼠标点到某个点就能显示对应数值

--- 页面2. 总体业绩分析
select Date, count(*) as finished_num
from (select DATE(p.CREATE_TIME) as date, s.name as status
from package as p natural join state as s) as joint
where Status='Finished'
GROUP BY MONTH(Date)
ORDER BY Date asc;
select Date, count(*) as all_num
from (select DATE(p.CREATE_TIME) as date, s.name as status
from package as p natural join state as s) as joint
GROUP BY MONTH(Date)
ORDER BY Date asc;
--- 无需选择省份
--- 这两条语句分别提取了 每月完成订单数量 和 每月订单总数，目的是计算每个月的订单完成率，绘制area chart

select u.province, sum(p.budget) as revenue
from user as u natural join package as p
GROUP BY u.`PROVINCE`;
--- 绘制气泡图显示各省销售收入，收入越高气泡越大。最好能显示在地图上。

--- 3. 订单界面
select `PACKAGE_ID`, user.`USER_ID`, waiting_pkg.deadline, FIRST_NAME, LAST_NAME, phone_number, STREET_ADDRESS 
from (select * from
(SELECT * from state where state_name='Waiting') as W natural join package) as waiting_pkg,
USER
where waiting_pkg.user_id=user.`USER_ID`;
--------查询未完成订单的详细信息，可以链接staff页面的订单管理

SELECT `PLANT_ID`, COUNT(*)
from plant_with_package
GROUP BY PLANT_ID;
SELECT plant_id, count(*) as machine_num
from machine GROUP BY `PLANT_ID`;