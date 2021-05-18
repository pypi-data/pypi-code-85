# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from mozphab.arcanist import update_arc
from mozphab.config import config
from mozphab.updater import self_upgrade


def self_update(_):
    """`self-update` command, updates arc and this package"""
    # Update arc.
    if config.arc_last_check >= 0:
        update_arc()

    # Upgrade self
    self_upgrade()


def add_parser(parser):
    update_parser = parser.add_parser("self-update", help="Update review script")
    update_parser.set_defaults(func=self_update, needs_repo=False, no_arc=True)
