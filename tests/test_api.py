# -*- coding: utf-8 -*-

from aws_bedrock_agent_core_poc import api


def test():
    _ = api


if __name__ == "__main__":
    from aws_bedrock_agent_core_poc.tests import run_cov_test

    run_cov_test(
        __file__,
        "aws_bedrock_agent_core_poc.api",
        preview=False,
    )
