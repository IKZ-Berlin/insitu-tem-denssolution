from nomad.config.models.plugins import SchemaPackageEntryPoint
from pydantic import Field


class MySchemaPackageEntryPoint(SchemaPackageEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from nomad_insitu_tem_denssolutions.schema_packages.mypackage import m_package

        return m_package


mypackage = MySchemaPackageEntryPoint(
    name='MyPackage',
    description='Schema package defined using the new plugin mechanism.',
)


class DensSolutionsPackageEntryPoint(SchemaPackageEntryPoint):
    # parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from nomad_insitu_tem_denssolutions.schema_packages.denssolutions import (
            m_package,
        )

        return m_package


denssolutions = DensSolutionsPackageEntryPoint(
    name='DensSolutions',
    description='Schema package defined using the new plugin mechanism.',
)
