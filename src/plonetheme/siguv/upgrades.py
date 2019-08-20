# -*- coding: utf-8 -*-

import logging


logger = logging.getLogger(__name__)


def to_1010(context):
    context.runAllImportStepsFromProfile('plonetheme.siguv:to_1010')
    logger.info('Updated registry-entries for less cache key')
