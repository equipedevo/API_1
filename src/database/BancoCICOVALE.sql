CREATE DATABASE BancoCICOVALE;

USE BancoCICOVALE;

create table Periodo(
    per_cod int auto_increment primary key,
    per_nome char(4),
    per_quant int
);

create table Cidade(
    cid_cod int auto_increment primary key,
    cid_nome varchar(30),
    cid_quant int
);

create table Valor(
    val_cod int auto_increment primary key,
    val_nome varchar(15),
    val_quant int
);

create table Tipo(
    tip_cod int auto_increment primary key,
    tip_nome varchar(15),
    tip_quant int
);


create table Subtipo(
    sub_cod int auto_increment primary key,
    sub_nome varchar(255),
    sub_quant int
);
