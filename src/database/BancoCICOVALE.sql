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

insert into Periodo
values
(1, '2019', 0),
(2, '2020', 0),
(3, '2021', 0),
(4, '2022', 0);

insert into Cidade
values
(1, 'São José dos Campos', 0),
(2, 'Taubaté', 0),
(3, 'Jacareí', 0);

insert into Valor
values
(1, 'Quantidade', 0),
(2, 'Gastos', 0);

insert into Tipo
values
(1, 'Consultas', 0),
(2, 'Internações', 0),
(3, 'Procedimentos', 0),
(4, 'Tratamentos', 0),
(5, 'Medicamentos', 0);

insert into Subtipo
values
(1, 'Serviços hospitalares', 0),
(2, 'Serviços profissionais', 0),
(3, 'CID III - Anemias por deficiência de ferro e outras anemias', 0),
(4, 'CID III - Afecções hemorrágicas e outras doenças do sangue e dos orgãos hematopoiéticos', 0),
(5, 'CID IV - Diabetes mellitus', 0),
(6, 'CID IV - Transtornos nutricionais metabólicos e sequelas nutricionais', 0),
(7, 'CID VI - Meningites bacterianas, infecciosas, parasitórias e outras causas', 0),
(8, 'CID VI - Doenças de parkinson, alzheimer e epilepsia', 0),
(9, 'CID VI - Doenças Relacionadas ao sistema Nervoso', 0),
(10, 'CID IX - Infarto agúdo do miocárdio', 0),
(11, 'CID IX - Infarto cerebral', 0),
(12, 'CID IX - Insuficiência cardíaca', 0),
(13, 'CID X - Pneumonia', 0),
(14, 'CID X - Bronquite e bronqueolíte agúda, doenças pulmonares crônicas e bronquequiectasia', 0),
(15, 'CID X - Asma', 0),
(16, 'Procedimentos com finalidade diagnóstica', 0),
(17, 'Procedimentos clínicos', 0),
(18, 'Procedimentos cirúrgicos', 0),
(19, 'Aparelho respiratório', 0),
(20, 'Tratamento de doenças infecciosas e parasitárias', 0),
(21, 'Traqueia e brônquios', 0),
(22, 'Pulmão', 0),
(23, 'IMUNOGLOBULINA ANTI-RHO (D) (FRASCO AMPOLA DE 2 ML E 1.250 UI)', 0),
(24, 'IMUNOGLOBULINA HUMANA 1,0 G INJETAVEL (POR FRASCO)', 0),
(25, 'SURFACTANTE FRASCO-AMPOLA', 0),
(26, "ALBUMINA HUMANA 20 POR CENTO (FRASCO-AMPOLA DE 50 ML)", 0);
