use desafio_engenheiro;

create table IF NOT EXISTS cliente (
    cliente_id bigint not null AUTO_INCREMENT,
    nome varchar(30) not null,
    PRIMARY KEY (cliente_id)
);

INSERT INTO 
	cliente(nome)
VALUES
	('Cliente A'),
	('Cliente B'),
	('Cliente C'),
	('Cliente D');


create table IF NOT EXISTS contrato (
    contrato_id bigint not null AUTO_INCREMENT,
    ativo bool not null,
    percentual numeric(10,2) not null,
    cliente_id bigint not null,
    PRIMARY KEY (contrato_id),
    FOREIGN KEY (cliente_id) REFERENCES cliente(cliente_id)
);

INSERT INTO 
	contrato(ativo, percentual, cliente_id)
VALUES
	(1, 2, 1),
	(0, 1.95, 1),
	(1, 1, 2),
	(1, 3, 4);

create table IF NOT EXISTS transacao (
    transacao_id bigint not null AUTO_INCREMENT,
    contrato_id bigint not null,
    valor_total decimal(15,2) not null,
    percentual_desconto numeric(10,2) null,
    PRIMARY KEY (transacao_id),
    FOREIGN KEY (contrato_id) REFERENCES contrato(contrato_id)
);

INSERT INTO 
	transacao(contrato_id, valor_total, percentual_desconto)
VALUES
	(1, 3000, 6.99),
	(2, 4500, 15),
	(1, 57989, 1.45),
    (4, 1, 0),
	(4, 35, null);