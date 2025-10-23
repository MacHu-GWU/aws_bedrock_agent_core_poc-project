# -*- coding: utf-8 -*-

if __name__ == "__main__":
    from aws_bedrock_agent_core_poc.tests import run_cov_test

    run_cov_test(
        __file__,
        "aws_bedrock_agent_core_poc",
        is_folder=True,
        preview=False,
    )
