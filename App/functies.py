from xknx import XKNX

async def S1A():
    xknx = XKNX(config='xknx.yaml')
    await xknx.start()
    await xknx.devices['schakelaar1.Light_1'].set_on()
    await xknx.stop()

async def S2A():
    xknx = XKNX(config='xknx.yaml')
    await xknx.start()
    await xknx.devices['schakelaar2.Light_1'].set_on()
    await xknx.stop()

async def S3A():
    xknx = XKNX(config='xknx.yaml')
    await xknx.start()
    await xknx.devices['schakelaar3.Light_1'].set_on()
    await xknx.stop()

async def S4A():
    xknx = XKNX(config='xknx.yaml')
    await xknx.start()
    await xknx.devices['schakelaar4.Light_1'].set_brightness(255/3)
    await xknx.stop()

async def S1U():
    xknx = XKNX(config='xknx.yaml')
    await xknx.start()
    await xknx.devices['schakelaar1.Light_1'].set_off()
    await xknx.stop()

async def S2U():
    xknx = XKNX(config='xknx.yaml')
    await xknx.start()
    await xknx.devices['schakelaar2.Light_1'].set_off()
    await xknx.stop()

async def S3U():
    xknx = XKNX(config='xknx.yaml')
    await xknx.start()
    await xknx.devices['schakelaar3.Light_1'].set_off()
    await xknx.stop()

async def S4U():
    xknx = XKNX(config='xknx.yaml')
    await xknx.start()
    await xknx.devices['schakelaar4.Light_1'].set_off()
    await xknx.stop()