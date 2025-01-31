from nomad.config.models.plugins import SchemaPackageEntryPoint
from pydantic import Field


class TipSchemaPackageEntryPoint(SchemaPackageEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from src.nomad_laserphysics.schema_packages.tip_sample_schema import m_package

        return m_package

class ElnSchemaPackageEntryPoint(SchemaPackageEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from src.nomad_laserphysics.schema_packages.FEM_correlation_chamber import m_package

        return m_package

eln_schema_package_entry_point = ElnSchemaPackageEntryPoint(
    name='eln schema',
    description='New schema package entry point configuration.',
    plugin_package='schema_packages',
)

tip_schema_package_entry_point = TipSchemaPackageEntryPoint(
    name='tip schema',
    description='New schema package entry point configuration.',
    plugin_package='schema_packages',
)
