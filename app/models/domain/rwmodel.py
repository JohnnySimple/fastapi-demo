from pydantic import BaseConfig, BaseModel

class RWModel(BaseModel):
    class Config(BaseConfig):
        allow_population_by_field_name = True
        use_enum_values = True