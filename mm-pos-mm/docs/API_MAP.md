# Mapa de APIs del Sistema MM

A continuación se presenta un mapa global de endpoints REST del sistema MM, organizados por módulo funcional. Todas las rutas asumen un prefijo base `/api/v1`.

## TPV (Punto de Venta)
-   `POST /pos/sales`: Registrar una nueva venta.
-   `GET /pos/sales/{id}`: Consultar detalle de venta.
-   `POST /pos/sales/{id}/refund`: Procesar devolución de una venta.
-   `POST /pos/sales/{id}/tip`: Registrar propina.
-   `POST /pos/register/open`: Apertura de caja.
-   `POST /pos/register/close`: Cierre de caja.
-   `GET /pos/register/status`: Estado de caja actual.
-   `GET /pos/receipts/{id}/digital`: Obtener recibo digital.

## Inventario
-   `GET /inventory/products`: Listado de productos.
-   `POST /inventory/products`: Crear/editar producto.
-   `GET /inventory/stock/{product_id}`: Consulta de stock para un producto.
-   `POST /inventory/movements`: Registrar movimiento de stock.
-   `POST /inventory/kits`: Crear/actualizar kit/paquete de productos.
-   `GET /inventory/alerts`: Alertas inteligentes de inventario.

## Compras y Proveedores
-   `POST /purchases/orders`: Crear orden de compra.
-   `PUT /purchases/orders/{id}/receive`: Recepción de mercancía.
-   `POST /purchases/orders/{id}/return`: Devolver a proveedor.
-   `GET /purchases/suppliers`: Listado de proveedores.
-   `GET /purchases/payables`: Cuentas por pagar.

## CRM y Marketing
-   `GET /crm/customers`: Listado de clientes.
-   `POST /crm/customers`: Crear/editar cliente.
-   `GET /crm/customers/{id}/loyalty`: Consultar cuenta de lealtad.
-   `POST /crm/customers/{id}/loyalty/redeem`: Redimir puntos.
-   `GET /crm/rfm-segments`: Segmentos RFM.
-   `POST /crm/campaigns`: Crear campaña de marketing.
-   `GET /crm/feedback`: Feedback de clientes.

## Administración y Seguridad
-   `GET /admin/branches`: Listar sucursales.
-   `POST /admin/branches`: Crear/editar sucursal.
-   `GET /admin/users`: Listar usuarios.
-   `POST /admin/users`: Crear/editar usuario.
-   `GET /admin/roles`: Listar roles.
-   `POST /admin/roles`: Crear/editar rol.
-   `GET /admin/logs`: Ver logs de seguridad.
-   `GET /admin/settings`: Configuración global.
-   `POST /admin/settings`: Actualizar configuración global.
-   `POST /admin/offline-sync`: Forzar sincronización offline.
-   `GET /admin/health`: Salud del sistema.
-   `POST /admin/webhooks`: Registrar webhook/API key.

## IA Operativa
-   `GET /ai/reports`: Reporte inteligente.
-   `GET /ai/fraud-alerts`: Alertas de fraude.
-   `GET /ai/recommendations`: Recomendaciones operativas.
-   `POST /ai/chat-assistant`: Asistente conversacional.

## OpenSignage
-   `GET /signage/screens`: Listar pantallas.
-   `POST /signage/screens`: Registrar nueva pantalla.
-   `POST /signage/content`: Crear contenido de pantalla.
-   `POST /signage/content/ai-generate`: Generar diseño con IA.
-   `GET /signage/playlists`: Consultar playlists.
-   `POST /signage/playlists`: Programar contenido.
-   `POST /signage/themes`: Administrar temas de diseño.

## Kioskos
-   `GET /kiosk/catalog`: Catálogo de productos para kiosko.
-   `POST /kiosk/order`: Iniciar orden self-service.
-   `POST /kiosk/order/{id}/pay`: Pago de orden self-service.
-   `GET /kiosk/order/{id}/status`: Estado de orden self-service.

## Portal Cliente
-   `POST /customer/login`: Login de cliente.
-   `GET /customer/profile`: Perfil del cliente.
-   `GET /customer/orders`: Historial de pedidos del cliente.
-   `GET /customer/orders/{id}`: Detalle de pedido específico.
-   `GET /customer/loyalty`: Información de lealtad.
-   `GET /customer/rewards`: Recompensas disponibles.
-   `POST /customer/feedback`: Enviar feedback.

## Loyalty (Gift Cards, Notas de Crédito, Membresías)
-   `POST /loyalty/giftcards`: Emitir gift card.
-   `GET /loyalty/giftcards/{code}`: Consultar saldo de una gift card.
-   `POST /loyalty/giftcards/{code}/redeem`: Usar gift card.
-   `POST /loyalty/credit-notes`: Emitir nota de crédito.
-   `GET /loyalty/credit-notes/{id}`: Consultar saldo de nota de crédito.
-   `POST /loyalty/memberships`: Crear/actualizar nivel de membresía.
-   `POST /loyalty/customers/{id}/membership`: Asignar membresía a cliente.

## Restaurante y Comandas
-   `GET /restaurant/tables`: Mapa de mesas y su estado.
-   `POST /restaurant/tables/{id}/open`: Apertura de mesa.
-   `POST /restaurant/orders`: Tomar orden en mesa.
-   `POST /restaurant/orders/{id}/item`: Agregar ítem a orden existente.
-   `POST /restaurant/orders/{id}/split`: Dividir cuenta.
-   `GET /restaurant/areas`: Áreas de impresión.
-   `POST /restaurant/areas`: Configurar área.
-   `POST /restaurant/print/{order_id}`: Imprimir comanda manual.

## Integraciones Externas
-   `POST /integrations/ecommerce/{platform}/sync`: Forzar sincronización e-commerce.
-   `GET /integrations/ecommerce/{platform}/status`: Estado de integración.
-   `POST /integrations/delivery/{platform}/webhook`: Recibir pedido de delivery.
-   `GET /integrations/accounting/export`: Exportar ventas a contabilidad.
