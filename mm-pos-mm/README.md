# MM (POS VENTA MULTI)

MM es un sistema POS empresarial modular diseñado para integrar todas las operaciones de un negocio en un ecosistema unificado. Ofrece flexibilidad, escalabilidad y eficiencia a empresas de todos los tamaños, adaptándose a múltiples industrias como retail, restaurantes y servicios.

## Módulos Principales

El sistema está compuesto por los siguientes módulos:

-   **POS (Punto de Venta)**: Gestión de ventas, devoluciones, caja y recibos.
-   **Inventario**: Control de productos, stock, movimientos y alertas.
-   **Compras**: Gestión de órdenes de compra, recepciones y proveedores.
-   **CRM**: Administración de clientes, puntos de lealtad y campañas de marketing.
-   **Admin**: Gestión de usuarios, roles, sucursales y configuración del sistema.
-   **IA (Inteligencia Artificial)**: Reportes inteligentes, alertas de fraude y recomendaciones.
-   **OpenSignage**: Gestión de pantallas y contenido digital.
-   **Kioskos**: Terminales de autoservicio para clientes.
-   **Portal Cliente**: Portal web para que los clientes consulten sus pedidos y puntos.
-   **Loyalty**: Gestión de gift cards, notas de crédito y membresías.
-   **Restaurante**: Gestión de mesas, órdenes y comandas.
-   **Integraciones**: Conexión con plataformas externas como e-commerce y sistemas de contabilidad.

## Cómo Levantar el Sistema con Docker

1.  **Clonar el repositorio:**
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd mm-pos-mm
    ```

2.  **Configurar las variables de entorno:**
    Copie el archivo de ejemplo `.env.example` y ajústelo según sea necesario.
    ```bash
    cp infra/env/.env.example infra/env/.env
    ```

3.  **Levantar los servicios con Docker Compose:**
    ```bash
    docker-compose -f infra/docker-compose.yml up -d
    ```

## Usuarios Demo

-   **Administrador:**
    -   **Usuario:** admin@example.com
    -   **Contraseña:** admin
-   **Cajero:**
    -   **Usuario:** cashier@example.com
    -   **Contraseña:** cashier
