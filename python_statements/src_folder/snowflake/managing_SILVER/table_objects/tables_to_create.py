from snowflake.core.table import PrimaryKey, Table, TableColumn, UniqueKey


productos = Table( #ya creada
    name="productos",
    columns=[TableColumn(name="id_producto", datatype="varchar", nullable=False, constraints=[PrimaryKey()]),
             TableColumn(name="name_producto", datatype="varchar", nullable=False),
             TableColumn(name="descripcion_producto", datatype="varchar", nullable=False),
             TableColumn(name="id_categoria", datatype="number(38,0)", nullable=False),
             TableColumn(name="precio_base_producto", datatype="number(38,0)"),
             TableColumn(name="fecha_creacion_producto", datatype="timestamp_ntz")]
)




variantes_producto = Table(
    name="variantes_producto",
    columns=[
        TableColumn(name="id_variante", datatype="varchar(36)", nullable=False, constraints=[PrimaryKey()]),
        TableColumn(name="id_producto", datatype="varchar(36)", nullable=False),
        TableColumn(name="sku", datatype="varchar(255)", nullable=False, constraints=[UniqueKey(name="UK_SKU")]),
        TableColumn(name="talla", datatype="varchar(255)", nullable=False),
        TableColumn(name="color", datatype="varchar(255)", nullable=False),
        TableColumn(name="stock_disponible", datatype="number(38,0)", nullable=False),
        TableColumn(name="precio_especifico", datatype="number(8,2)"),
        TableColumn(name="precio_oferta", datatype="number(8,2)"),
        TableColumn(name="codigo_barras", datatype="varchar", nullable=False)
    ]
)


clientes = Table(
    name="clientes",
    columns=[
        TableColumn(name="id_cliente", datatype="varchar(36)", nullable=False, constraints=[PrimaryKey()]),
        TableColumn(name="email", datatype="varchar(255)", nullable=False, constraints=[UniqueKey(name="UK_EMAIL")]),
        TableColumn(name="nombre", datatype="varchar(255)", nullable=False),
        TableColumn(name="apellidos", datatype="varchar(255)", nullable=False),
        TableColumn(name="password_hash", datatype="varchar(255)", nullable=False),
        TableColumn(name="telefono", datatype="varchar(255)", nullable=False),
        TableColumn(name="fecha_registro", datatype="timestamp_ntz(0)", nullable=False)
    ]
)


pedidos = Table(
    name="pedidos",
    columns=[
        TableColumn(name="id_pedido", datatype="varchar(36)", nullable=False, constraints=[PrimaryKey()]),
        TableColumn(name="id_cliente", datatype="varchar(36)", nullable=False),
        TableColumn(name="id_direccion_cliente", datatype="varchar(36)", nullable=False),
        TableColumn(name="id_paqueteria", datatype="varchar(255)", nullable=False),
        TableColumn(name="fecha_entrega_pedido", datatype="timestamp_ntz(0)", nullable=False),
        TableColumn(name="status_pedido", datatype="varchar(100)", nullable=False),
        TableColumn(name="total_pagado", datatype="number(8,2)", nullable=False),
        TableColumn(name="direccion_entrega", datatype="varchar", nullable=False),
        TableColumn(name="fecha_pedido", datatype="timestamp_ntz(0)", nullable=False)
    ]
)


lineas_pedido = Table(
    name="lineas_pedido",
    columns=[
        TableColumn(name="id_linea", datatype="varchar(36)", nullable=False, constraints=[PrimaryKey()]),
        TableColumn(name="id_pedido", datatype="varchar(36)", nullable=False),
        TableColumn(name="id_variante", datatype="varchar(36)", nullable=False),
        TableColumn(name="cantidad", datatype="number(38,0)", nullable=False),
        TableColumn(name="precio_unitario", datatype="number(8,2)", nullable=False),
        TableColumn(name="subtotal", datatype="number(8,2)", nullable=False)
    ]
)



direccion_cliente = Table(
    name="direccion_cliente",
    columns=[
        TableColumn(name="id_direccion_cliente", datatype="varchar(36)", nullable=False, constraints=[PrimaryKey()]),
        TableColumn(name="id_tipo_direccion", datatype="number(38,0)", nullable=False),
        TableColumn(name="id_cliente", datatype="varchar(36)", nullable=False),
        TableColumn(name="direccion", datatype="varchar", nullable=False),
        TableColumn(name="ciudad", datatype="varchar(255)", nullable=False),
        TableColumn(name="estado", datatype="varchar(255)", nullable=False),
        TableColumn(name="codigo_postal", datatype="varchar(255)", nullable=False),
        TableColumn(name="pais", datatype="varchar(255)", nullable=False)
    ]
)


paqueterias = Table(
    name="paqueterias",
    columns=[
        TableColumn(name="id_paqueteria", datatype="varchar(255)", nullable=False, constraints=[PrimaryKey()]),
        TableColumn(name="nombre_paqueteria", datatype="varchar(255)", nullable=False),
        TableColumn(name="telefono_paqueteria", datatype="varchar(255)", nullable=False)
    ]
)



pago = Table(
    name="pago",
    columns=[
        TableColumn(name="id_pago", datatype="varchar(36)", nullable=False, constraints=[PrimaryKey()]),
        TableColumn(name="id_pedido", datatype="varchar(36)", nullable=False),
        TableColumn(name="metodo_pago", datatype="varchar(255)", nullable=False)
    ]
)



categorias = Table(
    name="categorias",
    columns=[
        TableColumn(name="id_categoria", datatype="number(38,0)", nullable=False, constraints=[PrimaryKey()]),
        TableColumn(name="nombre", datatype="varchar(100)", nullable=False),
        TableColumn(name="parent_id", datatype="number(38,0)")
    ]
)



tipo_direccion = Table(
    name="tipo_direccion",
    columns=[
        TableColumn(name="id_tipo_direccion", datatype="number(38,0)", nullable=False, constraints=[PrimaryKey()]),
        TableColumn(name="tipo_direccion", datatype="varchar(255)", nullable=False)
    ]
)


