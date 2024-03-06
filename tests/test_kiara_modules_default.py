#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `kiara_plugin.sample_plugin` package."""

import kiara_plugin.sample_plugin
import pytest  # noqa


def test_assert():

    assert kiara_plugin.sample_plugin.get_version() is not None
