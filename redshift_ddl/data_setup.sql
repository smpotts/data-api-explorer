
create database dev;

create schema demo;

create table demo.data_api_test(
    data_api_test_id integer not null primary key,
    user_id integer not null,
    user_name varchar(64),
    region varchar(32) default 'us-east-1',
    request_timestamp timestamp default getdate()
);

insert into demo.data_api_test(data_api_test_id, user_id, user_name, region) values 
(1, 2948, 'demo_user', 'us-east-1'),
(2, 4832, 'testing123', 'us-west-1'),
(3, 2948, 'demo_user', 'us-east-2'),
(4, 5827, 'fake_user', 'eu-west-2'),
(5, 3453, 'test_user', 'eu-west-2'),
(6, 93452, 'foo', 'us-west-2'),
(7, 6234, 'bar', 'us-east-2'),
(8, 65048, 'test', 'ap-east-1'),
(9, 1234, 'fake', 'af-south-1'),
(10, 5436, 'user', 'us-east-1');
