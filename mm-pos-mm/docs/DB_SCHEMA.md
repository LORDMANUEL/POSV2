# Esquema de la Base de Datos del Sistema MM

Este documento describe las tablas clave y sus relaciones en la base de datos PostgreSQL del sistema MM.

## Tablas Principales

-   **branch**: Almacena las sucursales del negocio.
-   **user**: Contiene los usuarios del sistema (empleados).
-   **role**: Define los roles y permisos de los usuarios.
-   **product**: Maestro de productos y servicios. Utiliza JSONB para atributos flexibles.
-   **stock**: Control de existencias por producto y sucursal.
-   **stock_move**: Historial de movimientos de inventario (kardex).
-   **sale**: Encabezado de las transacciones de venta.
-   **sale_item**: Detalle de los productos vendidos en cada transacción.
-   **payment**: Registra los pagos asociados a una venta.
-   **register_shift**: Control de los turnos de caja (aperturas y cierres).
-   **register_audit**: Auditoría de eventos sensibles en la caja.
-   **customer**: Perfil de los clientes del CRM.
-   **loyalty_tx**: Historial de transacciones de puntos de lealtad.
-   **supplier**: Información de los proveedores.
-   **purchase_order**: Órdenes de compra a proveedores.
-   **purchase_item**: Detalle de las órdenes de compra.
-   **supplier_invoice**: Facturas de proveedores (cuentas por pagar).
-   **campaign**: Campañas de marketing del CRM.
-   **feedback**: Comentarios y calificaciones de los clientes.
-   **system_settings**: Configuración global del sistema. Utiliza JSONB.
-   **gift_card**: Gift cards emitidas con su saldo.
-   **credit_note**: Notas de crédito generadas.
-   **restaurant_table**: Mesas del módulo de restaurante.
-   **restaurant_order**: Órdenes de restaurante asociadas a mesas.
-   **restaurant_order_item**: Detalle de las órdenes de restaurante.

## Uso de JSONB

El tipo de dato `JSONB` se utiliza en varias tablas para proporcionar flexibilidad al esquema sin necesidad de migraciones constantes. Algunos ejemplos notables son:

-   `product.attributes`: Para almacenar atributos específicos de cada producto (talla, color, especificaciones técnicas, etc.).
-   `branch.settings`: Para configuraciones particulares de cada sucursal (IP de la impresora, tema visual, etc.).
-   `role.permissions`: Para definir los permisos de acceso de cada rol de manera granular.
-   `system_settings.config`: Para almacenar la configuración global del sistema de forma flexible.
-   `supplier.data`: Para guardar información adicional y flexible sobre los proveedores.
-   `campaign.segment`: Para definir los criterios de segmentación de las campañas de marketing.
