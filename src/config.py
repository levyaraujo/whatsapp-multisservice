from dynaconf import Dynaconf, FlaskDynaconf

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=["settings.toml", ".secrets.toml"],
    environments=["default", "development", "testing", "docker", "production"],
    load_dotenv=True,
    env_switcher="CHATENV",
)


def init(app):
    FlaskDynaconf(app=app)


# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.
