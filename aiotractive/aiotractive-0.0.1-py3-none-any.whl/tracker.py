from datetime import datetime, timedelta

from .data_object import DataObject


class Tracker(DataObject):
    ACTIONS = {True: "on", False: "off"}

    async def hw_info(self):
        return await self._api.request(f"device_hw_report/{self._id}/")

    async def positions(self, time_from=datetime.now() - timedelta(hours=6), time_to=datetime.now()):
        return await self._api.request(
            f"tracker/{self._id}/positions",
            params={
                "time_from": round(time_from.timestamp()),
                "time_to": round(time_to.timestamp()),
                "format": "json_segments",
            },
        )

    async def set_buzzer_active(self, active):
        action = self.ACTIONS[active]

        return await self._api.request(f"tracker/{self._id}/command/buzzer_control/{action}")

    async def set_led_active(self, active):
        action = self.ACTIONS[active]

        return await self._api.request(f"tracker/{self._id}/command/led_control/{action}")

    async def set_live_tracking_active(self, active):
        action = self.ACTIONS[active]

        return await self._api.request(f"tracker/{self._id}/command/live_tracking/{action}")
