create table car
    (VIN varchar (17) not null,
     model varchar(15) not null,
     year numeric (4,0),
     color varchar (15),
     weight numeric (10,0),
     engine varchar (15),
     transmission varchar (15),
     previous_owner varchar (30),
     primary key (VIN)
    );

create table company
    (company_name varchar (20),
     brand varchar (20),
     primary key (company_name)
    );

create table brand
    (company_name varchar (20),
     model varchar (20),
     primary key (company_name, model)
     foreign key (company_name) references company
    );

create table dealer
    (dealer_id numeric (5,0),
     customers varchar (20),
     address varchar (20),
     phone varchar (13),
     primary key (dealer_name)
    );

create table customers
    (customer_id numeric (5,0),
     name varchar (20),
     purchase varchar (20),
     address varchar (20),
     phone varchar (13),
     primary key (customer_id)
    );