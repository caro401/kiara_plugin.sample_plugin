# -*- coding: utf-8 -*-

"""Top-level package for kiara_plugin.sample_plugin."""


import os

from kiara.utils.class_loading import (
    KiaraEntryPointItem,
    find_data_types_under,
    find_kiara_model_classes_under,
    find_kiara_modules_under,
    find_pipeline_base_path_for_module,
)

__author__ = """Caro Appleby"""
__email__ = "meow@example.com"


KIARA_METADATA = {
    "authors": [{"name": __author__, "email": __email__}],
    "description": "Kiara modules for: sample-plugin",
    "references": {
        "source_repo": {
            "desc": "The module package git repository.",
            "url": "https://github.com/caro401/kiara_plugin.sample_plugin",
        },
        "documentation": {
            "desc": "The url for the module package documentation.",
            "url": "https://caro401.github.io/kiara_plugin.sample_plugin/",
        },
    },
    "tags": ["sample_plugin"],
    "labels": {"package": "kiara_plugin.sample_plugin"},
}

find_modules: KiaraEntryPointItem = (
    find_kiara_modules_under,
    "kiara_plugin.sample_plugin.modules",
)
find_model_classes: KiaraEntryPointItem = (
    find_kiara_model_classes_under,
    "kiara_plugin.sample_plugin.models",
)
find_data_types: KiaraEntryPointItem = (
    find_data_types_under,
    "kiara_plugin.sample_plugin.data_types",
)
find_pipelines: KiaraEntryPointItem = (
    find_pipeline_base_path_for_module,
    "kiara_plugin.sample_plugin.pipelines",
    KIARA_METADATA,
)


def get_version():
    from importlib.metadata import PackageNotFoundError, version

    try:
        # Change here if project is renamed and does not equal the package name
        dist_name = __name__
        __version__ = version(dist_name)
    except PackageNotFoundError:

        try:
            version_file = os.path.join(os.path.dirname(__file__), "version.txt")

            if os.path.exists(version_file):
                with open(version_file, encoding="utf-8") as vf:
                    __version__ = vf.read()
            else:
                __version__ = "unknown"

        except (Exception):
            pass

        if __version__ is None:
            __version__ = "unknown"

    return __version__
