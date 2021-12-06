drop table if exists users;

create table users 
(
  id integer primary key AUTOINCREMENT,
  name text not null,
  email text not null,
  password text not null,
  created_at datetime default current_timestamp
);

