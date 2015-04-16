-- Drop tables
drop table if exists members cascade;
drop table if exists contacts;
drop table if exists users;
drop type if exists contacts_type;
drop type if exists user_type;

-- Create type
create type contacts_type as enum ('address','phone','email','others');
create type user_type as enum ('admin','user','query');

-- Create tables
create table if not exists members (
	id serial primary key,
	name character varying(32) not null,
	dob date,
	join_date date,
	cell character varying(32),
	Update_date timestamp not null
);
create index members_name_index on members (name varchar_pattern_ops);


create table if not exists contacts (
	id integer references Members(id) on delete cascade on update cascade not null,
	info character varying(128) not null,
	type contacts_type not null,
	Update_date timestamp not null
);
create index contacts_id_index on contacts (id);


create table if not exists users (
	id integer references Members(id) on delete cascade on update cascade not null,
	muser character varying(16) not null,
	mpass character varying(64) not null,
	type user_type not null,
	session_id character varying(32),
	session_date timestamp
);


-- REMINDER: Functions with identical names but different arguments are allowed.

create or replace function verify_login(p_user character varying(16), p_pass character varying(64)) 
returns bigint as $$
select count(*) from users where muser=p_user and mpass=p_pass;
$$ LANGUAGE SQL;


create or replace function verify_login2(p_user character varying(16), p_pass character varying(64)) 
returns integer as $$
select id from users where muser=p_user and mpass=p_pass;
$$ LANGUAGE SQL;  


create or replace function update_session(p_id integer, p_session character varying(32)) returns void as $$
update users set session_id=p_session, session_date=now() where id=p_id;
$$ LANGUAGE SQL;


-- create or replace function verify_session(p_session character varying(32)) 
-- returns integer as $$
-- select id from users where session_id=p_session;
-- $$ LANGUAGE SQL; 
