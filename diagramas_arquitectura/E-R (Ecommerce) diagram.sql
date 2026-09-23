CREATE TABLE "productos" (
  "id_producto" UUID PRIMARY KEY NOT NULL,
  "name_producto" "VARCHAR(255)" NOT NULL,
  "descripcion_producto" TEXT NOT NULL,
  "id_categoria" INTEGER NOT NULL,
  "precio_base_producto" "DECIMAL(8,2)" NOT NULL,
  "fecha_creacion_producto" "TIMESTAMP(0)" NOT NULL
);

CREATE TABLE "variantes_producto" (
  "id_variante" UUID PRIMARY KEY NOT NULL,
  "id_producto" UUID NOT NULL,
  "sku" "VARCHAR(255)" UNIQUE NOT NULL,
  "talla" "VARCHAR(255)" NOT NULL,
  "color" "VARCHAR(255)" NOT NULL,
  "stock_disponible" INTEGER NOT NULL,
  "precio_especifico" "DECIMAL(8,2)",
  "precio_oferta" "DECIMAL(8,2)",
  "codigo_barras" VARCHAR NOT NULL
);

CREATE TABLE "clientes" (
  "id_cliente" UUID PRIMARY KEY NOT NULL,
  "email" "VARCHAR(255)" UNIQUE NOT NULL,
  "nombre" "VARCHAR(255)" NOT NULL,
  "apellidos" "VARCHAR(255)" NOT NULL,
  "password_hash" "VARCHAR(255)" NOT NULL,
  "telefono" "VARCHAR(255)" NOT NULL,
  "fecha_registro" "TIMESTAMP(0)" NOT NULL
);

CREATE TABLE "pedidos" (
  "id_pedido" UUID PRIMARY KEY NOT NULL,
  "id_cliente" UUID NOT NULL,
  "id_direccion_cliente" UUID NOT NULL,
  "id_paqueteria" "VARCHAR(255)" NOT NULL,
  "fecha_entrega_pedido" "TIMESTAMP(0)" NOT NULL,
  "status_pedido" "VARCHAR(100)" NOT NULL,
  "total_pagado" "DECIMAL(8,2)" NOT NULL,
  "direccion_entrega" TEXT NOT NULL,
  "fecha_pedido" "TIMESTAMP(0)" NOT NULL
);

CREATE TABLE "lineas_pedido" (
  "id_linea" UUID PRIMARY KEY NOT NULL,
  "id_pedido" UUID NOT NULL,
  "id_variante" UUID NOT NULL,
  "cantidad" INTEGER NOT NULL,
  "precio_unitario" "DECIMAL(8,2)" NOT NULL,
  "subtotal" "DECIMAL(8,2)" NOT NULL
);

CREATE TABLE "direccion_cliente" (
  "id_direccion_cliente" UUID PRIMARY KEY NOT NULL,
  "id_tipo_direccion" INTEGER NOT NULL,
  "id_cliente" UUID NOT NULL,
  "direccion" TEXT NOT NULL,
  "ciudad" "VARCHAR(255)" NOT NULL,
  "estado" "VARCHAR(255)" NOT NULL,
  "codigo_postal" "VARCHAR(255)" NOT NULL,
  "pais" "VARCHAR(255)" NOT NULL
);

CREATE TABLE "paqueterias" (
  "id_paqueteria" "VARCHAR(255)" PRIMARY KEY NOT NULL,
  "nombre_paqueteria" "VARCHAR(255)" NOT NULL,
  "telefono_paqueteria" "VARCHAR(255)" NOT NULL
);

CREATE TABLE "pago" (
  "id_pago" UUID PRIMARY KEY NOT NULL,
  "id_pedido" UUID NOT NULL,
  "metodo_pago" "VARCHAR(255)" NOT NULL
);

CREATE TABLE "categorias" (
  "id_categoria" INTEGER PRIMARY KEY NOT NULL,
  "nombre" "VARCHAR(100)" NOT NULL,
  "parent_id" INTEGER
);

CREATE TABLE "tipo_direccion" (
  "id_tipo_direccion" INTEGER PRIMARY KEY NOT NULL,
  "tipo_direccion" "VARCHAR(255)" NOT NULL
);

ALTER TABLE "lineas_pedido" ADD CONSTRAINT "lineas_pedido_id_variante_foreign" FOREIGN KEY ("id_variante") REFERENCES "variantes_producto" ("id_variante") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "lineas_pedido" ADD CONSTRAINT "lineas_pedido_id_pedido_foreign" FOREIGN KEY ("id_pedido") REFERENCES "pedidos" ("id_pedido") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "productos" ADD CONSTRAINT "categorias_id_categoria_foreign" FOREIGN KEY ("id_categoria") REFERENCES "categorias" ("id_categoria") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "tipo_direccion" ADD CONSTRAINT "tipo_direccion_id_tipo_direccion_foreign" FOREIGN KEY ("id_tipo_direccion") REFERENCES "direccion_cliente" ("id_tipo_direccion") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "variantes_producto" ADD CONSTRAINT "variantes_producto_id_producto_foreign" FOREIGN KEY ("id_producto") REFERENCES "productos" ("id_producto") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "pedidos" ADD CONSTRAINT "pedidos_id_cliente_foreign" FOREIGN KEY ("id_cliente") REFERENCES "clientes" ("id_cliente") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "pedidos" ADD CONSTRAINT "pedidos_id_direccion_cliente_foreign" FOREIGN KEY ("id_direccion_cliente") REFERENCES "direccion_cliente" ("id_direccion_cliente") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "pedidos" ADD CONSTRAINT "pedidos_id_pedido_foreign" FOREIGN KEY ("id_pedido") REFERENCES "pago" ("id_pedido") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "categorias" ADD FOREIGN KEY ("parent_id") REFERENCES "categorias" ("id_categoria") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "direccion_cliente" ADD FOREIGN KEY ("id_cliente") REFERENCES "clientes" ("id_cliente") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "pedidos" ADD FOREIGN KEY ("id_paqueteria") REFERENCES "paqueterias" ("id_paqueteria") DEFERRABLE INITIALLY IMMEDIATE;
