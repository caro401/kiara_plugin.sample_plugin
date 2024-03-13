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


def get_version() -> str:
    from importlib.metadata import PackageNotFoundError, version

    __version__ = "unknown"
    try:
        # Pass something other than __name__ if project is renamed to something other than the package name
        __version__ = version(__name__)
    except PackageNotFoundError:
        try:
            version_file = os.path.join(os.path.dirname(__file__), "version.txt")
            with open(version_file, encoding="utf-8") as vf:
                __version__ = vf.read()
                # TODO should we be validating anything about what the version is? nonempty at least?

        except OSError:  # noqa=S110
            # File missing, you don't have permissions to open it, or something else filesystem-related went wrong
            pass

    return __version__
