from nomad.config.models.plugins import AppEntryPoint

from nomad_laserphysics.apps.measurements import Measurements

measurements_app_entry_point = AppEntryPoint(
    name='Measurements',
    description='App defined using the new plugin mechanism.',
    app=Measurements
)