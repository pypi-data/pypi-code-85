#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2016, Artem Feofanov <artem.feofanov@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = '''

module: telegram
author:
 - "Artem Feofanov (@tyouxa)"
 - "Nikolai Lomov (@lomserman)"

short_description: module for sending notifications via telegram

description:
    - Send notifications via telegram bot, to a verified group or user.
    - Also, the user may try to use any other telegram bot API method, if you specify I(api_method) argument.
notes:
    - You will require a telegram account and create telegram bot to use this module.
    - The options I(msg), I(msg_format) and I(chat_id) have been deprecated and will be removed in community.general
      4.0.0. Use the corresponding variables in I(api_args) instead. See the examples for how that works.
options:
  token:
    type: str
    description:
      - Token identifying your telegram bot.
    required: true
  api_method:
    type: str
    description:
      - Bot API method.
      - For reference, see U(https://core.telegram.org/bots/api).
    default: SendMessage
    version_added: 2.0.0
  api_args:
    type: dict
    description:
      - Any parameters for the method.
      - For reference to default method, C(SendMessage), see U(https://core.telegram.org/bots/api#sendmessage).
    version_added: 2.0.0
  msg:
    type: str
    description:
      - (Deprecated) What message you wish to send.
  msg_format:
    type: str
    description:
      - (Deprecated) Message format. Formatting options C(markdown), C(MarkdownV2), and C(html) described in
        Telegram API docs (https://core.telegram.org/bots/api#formatting-options).
        If option C(plain) set, message will not be formatted.
    default: plain
    choices: [ "plain", "markdown", "MarkdownV2", "html" ]
  chat_id:
    type: str
    description:
      - (Deprecated) Telegram group or user chat_id.

'''

EXAMPLES = """

- name: Send notify to Telegram
  community.general.telegram:
    token: '9999999:XXXXXXXXXXXXXXXXXXXXXXX'
    api_args:
      chat_id: 000000
      parse_mode: "markdown"
      text: "Your precious application has been deployed: https://example.com"
      disable_web_page_preview: True
      disable_notification: True

- name: Forward message to someone
  community.general.telegram:
    token: '9999999:XXXXXXXXXXXXXXXXXXXXXXX'
    api_method: forwardMessage
    api_args:
      chat_id: 000000
      from_chat_id: 111111
      disable_notification: True
      message_id: '{{ saved_msg_id }}'

- name: Send a message to chat in playbook (deprecated old style)
  community.general.telegram:
    token: '9999999:XXXXXXXXXXXXXXXXXXXXXXX'
    chat_id: 000000
    msg: Ansible task finished
"""

RETURN = """

msg:
  description: The message you attempted to send
  returned: success
  type: str
  sample: "Ansible task finished"
telegram_error:
  description: Error message gotten from Telegram API
  returned: failure
  type: str
  sample: "Bad Request: message text is empty"
"""

import json

from ansible.module_utils.basic import AnsibleModule
# noinspection PyUnresolvedReferences
from ansible.module_utils.six.moves.urllib.parse import quote
from ansible.module_utils.urls import fetch_url


def main():
    module = AnsibleModule(
        argument_spec=dict(
            token=dict(type='str', required=True, no_log=True),
            api_args=dict(type='dict'),
            api_method=dict(type="str", default="SendMessage"),
            chat_id=dict(type='str', no_log=True, removed_in_version='4.0.0',
                         removed_from_collection='community.general'),
            msg=dict(type='str', removed_in_version='4.0.0', removed_from_collection='community.general'),
            msg_format=dict(type='str', choices=['plain', 'markdown', 'html', 'MarkdownV2'], default='plain',
                            removed_in_version='4.0.0', removed_from_collection='community.general'),
        ),
        supports_check_mode=True
    )

    token = quote(module.params.get('token'))
    api_args = module.params.get('api_args') or {}
    api_method = module.params.get('api_method')
    # filling backward compatibility args
    api_args['chat_id'] = api_args.get('chat_id') or module.params.get('chat_id')
    api_args['parse_mode'] = api_args.get('parse_mode') or module.params.get('msg_format')
    api_args['text'] = api_args.get('text') or module.params.get('msg')

    if api_args['parse_mode'] == 'plain':
        del api_args['parse_mode']

    url = 'https://api.telegram.org/bot{token}/{api_method}'.format(token=token, api_method=api_method)

    if module.check_mode:
        module.exit_json(changed=False)

    response, info = fetch_url(module, url, method="POST", data=json.dumps(api_args),
                               headers={'Content-Type': 'application/json'})
    if info['status'] == 200:
        module.exit_json(changed=True)
    elif info['status'] == -1:
        # SSL errors, connection problems, etc.
        module.fail_json(msg="Failed to send message", info=info, response=response)
    else:
        body = json.loads(info['body'])
        module.fail_json(
            msg="Failed to send message, return status = {status}\n"
                "url = {api_url}\n"
                "api_args = {api_args}".format(
                    status=info['status'], api_url=url, api_args=api_args
                ),
            telegram_error=body['description'],
        )


if __name__ == '__main__':
    main()
