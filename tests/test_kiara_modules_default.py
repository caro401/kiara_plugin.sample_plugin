#!/usr/bin/env python
# -*- coding: utf-8 -*-


import kiara_plugin.sample_plugin


def test_get_plugin_version_returns_a_value():
    assert kiara_plugin.sample_plugin.get_version() is not None
