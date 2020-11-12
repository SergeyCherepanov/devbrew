#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for ios_lacp
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'network'
}

DOCUMENTATION = """
---
module: ios_lacp
version_added: 2.9
short_description: Manage Global Link Aggregation Control Protocol (LACP) on Cisco IOS devices.
description: This module provides declarative management of Global LACP on Cisco IOS network devices.
author: Sumit Jaiswal (@justjais)
notes:
  - Tested against Cisco IOSv Version 15.2 on VIRL
  - This module works with connection C(network_cli),
    See L(IOS Platform Options,../network/user_guide/platform_ios.html).
options:
  config:
    description: The provided configurations.
    type: dict
    suboptions:
      system:
        description: This option sets the default system parameters for LACP.
        type: dict
        suboptions:
          priority:
            description:
            - LACP priority for the system.
            - Refer to vendor documentation for valid values.
            type: int
            required: True
  state:
    description:
    - The state of the configuration after module completion
    type: str
    choices:
    - merged
    - replaced
    - deleted
    default: merged
"""

EXAMPLES = """

# Using merged
#
# Before state:
# -------------
#
# vios#show lacp sys-id
# 32768, 5e00.0000.8000

- name: Merge provided configuration with device configuration
  ios_lacp:
    config:
      system:
        priority: 123
    state: merged

# After state:
# ------------
#
# vios#show lacp sys-id
# 123, 5e00.0000.8000

# Using replaced
#
# Before state:
# -------------
#
# vios#show lacp sys-id
# 500, 5e00.0000.8000

- name: Replaces Global LACP configuration
  ios_lacp:
    config:
      system:
        priority: 123
    state: replaced

# After state:
# ------------
#
# vios#show lacp sys-id
# 123, 5e00.0000.8000

# Using Deleted
#
# Before state:
# -------------
#
# vios#show lacp sys-id
# 500, 5e00.0000.8000

- name: Delete Global LACP attribute
  ios_lacp:
    state: deleted

# After state:
# -------------
#
# vios#show lacp sys-id
# 32768, 5e00.0000.8000

"""

RETURN = """
before:
  description: The configuration as structured data prior to module invocation.
  returned: always
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The configuration as structured data after module completion.
  returned: when changed
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['lacp system-priority 10']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.network.ios.argspec.lacp.lacp import LacpArgs
from ansible.module_utils.network.ios.config.lacp.lacp import Lacp


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    required_if = [('state', 'merged', ('config',)),
                   ('state', 'replaced', ('config',))]

    module = AnsibleModule(argument_spec=LacpArgs.argument_spec,
                           required_if=required_if,
                           supports_check_mode=True)

    result = Lacp(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
