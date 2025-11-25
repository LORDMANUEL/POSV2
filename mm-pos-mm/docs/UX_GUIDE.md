# Guía de UX y Patrones de UI del Sistema MM

Este documento establece los patrones de diseño y la guía de estilo para la interfaz de usuario (UI) del sistema MM, asegurando una experiencia de usuario (UX) coherente y moderna en todos los módulos.

## Filosofía de Diseño: Liquid Glass / Glassmorphism

La interfaz de MM se basa en el estilo **Liquid Glass** o **Glassmorphism**. Este enfoque se caracteriza por:

-   **Transparencia y Desenfoque (Blur)**: Los elementos de la UI, como tarjetas y paneles, tienen un fondo translúcido con un efecto de desenfoque de fondo (`backdrop-blur`), creando una sensación de profundidad y jerarquía.
-   **Bordes Sutiles**: Los contenedores tienen bordes delgados y semitransparentes para definir su forma sin ser visualmente pesados.
-   **Sombras Suaves**: Se utilizan sombras difusas para levantar los elementos del fondo, mejorando la legibilidad y la percepción de capas.
-   **Colores Vibrantes y Gradientes**: Sobre un fondo oscuro o con gradientes suaves, se utilizan colores brillantes y acentos para resaltar acciones importantes y guiar al usuario.

Todo el estilado se implementará exclusivamente con **Tailwind CSS**.

## Layout Principal

La aplicación principal sigue un diseño de dashboard consistente:

-   **Sidebar Izquierda**:
    -   Estilo "glass" (`backdrop-blur bg-white/10`).
    -   Contiene la navegación principal a los diferentes módulos.
    -   Bordes redondeados (`rounded-3xl`) y sombras suaves (`shadow-xl`).
-   **Topbar Superior**:
    -   También de estilo "glass".
    -   Muestra el perfil del usuario, selector de sucursal y notificaciones.
-   **Fondo General**:
    -   Utiliza gradientes suaves (ej. `bg-gradient-to-br from-slate-900 to-slate-800`) para crear un ambiente moderno y oscuro que haga resaltar los elementos "glass".

## Componentes Base Reutilizables

Para mantener la consistencia, se utilizará un conjunto de componentes base pre-estilizados:

-   `GlassCard`: El componente principal para contener información.
    -   Clases: `rounded-3xl bg-white/10 border border-white/20 backdrop-blur-lg shadow-xl`
-   `GlassButton`: Para todas las acciones interactivas.
    -   Incluye transiciones suaves (`transition-all`), efectos de `hover` (escala y brillo) y sombras.
-   `GlassInput`: Campos de formulario estilizados.
    -   Fondos transparentes, bordes sutiles y estados de `focus` claros.
-   `GlassModal`: Ventanas modales para diálogos y formularios.
    -   Animación de aparición y desaparición (escala y opacidad).
-   `DataTable`: Tablas de datos estandarizadas.
    -   Con paginación, filtros y acciones por fila.

## Estados de la UI

Cada página y componente debe manejar de forma explícita los siguientes estados para ofrecer una UX clara y sin fricciones:

-   **Estado de Carga (Loading)**:
    -   Mostrar spinners o skeletons mientras se cargan los datos. Esto evita pantallas en blanco y comunica que el sistema está trabajando.
-   **Estado Vacío (Empty)**:
    -   Cuando una lista o tabla no tiene datos, mostrar un mensaje amigable con un icono. (Ej. "No se encontraron productos. ¡Crea el primero!").
-   **Estado de Error (Error)**:
    -   Mostrar alertas claras y concisas cuando una operación falla. Proporcionar información útil sobre el error si es posible.

## Animaciones y Transiciones

-   Se utilizarán animaciones sutiles para mejorar la experiencia sin distraer.
-   Todas las transiciones de estado (hover, focus, etc.) serán suaves (`transition-all duration-200/300`).
-   La carga de páginas y módulos puede incluir un efecto de "fade-in" para una aparición más fluida.

La adhesión estricta a esta guía asegurará que el sistema MM no solo sea funcionalmente robusto, sino también visualmente atractivo, intuitivo y coherente en toda la plataforma.
