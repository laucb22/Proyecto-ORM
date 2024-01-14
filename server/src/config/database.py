from playhouse.cockroachdb import CockroachDatabase

#Variable a exportar para la conexión a la base de datos
DB = CockroachDatabase(
    "postgresql://charrin:G96BcOEZo4vEGoU7mWe71w@ochre-werecat-12359.8nj.cockroachlabs.cloud:26257/orm_project?sslmode=verify-full"
)

