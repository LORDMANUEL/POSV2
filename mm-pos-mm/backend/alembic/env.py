from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy.pool import NullPool
from alembic import context
import sys
import os

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# Add the project root to the Python path
sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), '..')))

# Import all models here so that Alembic can see them
from core.database import Base
from modules.admin import models as admin_models
from modules.inventory import models as inventory_models
from modules.crm import models as crm_models
from modules.pos import models as pos_models
from modules.purchases import models as purchases_models
from modules.loyalty import models as loyalty_models
from modules.restaurant import models as restaurant_models
from modules.integrations import models as integrations_models
from modules.signage import models as signage_models
from modules.kiosk import models as kiosk_models
from core.config import settings

target_metadata = Base.metadata
# Set the sqlalchemy.url in the config object
config.set_main_option('sqlalchemy.url', settings.DATABASE_URL)

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
