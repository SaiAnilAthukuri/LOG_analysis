# Project 1: Logs Analysis Project(`ATHUKURI SAI ANIL`)

Logs Analysis Project, part of the Udacity [Full Stack Web Developer Nanodegree](https://www.udacity.com/).

## What it is and does

A Reporting page that prints out reports in a plain text format based on the data in the database.This reporting tool is a python program using the `psycopg2` module to connect to the database.

## Project content

## Following files are in folder:

- analysis.py - main file to run this Logs Analysis Reporting tool
- README.md - instructions to install this reporting tool
- newsdata.sql - database file
- dataviews.sql - views files
- output.PNG - screen shot images
- output.txt - output text file

## Mandatory Tools

- Python
- Vagrant
- VirtualBox

## Installation steps to run application:

There are some dependancies and a few instructions on how to run the application.

## Dependencies

- [Vagrant](https://www.vagrantup.com/)
- [Udacity Vagrantfile](https://github.com/udacity/fullstack-nanodegree-vm)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

## How to Install
- Install Vagrant & VirtualBox

## How to Run Project

- Download the project zip file to you computer and unzip the file then place inside `vagrant/log_analysis`.
- Go to Vagrant directory and place extract here
- Create the Vagrant file(`vagrant init ubuntu/xenial64`)
- Launch the Vagrant VM (`vagrant up`)
- Log into the Vagrant VM (`vagrant ssh`)
- Exit the directory 2 times (`cd ..' )
- Navigate to `cd /vagrant` as instructed in terminal
- Update the virtual machine (`sudo apt-get update` )
- Install Postgresql in Postgres User (`sudo apt-get install postgresql`)
- Login to postgresql server by using command (`psql`)
- Create super user vagrant with attributes(`create user vagrant with superuser createdb createrole nologin replication bypassrls;`)
- Create databse news with owner to vagrant(`create database news owner to 'vagrant' `)
- Exit the database using command (`\q`)
- Logout the current user by using command(`logout`)
- Install psycopg2 module by using Pip(`pip install psycopg2`)
- To load the database use the following command(`psql -d news -f newsdata.sql`)
- The result be like
	```
	SET
	SET
	SET
	SET
	SET
	SET
	SET
	SET
	SET
	CREATE TABLE
	ALTER TABLE
	CREATE SEQUENCE
	ALTER TABLE
	ALTER SEQUENCE
	CREATE TABLE
	ALTER TABLE
	CREATE SEQUENCE
	ALTER TABLE
	ALTER SEQUENCE
	CREATE TABLE
	ALTER TABLE
	CREATE SEQUENCE
	ALTER TABLE
	ALTER SEQUENCE
	ALTER TABLE
	ALTER TABLE
	ALTER TABLE
	COPY 8
	setval
	--------
	30
	(1 row)

	
	COPY 4
	setval
	--------
	4
	(1 row)

	
	COPY 1677735
	setval
	---------
	3356657
	(1 row)


	ALTER TABLE
	ALTER TABLE
	ALTER TABLE
	ALTER TABLE
	ALTER TABLE	
	```
- Make views by running respective queries on command line(`psql -d news dataviews.sql`)
- My dataviews.sql file queries 
	(`create or replace view udacityloganalysis_articles as select replace(path,'/article/','') as loganalysisslug, 
	count(*) as loganalysisviews from log where path<>'/' and status like '%200%' group by path;`)
	
	(`create or replace view udacityloganalysis_authors as select authors.name as loganalysisname, articles.slug as loganalysisslug from authors inner join articles on articles.author=authors.id order by authors.id;`)
	
	(`create or replace view udacityloganalysis_totalerrors as select date(time), count(date(time)) from log group by date(time);`)
	
	(`create or replace view udacityloganalysis_totalfilled as select date(time), count(date(time)) from log where status like '%404%' group by date(time) order by date(time);`)
	
- Execute above sql statements and result be like : 
	```
	CREATE VIEW
	CREATE VIEW
	CREATE VIEW
	CREATE VIEW
	```
- Finally Run python file (`python analysis.py`)
- Final Output of the log analysis project is :
	```
	The List of the Most Popular Article:
	-------------------------------------
	Candidate is jerk, alleges rival****338647
	Bears love berries, alleges bear****253801
	Bad things gone, say good people****170098


	The List of the Popular Authors :
	---------------------------------
	Ursula La Multa****507594
	Rudolf von Treppenwitz****423457
	Anonymous Contributor****170098
	Markoff Chaney****84557


	Error :
	------------
	2016-07-17****2.3 %
	```

Logs Analysis Output:-
[Log_Analysis](https://github.com/SaiAnilAthukuri/LOG_analysis/blob/master/output.PNG)
