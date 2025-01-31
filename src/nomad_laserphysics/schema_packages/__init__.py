from nomad.config.models.plugins import SchemaPackageEntryPoint
from pydantic import Field


class TipSampleSchemaPackageEntryPoint(SchemaPackageEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from src.nomad_laserphysics.schema_packages.tip_sample_schema import m_package

        return m_package

class FEMCorrelationChamberSchemaPackageEntryPoint(SchemaPackageEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from src.nomad_laserphysics.schema_packages.FEM_correlation_chamber_schema import m_package

        return m_package

FEM_correlation_chamber_schema_package_entry_point = FEMCorrelationChamberSchemaPackageEntryPoint(
    name='FEM correlation chamber schema',
    description='New schema package entry point configuration.',
    plugin_package='schema_packages',
)

tip_sample_schema_package_entry_point = TipSampleSchemaPackageEntryPoint(
    name='tip sample schema',
    description='New schema package entry point configuration.',
    plugin_package='schema_packages',
)
