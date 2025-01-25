"""
This module contains the registry for the pipelines in the project.
"""

from suml.pipelines import pipeline as ds_pipeline


def register_pipelines():
    """
    Registers and returns a set of pipelines for data processing tasks.

    Returns:
        dict[str, Pipeline]: A mapping of pipeline names to their pipeline objects.
        The "ds" key references a data science pipeline and the "__default__" key
        references the default pipeline used in the system.
    """
    return {
        "ds": ds_pipeline.create_pipeline(),
        "__default__": ds_pipeline.create_pipeline(),
    }
