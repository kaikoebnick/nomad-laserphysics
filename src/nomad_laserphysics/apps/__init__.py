from nomad.config.models.plugins import AppEntryPoint

from nomad_laserphysics.apps.evaluations import Evaluations
from nomad_laserphysics.apps.measurements import Measurements
from nomad_laserphysics.apps.objects import Objects

measurements_app_entry_point = AppEntryPoint(
    label='Measurements',
    description='App defined using the new plugin mechanism.',
    app=Measurements
)
evaluations_app_entry_point = AppEntryPoint(
    label='Evaluations',
    description='App defined using the new plugin mechanism.',
    app=Evaluations
)
objects_app_entry_point = AppEntryPoint(
    label='Objects',
    description='App defined using the new plugin mechanism.',
    app=Objects
)
