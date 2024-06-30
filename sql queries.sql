create table user_reg (name varchar(25) not null,password varchar(25) not null,user_id smallint primary key auto_increment ) ;
create table customers(user_id smallint not null, name text not null,mobile long not null ,email text not null,aadhar long not null);
create table book(user_id int not null, guest int not null, checkin date not null, checkout date not null, room enum("king","queen","budget") , status text not null );
create table feedback(user_id int not null,feedback text not null);