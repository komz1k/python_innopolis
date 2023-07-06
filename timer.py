import asyncio


class Countdown:
    def __init__(self, sec: int, name: str):
        self._sec = sec
        self._name = name

    async def start(self):
        for i in range(self._sec, -1, -1):
            await asyncio.sleep(1)
            print(self._name, i)

        self.ready()

    def ready(self):
        print(f"{self._name} done")


async def main():
    cd1 = Countdown(5, "first")
    cd2 = Countdown(3, "second")
    await asyncio.gather(cd1.start(), cd2.start())

asyncio.run(main())
